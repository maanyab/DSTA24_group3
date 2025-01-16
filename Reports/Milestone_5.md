# Milestone 4 Report 

*DSTA24 Fall Term 2024 - Group 3*

__*Authors*__
- *Vishal Alluri* 
- *Maanya Bagga*
- *Tommaso Fruci*


# Task 1

Steps undertaken to run Flask Application on the Machine -
    - I downloaded Virtual box from virtual box
    - Thereafter, installed Ubuntu 18.04.6 server image
    - Created a new virtual machine and ran it Ubuntu on it
    - Set up SSH



# Task 2 


**Error:** 
Couldn't connect to Docker daemon at http+docker://localunixsocket - is it running? If it's
at a non-standard location, specify the URL with the DOCKER_HOST environment variable.Encountered this issue even though the docker was active and running. The issue was my non root user was not a part of the docker group. 

**Solution:**
Added my user to the docker group 

```
sudo usermod -aG docker $USER
```

**Error:**
bind: address already in use- The error occured because the port 5432(the default port for PostgreSQL) was already in use on my machine.

**Solution:**
The existing PostgreSQL was stopped and the container was built again.

**Error**
Cannot import name Markup from Jinja2. Flask was trying to import Markup and escape from Jinja2 but they were not available in version 3.1.0 above.H However, all the packages were on their latest version. Inclduing marksafe up being included in the requirement text file.

Tried to find dependencies on MarkupSafe using ```pipdeptree```. Did not work. Then deactivated and removed the old environment and rebuilt the virtual environment.

**Error**
There was problem in 



 | **Package Name** | **Version** | **SHA256 Hash Digest** |
|------------------|-------------|------------------------|
|flask          |       |                  |
|pandas        |      | 
|Docker | |                
