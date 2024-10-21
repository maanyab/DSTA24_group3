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
The initial error when trying to commit was to not have declared useremail and username. The following commands were used to do so:     
```  
git config --global user.email "you@example.com"
git config --global user.name "Your Name".
```

Another error was not being in the right directory when trying to commit. After correcting this issue, the file was added using the following commit and push commands:
        
```
git add code/
git commit -m "Existing code upload"
git push
```
        

## Task 4

Ubuntu comes with Python preinstalled.
Initially it was wrongly assumed that there was no python installed as the following command resulted in an error:
        ```python --version```
But it was later realised that the correct command was the following and that python does exist:
        ```python3 --version```

Python 3.12.4 which was installed as part of anaconda 24.9.2 was used for this project
A new conda environment was created to isolate dependencies for this project using the following command:
```
conda create --name DSTA1_env python=3.12.4
conda activate DSTA1_env
```
The conda environment was used instead of venv, to increase familiarity as future use cases are expected to go beyond using python packages to more data science - non python dependencies.

The necessary libraries (numpy, keras) required to run the code were installed using the following command:
```
conda install numpy keras
``` 

Running the code resulted in an error which arose from not having tensflow, which was rectified using:
```
conda install tensorflow
```

The following versions of the library were used - numpy version 1.26.4, keras 3.4.1 and tensorlow 2.17.0
```
conda list library_name
```

To recreate the same environment, an 'environment.yml' file was created which lists all the dependencies and their versions using the following command:
```
conda env export --no-builds > environment.yml
```


## Task 5
The input to the neural network is grayscale images of handwritten digits from the MNIST dataset and the output is a vector of 10 values, each represents the probability of the image being the particular digit.

The data is loaded via Keras' built in function ```keras.datasets.mnist.load_data()```. It is split into train (training images and their labels) and test (test images and their labels) They are then normalized (range [0,1]) and further categorized (binary class).

Dependencies: numpy was used for reshaping and processing the image data, keras is used to build, train and evaluate the neural network model and keras.layers to define the layers of the model (Conv2D, MaxPooling2D etc). 

The code is based on Convolutional Neural Network, it includes:
- Convolutional Layers (Conv2D) to extract features.
- MaxPooling Layers (MaxPooling2D) to reduce dimensionality.
- Flatten Layer
- Dropout Layer to prevent overfitting.
- Dense (Fully Connected) Layer to output probability distribution over the 10 classes.

This task requires recognizing patterns in images, and CNN's are ideal because they automatically learn features like edges, shapes and textures. It works well in extracting and combining features from pixel data to classify the images correctly.