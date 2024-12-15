import os
import psycopg2
from io import BytesIO
from keras.models import load_model
from keras.datasets import mnist
from PIL import Image
import numpy as np

# Database connection details
DB_HOST = os.getenv("DB_HOST", "localhost")
DB_PORT = os.getenv("DB_PORT", "5432")
DB_USER = os.getenv("DB_USER", "user")
DB_PASSWORD = os.getenv("DB_PASSWORD", "password")
DB_NAME = os.getenv("DB_NAME", "milestone_3")

# Connect to the PostgreSQL database
def connect_db():
    return psycopg2.connect(
        host=DB_HOST,
        port=DB_PORT,
        user=DB_USER,
        password=DB_PASSWORD,
        database=DB_NAME
    )

# Initialize the database and tables
def init_db(conn):
    with conn.cursor() as cursor:
        cursor.execute("SELECT 1 FROM pg_database WHERE datname = 'milestone_3';")
        if cursor.fetchone():
            print("Database already initialized.")
            return
        cursor.execute("CREATE TABLE IF NOT EXISTS input_data (id SERIAL PRIMARY KEY, image BYTEA NOT NULL);")
        cursor.execute("CREATE TABLE IF NOT EXISTS predictions (id SERIAL PRIMARY KEY, prediction INT NOT NULL, input_id INT REFERENCES input_data (id));")
        conn.commit()

# Load the neural network model
def load_model_from_volume():
    return load_model("/usr/src/app/model/saved_model")

# Serialize image to binary
def serialize_image(image):
    byte_stream = BytesIO()
    Image.fromarray(image).save(byte_stream, format='PNG')
    return byte_stream.getvalue()

# Deserialize image from binary
def deserialize_image(image_binary):
    return Image.open(BytesIO(image_binary))

# Main logic
def main():
    conn = connect_db()
    init_db(conn)

    # Load MNIST data
    (x_train, y_train), _ = mnist.load_data()
    sample_image = x_train[0]
    sample_label = y_train[0]

    # Save image to database
    with conn.cursor() as cursor:
        image_binary = serialize_image(sample_image)
        cursor.execute("INSERT INTO input_data (image) VALUES (%s) RETURNING id;", (image_binary,))
        input_id = cursor.fetchone()[0]

    # Load image from database
    with conn.cursor() as cursor:
        cursor.execute("SELECT image FROM input_data WHERE id = %s;", (input_id,))
        image_binary = cursor.fetchone()[0]
        fetched_image = deserialize_image(image_binary)

    # Predict using the model
    model = load_model_from_volume()
    prediction = np.argmax(model.predict(fetched_image.resize((28, 28)).convert("L").reshape(1, 28, 28, 1)))

    # Save prediction to database
    with conn.cursor() as cursor:
        cursor.execute("INSERT INTO predictions (prediction, input_id) VALUES (%s, %s);", (prediction, input_id))
        conn.commit()

    print(f"Prediction saved: {prediction}")
    conn.close()

if __name__ == "__main__":
    main()
