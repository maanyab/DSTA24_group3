# Milestone 5 Report 

*DSTA24 Fall Term 2024 - Group 3*

__*Authors*__
- *Vishal Alluri* 
- *Maanya Bagga*
- *Tommaso Fruci*


# Task 1

Steps that were undertaken to run Flask Application on the Virtual Machine 
    - I downloaded Virtual Box from Virtual Box
    - Thereafter, installed Ubuntu 18.04.6 server image
    - Created a new virtual machine and ran Ubuntu on it
    
**Problem**

While setting up to build flask application, I installed nginx. When testing if nginx was working as required, I had to open a webpage using an IP address. When I entered my public IP address the 'Welcome to nginx' webpage wouldn't load for me.

**Solution**

- Initially, I was using NAT mode, in which the VM can access the internet using host's network but external devices cannot directly access the VM, which is why the public IP wasn't working unless port forwarding was set up. I implemented port forwarding rules on my Virtual Machine mapping Host port 80 to Guest Port 80. However, that didn't seem to work. I also tried to see if the firewall might be blocking it but that didn't seem to be the issue. After a bit of research I realized that my provider has blocked port 80 on residential plans. However, thereafter, I used bridge network instead of NAT and that seemed to work.

# Task 2 


**Error:** 

Couldn't connect to Docker daemon at http+docker://localunixsocket - is it running? If it's
at a non-standard location, specify the URL with the DOCKER_HOST environment variable. Encountered this issue even though the docker was active and running. The issue was my non root user was not a part of the docker group. 

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

Cannot import name Markup from Jinja2. Flask was trying to import Markup and escape from Jinja2 but they were not available in version 3.1.0 above. However, all the packages were on their latest version. Including marksafe up in the requirement text file.

**Solution**

Tried to find dependencies on MarkupSafe using ```pipdeptree```. Did not work. Then deactivated and removed the old environment and rebuilt the virtual environment which seemed to work.

**Error**

Various issues with file permissions, some files were owned by root users, due to which sometimes I encountered errors while pulling from Github, moving files etc.

**Solution**

Changed file permission with 
```
chmod u+w path/to/file
```


**Error**
The biggest problem that we encountered was that of circular import. It took up majority of our time to sort out. Importing different funtions from different files made them interddependent resulting in numerous errors. Previously the code related to training of model as well as database initialisation was integrated with Flask app initialisation which led to numerous errors as everything was jumbled up and no one script was executed fully.

**Solution**
We used Python tutor to understand the order in which modules were being imported and python files being executed. Thereafter, we took out few modules  (those related to model training and database) outside the app initialisation .i.e. ran them before the app had even been initialised. 
Then we used application factory pattern which was suggested as the best way to fix circular imports in Flask apps. Rather than directly initialising the app, we created and used a function called 'create_app'.







 | **Package Name** | **Version** | **SHA256 Hash Digest** |
|------------------|-------------|------------------------|
|Flask          |  2.2.5     |SHA256 edee9b0a7ff26621bd5a8c10ff484ae28737a2410d99b0bb9a6850c7fb977aa0           |
|Pillow       |   9.5.0   | SHA256 bf548479d336726d7a0eceb6e767e179fbde37833ae42794602631a070d630f1|
|Guincorn | 20.1.0| SHA256 e0a968b5ba15f8a328fdfd7ab1fcb5af4470c28aaf7e55df02a99bc13138e6e8 |
|Psycopg2-binary| 2.9.9 | SHA256 7f01846810177d829c7692f1f5ada8096762d9172af1b1a28d4ab5b77c923c1c |


