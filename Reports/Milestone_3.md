# Milestone 3 Report 

*DSTA24 Fall Term 2024 - Group 3*

__*Authors*__
- *Vishal Alluri* 
- *Maanya Bagga*
- *Tommaso Fruci*


## Task 1

## Task 2

## Task 3

## Task 4

The compose file was set to define two services the PostgreSQL database and Python application 

Instead of using the latest version of the base image, I used 2.10 as it is smaller (CPU-only version) but still stable and not too heavy to run on my machine

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
