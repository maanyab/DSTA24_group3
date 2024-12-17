from keras.datasets import mnist
import psycopg2
from PIL import Image
import numpy as np
from io import BytesIO

(x_train, y_train), _ = mnist.load_data()

#Sample img
sample_image = x_train[0]  
sample_label = int(y_train[0])

#Serialize image to binary format
image_bytes = BytesIO()
Image.fromarray(sample_image).save(image_bytes, format='PNG')
image_binary = image_bytes.getvalue()

#Connect to Postgres
connection = psycopg2.connect(
    host="localhost",
    port=5432,
    database="postgres",  
    user="postgres",
    password="postgres"
)
connection.autocommit = True  
cursor = connection.cursor()

# Create database
try:
    cursor.execute("CREATE DATABASE mnist_db;")
    print("Database 'mnist_db' created successfully.")
except psycopg2.errors.DuplicateDatabase:
    print("Database already exists.")

#Close connection with default db
connection.close()
#Connect to new db
connection = psycopg2.connect(
    host="localhost",
    port=5432,
    database="mnist_db",  
    user="postgres",
    password="postgres"
)
cursor = connection.cursor()

#Create table to store img
cursor.execute("""
    CREATE TABLE IF NOT EXISTS mnist_images (
        id SERIAL PRIMARY KEY,
        label INT NOT NULL,
        image_data BYTEA NOT NULL
    );
""")
connection.commit()

#Insert img into table
cursor.execute(
    "INSERT INTO mnist_images (label, image_data) VALUES (%s, %s) RETURNING id;",
    (sample_label, image_binary)
)
connection.commit()

inserted_id = cursor.fetchone()[0]
#Fetch img back from db
cursor.execute("SELECT label, image_data FROM mnist_images WHERE id = %s;", (inserted_id,))
fetched_label, fetched_image_binary = cursor.fetchone()

#Deserialize img
fetched_image = Image.open(BytesIO(fetched_image_binary))


fetched_image.show()  
print(f"Fetched Label: {fetched_label}")

cursor.close()
connection.close()
