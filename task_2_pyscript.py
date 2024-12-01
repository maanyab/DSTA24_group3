import psycopg2

# Connect to the PostgreSQL server
connection = psycopg2.connect(
    host="localhost",      
    port=5432,             # default PostgreSQL port
    database="postgres",   
    user="postgres",       # username
    password="dstag3"      # password 
)
cursor = connection.cursor()

# Enable autocommit mode to allow create database
connection.autocommit = True
cursor = connection.cursor()

# Create new database called "ms3_jokes"
cursor.execute("CREATE DATABASE ms3_jokes;")
connection.commit()

# Reconnect to the new database
connection.close()
connection = psycopg2.connect(
    host="localhost",
    port=5432,
    database="ms3_jokes",  # new database
    user="postgres",
    password="dstag3"
)
cursor = connection.cursor()

# Create "jokes" table
cursor.execute("""
    CREATE TABLE jokes (
        ID SERIAL PRIMARY KEY,  -- Automatically incrementing ID
        JOKE TEXT NOT NULL      -- Text column for storing jokes
    );
""")
connection.commit()

# Insert one joke into the table
joke = "What's Thanos' favourite app? Snapchat."
cursor.execute("INSERT INTO jokes (JOKE) VALUES (%s);", (joke,))
connection.commit()

# Fetch the joke and print it
cursor.execute("SELECT JOKE FROM jokes WHERE ID = 1;")
fetched_joke = cursor.fetchone()[0]
print("My favorite joke is:", fetched_joke)

# Close the connection
cursor.close()
connection.close()
