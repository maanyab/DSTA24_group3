import base64
import keras
import psycopg2
from PIL import Image
import numpy as np
from io import BytesIO
import os
from data_handling import prepare_data
from neuralnet_architecture import neuralnet_model
from train_save import train_model, save_model


# Training and saving the model that will be used for prediction 
# Load and preprocess data
x_train, y_train, x_test, y_test = prepare_data()
    
# Create the neural network model
model = neuralnet_model(input_shape=(28, 28, 1),num_classes=10)
    
# Train the model
model = train_model(model, x_train, y_train)
    
# Save the model 
save_model(model)

#Connect to postgre
connection = psycopg2.connect(
    host="db",
    port=5432,
    database="postgres",  
    user="postgres",
    password=""
)
connection.autocommit = True  
cursor = connection.cursor()

# Create database
try:
    cursor.execute("CREATE DATABASE mnist_db;")
    print("Database 'mnist_db' created successfully.")
except psycopg2.errors.DuplicateDatabase:
    print("Database already exists.")

# Close the connection with default database 
connection.close()

# Establishing connection with database
# Database connection details
DB_HOST = os.getenv("DB_HOST", "db")
DB_PORT = os.getenv("DB_PORT", "5432")
DB_USER = os.getenv("DB_USER", "postgres")
DB_PASSWORD = os.getenv("DB_PASSWORD", "")
DB_NAME = os.getenv("DB_NAME", "mnist_db")

# Connect to the new database
def connect_db():
    return psycopg2.connect(
        host=DB_HOST,
        port=DB_PORT,
        user=DB_USER,
        password=DB_PASSWORD,
        database=DB_NAME
    )

#Check if the table already exists otherwise create two tables
def init_db(conn):
    with conn.cursor() as cursor:
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

#Initialize the database
conn = connect_db()
init_db(conn)

#load a sample from the dataset
(x_train, y_train), _ = keras.datasets.mnist.load_data()
sample_image = x_train[0]  
sample_label = int(y_train[0])

#Serialize image to binary format and save image to database
def save_image(label, image_array):
    conn = connect_db()
    cursor = conn.cursor()
    try:
        # Serialize the image to binary format
        image_bytes = BytesIO()
        Image.fromarray(image_array).save(image_bytes, format='PNG')
        image_binary = image_bytes.getvalue()

        # Insert image data into the database
        cursor.execute("INSERT INTO input_data (label, image_data) VALUES (%s, %s) RETURNING id;", (label, image_binary))
        input_id = cursor.fetchone()[0]
        conn.commit()
        print(f"Image saved with ID: {input_id}")
        return input_id
    except Exception as e:
        print(f"Error saving image to database: {e}")
        conn.rollback()
        raise
    finally:
        cursor.close()
        conn.close()

#Fetch image back from back from the database and deserialize

# Fetch image from the database (only fetches the image binary)
def fetch_image(input_id):
    conn = connect_db()
    try:
        with conn.cursor() as cursor:
            # Fetch image binary from the database
            cursor.execute("SELECT image_data FROM input_data WHERE id = %s;", (input_id,))
            image_binary = cursor.fetchone()[0]
        return image_binary
    except Exception as e:
        print(f"Error fetching image from database: {e}")
        raise
    finally:
        conn.close()
        
def preprocess_image(image_base64):
    # Decode the base64-encoded image
    image_data = base64.b64decode(image_base64.split(',')[-1])
    image = Image.open(BytesIO(image_data)).convert('L')  # Convert to grayscale
    image_resized = image.resize((28, 28))  # Resize to 28x28 for MNIST format
    input_data = np.array(image_resized).reshape(1, 28, 28, 1).astype('float32') / 255.0  # Normalize
    return input_data


# load the model from the saved location

def predict_image(input_data, model_path="src/app/model/saved_model.keras"):
    try:
        # Load the model from the saved location
        model = keras.models.load_model(model_path)

        # Make the prediction
        prediction = np.argmax(model.predict(input_data))

        return prediction
    except Exception as e:
        print(f"Error making prediction: {e}")
        raise
    
# Save prediction result to the database
def save_prediction(prediction, input_id):
    conn = connect_db()
    try:
        with conn.cursor() as cursor:
            # Insert the prediction result into the database
            cursor.execute("INSERT INTO predictions (prediction, input_id) VALUES (%s, %s);", (int(prediction), int(input_id)))
            conn.commit()
            print(f"Prediction {prediction} saved for input_id {input_id}")
    except Exception as e:
        print(f"Error saving prediction to the database: {e}")
        conn.rollback()
        raise
    finally:
        conn.close()





