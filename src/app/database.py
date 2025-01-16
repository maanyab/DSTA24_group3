import psycopg2
import os
from io import BytesIO
from PIL import Image


# Connect to postgre
DEFAULT_CONFIG={
	"host": "localhost",
	"port": "5432",
	"database": "postgres",
	"user": "postgres"
}




# Database configuration from environment variables 
DB_CONFIG={
	"host": os.getenv("DB_HOST", "localhost"),
	"port": os.getenv("DB_PORT", "5432"),
	"database": os.getenv("DB_NAME", "mnist_db"),
	"user": os.getenv("DB_USER", "postgres")
}

def create_database():
	try:
		conn=psycopg2.connect(
			host=DEFAULT_CONFIG["host"],
			port=DEFAULT_CONFIG["port"],
			database=DEFAULT_CONFIG["database"],
			user=DEFAULT_CONFIG["user"],
		)
		conn.autocommit=True
		cursor = conn.cursor()

		#Check if database exists
		cursor.execute(f"SELECT 1 FROM pg_database WHERE datname= %s;",(mnist_db,))
		exists=cursor.fetchone()

		if not exists:
			cursor.execute(sql.SQL("CREATE DATABASE {};").format(sql.Identifier(mnist_db)))
		else:
			print(f"Database '{mnist_db}' already exists.")

	except Exception as e:
		print(f"Error creating database: {e}")
	finally:
		cursor.close()
		conn.close()

# Connection to Postgre
def connect_db():
	try:
		conn = psycopg2.connect(
			host=DB_CONFIG["host"],
			port=DB_CONFIG["port"],
			database=DB_CONFIG["database"],
			user=DB_CONFIG["user"]
		)
		return conn
	except Exception as e:
		print(f"Error connecting to database: {e}")
		raise
def init_db():
	conn=connect_db()
	cursor=conn.cursor()
	try:
		cursor.execute("""
			CREATE TABLE IF NOT EXISTS input_data (
				id SERIAL PRIMARY KEY,
				label INT NOT NULL,
				image_data BYTEA NOT NULL
			);
		""")
		cursor.execute("""
			CREATE TABLE IF NOT EXISTS prediction (
				id SERIAL PRIMARY KEY,
				prediction INT NOT NULL,
				input_id INT REFERENCES input_data(id)
			);
		""")
		conn.commit()

		print("Database 'mnist_db' created successfully.")
	except Exception as e:
		print(f"Error initialising database : {e}")
	finally:
		cursor.close()
		conn.close()

def save_image(label, image_array):
	conn= connect_db()
	cursor=conn.cursor()
	try:
		#  serialise the image to binary format
		image_bytes=BytesIO()
		Image.fromarray(sample_image).save(image_bytes, format="PNG")
		image_binary = image_bytes.getvalue()

		cursor.execute(
			"INSERT INTO input_data (label, image_data) VALUES (%s, %s) RETURNING id;",
			(label, image_binary)
		)
		conn.commit()
		inserted_id=cursor.fetchone()[0]
		return inserted_id
	except Exception as e:
		print(f"Error saving image to database: {e}")
	finally:
		cursor.close()
		conn.close()

def fetch_image(image_id):
	conn=connect_db()
	cursor=conn.cursor()
	try:
		cursor.execute("SELECT label, image_data FROM input_data WHERE id = %s;", (image_id,))
		record=cursor.fetchone()
		if record:
			label=record[0]
			image_binary = record[1]
			image=Image.open(BytesIO(image_binary))
			return label, image
		else:
			print("Image not found.")
			return None, None
	except Exception as e:
		print(f"Error fetching image from database: {e}")
	finally:
		cursor.close()
		conn.close()



