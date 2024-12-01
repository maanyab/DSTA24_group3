# Task 1

The services used for the application in the provided link are "web" and "redis" which are defined in the file "compose.yaml".

"web" is used to run a website using Flask (python library used o create web pages). The code for the service is in the file "app.py" and it is built using a Dockerfile.
"redis" stores data temporarily in the computer's memory (lightweight-in memory database). In this case it used to count how many times the website created has been visited. Docker sets up Redis automatically using an official image called "redis:alpine".

Docker Compose creates a private network for all the services defined in the file "compose.yaml" and each service has a defined name within this network. Instead of using IP addresses, inside the private network the "web" service connects to "redis" using its service name ("redis"). 
In the "app.py" file it is used the "redis-py" library to connect through the following code:

cache = redis.Redis(host='redis', port=6379)

The host is the service name, and Docker translates it to the internal address of the Redis container. It isn't necessary to know the IP address of the Redis container because Docker connects automatically the "web" service to the correct container.

The "web" service listens on port 5000 inside its container. Then the "compose.yaml" file maps it to port 8000 on the host machine.
The "redis" service listens on port 6379 (default) inside its container but it is accesible only within Docker's internal network and it is not exposed to the host machine.

The host machine communicates with the application inside the Docker container through port mapping.
When the host machine visit "http://localhost:8000" it sends a request to port 8000 and Docker forwards this request to port 5000 inside the container where the application is running. 

The "redis" service is not directly accessible from the host machine because its port is not exposed, not mapped to the host machine.
For the "web" service port 8000 on the host machine is exposed, it is mapped to port 5000 inside the container.

localhost is an hostname that always points to the host machine itself using the loopback address 127.0.0.1. Using localhost the host machine sends requests back to itself and does not go out to a network.
This is useful for web applications because it allows developers to test and debug without needing to host them on a live server and anything running on localhost is accesible only from the host machine itself so it is also secure and private.
