# Milestone 3 Report 

*DSTA24 Fall Term 2024 - Group 3*

__*Authors*__
- *Vishal Alluri* 
- *Maanya Bagga*
- *Tommaso Fruci*


## Task 1
The services used for the application in the provided link are "web" and "redis" which are defined in the file "compose.yaml".

"web" is used to run a website using Flask (python library used o create web pages). The code for the service is in the file "app.py" and it is built using a Dockerfile. "redis" stores data temporarily in the computer's memory (lightweight-in memory database). In this case it used to count how many times the website created has been visited. Docker sets up Redis automatically using an official image called "redis:alpine".

Docker Compose creates a private network for all the services defined in the file "compose.yaml" and each service has a defined name within this network. Instead of using IP addresses, inside the private network the "web" service connects to "redis" using its service name ("redis"). In the "app.py" file it is used the "redis-py" library to connect through the following code:

cache = redis.Redis(host='redis', port=6379)

The host is the service name, and Docker translates it to the internal address of the Redis container. It isn't necessary to know the IP address of the Redis container because Docker connects automatically the "web" service to the correct container.

The "web" service listens on port 5000 inside its container. Then the "compose.yaml" file maps it to port 8000 on the host machine. The "redis" service listens on port 6379 (default) inside its container but it is accesible only within Docker's internal network and it is not exposed to the host machine.

The host machine communicates with the application inside the Docker container through port mapping. When the host machine visit "http://localhost:8000" it sends a request to port 8000 and Docker forwards this request to port 5000 inside the container where the application is running.

The "redis" service is not directly accessible from the host machine because its port is not exposed, not mapped to the host machine. For the "web" service port 8000 on the host machine is exposed, it is mapped to port 5000 inside the container.

localhost is an hostname that always points to the host machine itself using the loopback address 127.0.0.1. Using localhost the host machine sends requests back to itself and does not go out to a network. This is useful for web applications because it allows developers to test and debug without needing to host them on a live server and anything running on localhost is accesible only from the host machine itself so it is also secure and private.

## Task 2
# Task 2

PostgreSQL is a relational database management system that stores data in tables and uses SQL to interact with the data.
It is SQL because it uses a table-based system, organizing the data in a structured way (rows and columns). To modify the data we can use SQL commands.

### Problem
I tried to install `psycopg2`, but it failed because my system didn’t have the `pg_config` tool, which is required to build the library from source.

I installed `psycopg2-binary` instead, which is a pre-compiled version that doesn’t need `pg_config`, using the command:  
```bash
pip install psycopg2-binary
```

### Connecting PostgreSQL to pgAdmin

#### 1. Problem: unable to connect to PostgreSQL in pgAdmin
Initially, I couldn’t connect to my PostgreSQL server using `localhost` as the host in pgAdmin. I kept encountering the error:

> "Unable to connect to server: connection failed: connection to server at `127.0.0.1`, port `5432` failed: Connection refused."

I realized that I needed to use the IP address of the PostgreSQL container.

1. I found the IP address of my PostgreSQL container by running:
   ```bash
   docker inspect postgres_server | grep IPAddress
   ```
   This gave me an IP address `172.17.0.2`.

2. In pgAdmin, I used this IP address instead of `localhost` when setting up the connection:
   - Host: `172.17.0.2`
   - Port: `5432`
   - Username: `postgres`
   - Password: `dstag3`

Once I saved the changes, pgAdmin successfully connected to the PostgreSQL server.


#### 2. Problem: Missing `system_stats` extension
When accessing the database, I encountered a message saying:

> "The `system_stats` extension is not installed."

1. I connected to the database using `psql`:
   ```bash
   psql -h localhost -U postgres -p 5432
   ```

2. I switched to the `ms3_jokes` database:
   ```sql
   \c ms3_jokes
   ```

3. I installed the `system_stats` extension:
   ```sql
   CREATE EXTENSION system_stats;
   ```

4. I refreshed the database in pgAdmin, and everything worked as expected.

If you stop and delete the Docker container the joke would not stay in the database beacuse the data is stored inside the container and gets deleted with it. 
In order to be able to keep the data in that case we should use a Docker volume to save the database outside the container.

## Task 3

How to represent/transform image data to save it to a relational database?
Convert images to a binary format.
- Load image from keras, this is loaded as a numpy array.
- Convert it into png using Pillow (```Image.fromarray()```).
- Now serialize png to binary using BytesIO (image_binary: BYTEA data type for Postgres compatability).


1. Dataset structure:
Images: Grayscale images of size 28x28 pixels stored as NumPy arrays. Pixel values fall in the range of 0-255.
Labels: Numbers (0-9) representing the digit in the image.

2. Relational table design:
Table Name: mnist_images

    | **Attribute** | **Data Type** | **Description**                              |
    |---------------|---------------|----------------------------------------------|
    | `id`          | `SERIAL`      | Unique ID for each image.                   |
    | `label`       | `INTEGER`     | The digit label (0-9).                      |
    | `image_data`  | `BYTEA`       | Binary data for storing the image.          |


3. Additional attributes:
- A column classifying numbers as odd or even; prime or composite (VARCHAR).
- Pixel intensity (average) could possibly help in identifying specific characteristics.

## Task 4

The compose file was set to define two services the PostgreSQL database and Python web application. However, since latter was 
dependent on the former, we had to include conditions so that it doesn't run before the database. 
There are three types of conditions -
**service_started:**
**service_healthy:**
**service_completed_successfully:**




Since I was running into memory problem, I tried to build docker container using a smaller sized base image.
Instead of using the latest version of the base image, I used 2.10. Although it is smaller (CPU-only version), still stable and not too heavy to run on my machine.

```
FROM tensorflow/tensorflow:2.10.0-py3
```

Using service_healthy
when restart is set to true Compose restarts this service after it updates the dependency service.

condition: Sets the condition under which dependency is considered satisfied

service_started: An equivalent of the short syntax described above
service_healthy: Specifies that a dependency is expected to be "healthy" (as indicated by healthcheck) before starting a dependent service.
service_completed_successfully: Specifies that a dependency is expected to run to successful completion before starting a dependent service.

Compose waits for healthchecks to pass on dependencies marked with service_healthy. In the following example, db is expected to be "healthy" before web is created.

Avoided using fixed container names to avoid error incase of scaling in the future.


+---------------+            +------------------+
|   input_data  |            |   predictions    |
+---------------+            +------------------+
| id (PK)       | <----------| id (PK)          |
| image (BYTEA) |            | prediction (INT) |
+---------------+            | input_id (FK)    |
                             +------------------+
