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


If you stop and delete the Docker container the joke would not stay in the database beacuse the data is stored inside the container and gets deleted whit it. 
In order to be able to keep the data in that case we should use a Docker volume to save the database otuside the container.