# Milestone 1 Report 


## Initial Setup
To begin with, I cloned the GitHub repository to my local repository by clicking the clone repository button on visual studio code. A prompt asking for the repository URL appeared, I pasted the URL found in HTTPS section after which the repository was cloned.

## Task 1

### Steps 

### About the dataset

- MNIST dataset is a database of handwritten digits. A handwritten digits database is a structured collection of images or samples of handwritten numerical digits (0-9). The purpose of such datasets is benchmarking, training machine learning datasets and for research and development.

- This particular dataset tests a lot of classification techniques including linear classifiers, K-Nearest Neighbours, Boosted Stumps, Non-linear Classifiers, SVM, Neural Nets, Convolutional Nets.


## Task 2

I tried to pull the base code using shell commands. This process took a bit more research. I found a couple of sources that provided the information required to carry this step out. Firstly, I tried with the code below -

```
 git remote add keras-team/keras-io https://github.com/keras-team/keras-io.git
git fetch keras-team/keras-io
git checkout -b base-code keras-team/keras-io/examples/vision/mnist_convnet.py  
```
I got an error with this code as this code is used to create a branch from an existing branch, however, I was using a filepath. Then I tried to used Git sparse-checkout to pull only a specific file. Initially, I encountered errors but then I removed the remote repository ans tried again. I managed to pull just the file and add it as a separate folder in my local repo.

```
git remote add keras-io https://github.com/keras-team/keras-io.git
git sparse-checkout init --cone
git sparse-checkout set examples/vision/mnist_convnet.py
git pull keras-io master
git checkout keras-io/master -- examples/vision/mnist_convnet.py
```

## Task 3: Commiting the relevant python file to Git repo

To ensure organisation and structure, I made two separate folders (for code and reports) simply using the options available on the left pane of the visual studio code(i.e. I did not use shell command initially).However, I encountered an error while trying to commit. Thereafter, I used the add command in the shell to add the report folder and the files in it. Lastly, I also changed the branch from main to the branch assigned to me.There were some authentication issues while pushing the changes as I had 2FA enabled. I had used HTTPS to clone the repository, therefore I had to generate personal access code token. After entering the generated code, I was able to push the changes I made to Git.

I added the python file that I pulled from remote repository to our repository with the below given code along with summary.
```
git add examples/vision/mnist_convnet.py
git commit -m "Summary: Added the code base from keras-io repository to DSTA24 Repo"
```
I had a preexisting folder for codes that I deleted and renamed the folder examples/vision to Code. Used the below code to change the name of the folder to Code
```
mv examples/vision Code
```
However, I was again confronted with an error as I was working with paths not included in my sparse checkout. Thus, was unable to commit the changes. As the sparse only recognised the old folder name. I added the new folder name (Code) to it.

```
git sparse-checkout set Code/
```


## Task 4
I had visual studio code already installed on my laptop therefore, I didn't have to install Python. However, I did have to install the libraries used in the code including Numpy and Keras using the 'pip install' command. Prior to installation, I activated my virtual environment which ran the  3.11.7 version of Python. 
In the first instance the  script wouldn't run bcz the packages weren't installed properly. There was a requirement to install TensorFlow along with Keras




## Task 5

Keras and Tensorflow - Tensorflow library is a dependency of Keras. Keras relies on Tensorflow as a backend
-The model it used was sequential 
- The dataset set was automatoicall downloaded and split using the code
```
    keras.datasets.mnist.load_data()
```
- There were 15 Epoch

## Task 6 




