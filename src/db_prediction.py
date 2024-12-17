import keras 
import psycopg2
from PIL import Image
import numpy as np
from io import BytesIO
import os
from data_handling import prepare_data
from neuralnet_architecture import neuralnet_model
from train_eval import train_model
from saving_FittedModel import save_fittedmodel


# Training and saving the model that will be used for prediction 
# Load and preprocess data
x_train, y_train, x_test, y_test = prepare_data()
    
# Create the neural network model
model = neuralnet_model(input_shape=(28, 28, 1),num_classes=10)
    
# Train the model
model = train_model(model, x_train, y_train)
    
# Save the model 
save_fittedmodel(model, filename="./model/saved_model.keras")

username = input("Enter your PostgreSQL username: ")
password = input("Enter your PostgreSQL password: ")

#Connect to postgre
connection = psycopg2.connect(
    host="localhost",
    port=5432,
    database="postgres",  
    user=username,
    password=password
)
connection.autocommit = True  
cursor = connection.cursor()

# Create database
try:
    cursor.execute("CREATE DATABASE milestone_3;")
    print("Database 'milestone_3' created successfully.")
except psycopg2.errors.DuplicateDatabase:
    print("Database already exists.")

# Close the connection with default database 
connection.close()

# Establishing connection with database
# Database connection details
DB_HOST = os.getenv("DB_HOST", "localhost")
DB_PORT = os.getenv("DB_PORT", "5432")
DB_USER = os.getenv("DB_USER", "user")
DB_PASSWORD = os.getenv("DB_PASSWORD", "password")
DB_NAME = os.getenv("DB_NAME", "milestone_3")

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

#Serialize image to binary format
image_bytes = BytesIO()
Image.fromarray(sample_image).save(image_bytes, format='PNG')
image_binary = image_bytes.getvalue()

# Save image to database
with conn.cursor() as cursor:
    cursor.execute("INSERT INTO input_data (label, image_data) VALUES (%s, %s) RETURNING id;", (sample_label, image_binary,))
    input_id = cursor.fetchone()[0]

#Fetch image back from back from the database and deserialize
with conn.cursor() as cursor:
        cursor.execute("SELECT image_data FROM input_data WHERE id = %s;", (input_id,))
        image_binary = cursor.fetchone()[0]
        fetched_image = Image.open(BytesIO(image_binary))

# Preprocess the image for prediction 
fetched_image_resized = fetched_image.resize((28, 28)).convert("L")
input_data = np.array(fetched_image_resized).reshape(1, 28, 28, 1).astype('float32') / 255.0

# load the model from the saved location
model = keras.models.load_model("./model/saved_model.keras")

# make predictions
prediction = np.argmax(model.predict(input_data))

# Save prediction result to the database
with conn.cursor() as cursor:
    cursor.execute("INSERT INTO predictions (prediction, input_id) VALUES (%s, %s);", (int(prediction), int(input_id)))
    conn.commit()
conn.close()












