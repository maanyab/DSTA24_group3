# Milestone 1 Report

## Initial Setup
The first step was to setup a virtual machine, Oracle Virtual box was chosen. Initially it failed to install but the fix was to download Microsoft Visual C++ Redistributable from the official website. 

The desired OS for the VM- Ubuntu 24.04.1 was downloaded next. VM setup was now ready.

The next step was to install VScode and install git via terminal for version control (sudo apt install git). 'sudo' was used since it was understood that this would not harm any key dependencies. 

Anaconda version 24.9.2 was installed next. A '.sh' file was first downloaded from the official Anaconda website. To install, this file was run using the bash command.

Finally the group's github repository was cloned using the HTTPS link (found on the repos page) when prompted by VScode. A seperate branch for each member was created to account for their contribution.
   
## Task 1

The MNIST dataset is a collection of handwritten digits. It contains 70,000 images of digits 0-9, 60,000 being training images and 10,000 test. Each image is a 28x28 pixel grayscale image. Pixel values range between 0(white) to 255(black), intermediate values are shades of gray.

This is a classification problem as the goal is to assign each input to one of the 10 digit categories based on pixel values of the image. This dataset is generally used as a benchmark for image classification models like neural networks.

## Task 2
Since the project required only the one python code file, the raw file was directly downloaded from github instead of using git commands like checkout and stored in the code folder (minst_covnet.py).


## Task 3
The initial error when trying to commit was to not have declared useremail and username. The following commands were used to do so:       git config --global user.email "you@example.com"
  git config --global user.name "Your Name".

Another error was not being in the right directory when trying to commit. After correcting this issue, the file was added using the following commit and push commands:
    git add code/
    git commit -m "Existing code upload"
    git push


Using python 3.12.4 from anaconda
- New environment to isolate dependecies for this project conda create --name DSTA1_env python=3.12.4
- To activate: conda activate DSTA1_env

Initially I wrongly assumed that there was no python installed as python --version gave an error, but later realised that it does exist when python3 --version. But the coda environment was still used instead of venv, to increase familiarity as future use cases will probably go beyond only using python packages to more data science - non python dependencies.

Install libraries using conda install ....