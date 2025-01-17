import os
from io import BytesIO
from PIL import Image
import numpy as np
import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
from app.model import load_model

# Model Path to load the model

MODEL_PATH = os.getenv("MODEL_PATH", "src/app/model/saved_model.keras")


def connect_db():
    """Establish a connection to the PostgreSQL database and create mnist_db database if it doesn't exist"""
    connection = None
    cursor = None

    for i in range(5):
        try:
            connection= psycopg2.connect(
                host="db",
                port=5432,
                user="postgres",
                password="",
                database="postgres",
            )
            connection.autocommit = True  
            cursor = connection.cursor()
            print(f"Connection established")
            break
        except psycopg2.OperationalError as e:
            print(f"Attempt {i} failed: {e}. Retrying...")
    
    
     # Creating the mnist_db database
    try:
        cursor.execute("CREATE DATABASE mnist_db;")
        print("Database 'mnist_db' created successfully.")
    except psycopg2.errors.DuplicateDatabase:
        print("Database already exists.")

# Close the connection with default database 
    cursor.close()
    connection.close()

# Load environment variables for database and model paths
DB_HOST = os.getenv("DB_HOST", "db")
DB_PORT = os.getenv("DB_PORT", "5432")
DB_USER = os.getenv("DB_USER", "postgres")
DB_PASSWORD = os.getenv("DB_PASSWORD", "")
DB_NAME = os.getenv("DB_NAME", "mnist_db")


# Connect to the new database
def connect_mdb():
    return psycopg2.connect(
        host=DB_HOST,
        port=DB_PORT,
        user=DB_USER,
        password=DB_PASSWORD,
        database=DB_NAME
    )



def init_db(conn):
    """Initialize the database by creating the necessary tables."""
    with conn.cursor() as cursor:
        try:
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS input_data (
                    id SERIAL PRIMARY KEY,
                    label INT NOT NULL,
                    image_data BYTEA NOT NULL
                );
            """)
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS predictions (
                    id SERIAL PRIMARY KEY,
                    prediction INT NOT NULL,
                    input_id INT REFERENCES input_data (id)
                );
            """)
            conn.commit()
            print("Tables initialized successfully.")
        except Exception as e:
            print(f"Error initializing database: {e}")
        raise

    cursor.close()
    conn.close()

#Initialize the database
conn = connect_mdb()
init_db(conn)

def save_image(label, image_array):
    """Save an image to the database."""
    conn = connect_mdb()
    cursor = conn.cursor()
    try:
        # Serialize the image to binary format
        image_bytes = BytesIO()
        Image.fromarray(image_array).save(image_bytes, format="PNG")
        image_binary = image_bytes.getvalue()

        # Insert into the database
        cursor.execute(
            "INSERT INTO input_data (label, image_data) VALUES (%s, %s) RETURNING id;",
            (label, image_binary),
        )
        conn.commit()
        inserted_id = cursor.fetchone()[0]
        print(f"Image saved with ID: {inserted_id}")
        return inserted_id
    except Exception as e:
        print(f"Error saving image to database: {e}")
    finally:
        cursor.close()
        conn.close()


def fetch_image(image_id):
    """Fetch an image and its label from the database."""
    conn = connect_mdb()
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT label, image_data FROM input_data WHERE id = %s;", (image_id,))
        record = cursor.fetchone()
        if record:
            label = record[0]
            image_binary = record[1]
            image = Image.open(BytesIO(image_binary))
            return label, image
        else:
            print("Image not found.")
            return None, None
    except Exception as e:
        print(f"Error fetching image from database: {e}")
    finally:
        cursor.close()
        conn.close()


def predict_image(image):
    """Make a prediction using the trained model."""
    try:
        # Load the model
        model = load_model(MODEL_PATH)

        # Preprocess the image
        image_resized = image.resize((28, 28)).convert("L")
        input_data = np.array(image_resized).reshape(1, 28, 28, 1).astype("float32") / 255.0

        # Make the prediction
        prediction = np.argmax(model.predict(input_data))
        return prediction
    except Exception as e:
        print(f"Error during prediction: {e}")
        raise


def save_prediction(prediction, input_id):
    """Save the prediction to the database."""
    conn = connect_mdb()
    cursor = conn.cursor()
    try:
        cursor.execute(
            "INSERT INTO predictions (prediction, input_id) VALUES (%s, %s);",
            (int(prediction), int(input_id)),
        )
        conn.commit()
        print(f"Prediction saved for input ID: {input_id}")
    except Exception as e:
        print(f"Error saving prediction: {e}")
    finally:
        cursor.close()
        conn.close()




		



