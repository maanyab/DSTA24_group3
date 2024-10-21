# Milestone 1 Report 


## Initial Setup
To begin with, I cloned the GitHub repository to my local repository by clicking the clone repository button on visual studio code. A prompt asking for the repository URL appeared, I pasted the URL found in HTTPS section after which the repository was cloned.

## Task 1: Overview of MNIST Datset

### Overview 
MNIST dataset is a database of handwritten digits. A handwritten digits database is a structured collection of images or samples of handwritten numerical digits (0-9). The purpose of such datasets is benchmarking, training machine learning datasets and for research and development. The MNIST dataset is composed of grayscale images of handwritten digits from 0 to 9. The images are pre-processed to ensure that they all have the same size and pixel intensity distribution. Each image in the dataset represents a single handwritten digit, and the task for machine learning models is to correctly classify the digit. This particular dataset tests a lot of classification techniques including linear classifiers, K-Nearest Neighbours, Boosted Stumps, Non-linear Classifiers, SVM, Neural Nets, Convolutional Nets.

### Type of Machine Learning problem
The MNIST dataset presents a classification problem, where the goal is to assign a label (digit from 0 to 9) to each image. The dataset consists of 10 classes, each representing a digit. The task for machine learning models is to learn patterns in the image data and accurately predict the label for each image.

### Characteristics of the Dataset
Size of the dataset: The MNIST dataset contains a total of 70,000 images:

60,000 training images: these are used to train the machine learning models.
10,000 testing images: these are used to evaluate the model’s performance after training.
Image format:

Each image is a 28x28 pixel grayscale image, which means that each image has 28 rows and 28 columns of pixel values.
The pixel values range from 0 to 255, where 0 represents black (background) and 255 represents white (foreground). The pixel intensities in between represent varying shades of gray.
Label format:

Each image in the dataset is associated with a label (also referred to as the target value). The label is a digit from 0 to 9 corresponding to the handwritten digit in the image.
The labels are stored as integers (0, 1, 2, ..., 9).

### Structure of the dataset
The dataset was divided into training and test datasets.
- The training set contains 60,000 images and their corresponding labels. This is the data that the machine learning model uses to learn the mapping between images and labels.
- The test set contains 10,000 images and their corresponding labels. This set is used to evaluate the model’s generalization ability.

The task associated with the MNIST dataset is to build a model that can accurately recognize handwritten digits. The model is trained on the 60,000 training images to learn patterns in the data, such as strokes, curves, and shapes that distinguish one digit from another. After training, the model is evaluated on the 10,000 test images to assess how well it can generalize to unseen data.

## Task 2: Code Base from Keras Repository

I tried to pull the base code using shell commands. This process took a bit more research. I found a couple of sources that provided the information required to carry this step out. Firstly, I tried with the code below -

```
git remote add keras-team/keras-io https://github.com/keras-team/keras-io.git
git fetch keras-team/keras-io
git checkout -b base-code keras-team/keras-io/examples/vision/mnist_convnet.py  
```
I got an error with this code as this code is used to create a branch from an existing branch, however, I was using a filepath. Then I tried to used Git sparse-checkout to pull only a specific file. Initially, I encountered errors but then I removed the remote repository ans tried again. I managed to pull just the file and add it as a separate folder in my local repo.

```
git remote add keras-io https://github.com/keras-team/keras-io.git
git sparse-checkout init --cone #To pull a subset of files from a large repository
git sparse-checkout set examples/vision/mnist_convnet.py
git pull keras-io master
git checkout keras-io/master -- examples/vision/mnist_convnet.py
```

## Task 3: Commiting the Relevant Python File to Git Repository

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

## Task 4: Running the MNIST CNN Code in Python

- I had visual studio code already installed on my laptop therefore, I didn't have to install Python.
I had already pulled the base code from git as mentioned before. However, I did have to install the libraries used in the code including Numpy and Keras using the 'pip install' command. 
- In the first instance the script wouldn't run as the packages weren't installed properly. There was a requirement to install TensorFlow as it is a dependency for Keras. I tried to install all the dependencies for this code base using the requirements.txt file, however, I received an error stating there was no such file or directory. The reason being that the file was not pulled from the remote directory. After pulling the file, I installed all the dependencies from the requirements file. Thereafter, after I ran "pip freeze" to check the dependencies and their versions which I saved in the requirements file in the root directory.
- I activated my virtual environment using the command below and named it virenv. It ran the  3.11.7 version of Python. The entire virtual environment does not need to be tracked thus I put it in git ignore file. 
```
python -m venv virenv
```
MacOS - The mnist_convnet code ran smoothly on Mac, no dependency issues were encountered.

### Alternative Method 

#### Installing Python on MacOS using Homebrew
Homebrew is a package manager for macOS that simplifies installing and managing software packages directly from the command line.

#### Step 1: Install Homebrew
- Open Terminal on MacOS
- Run the following command to install Homebrew:
```
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

I found the code snippet for installing Homebrew on the official Homebrew website. The command is designed to streamline the installation process of Homebrew. Specifically, the code executes a shell script hosted at
https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh on GitHub.

#### Step 2: Install Python
To install the latest version of Python we need to run this command in the Terminal: 
```
brew install python
```
Homebrew will download and install Python with any necessary dependencies.

#### Step 3: Verify the Installation 
Verify that Python has been succesfully installed by running this command: python3 --version
The output is: Python 3.13.0

#### Running the code
- Setting up the project directory:
    Created a project directory on my desktop titled "DS Toolkits and Architectures".

#### Problem 
I tried to run the code in my virtual environment but the virtual environment was using python 3.13 and the error i got was:
"ERROR: Could not find a version that satisfies the requirement tensorflow (from versions: none) ERROR: No matching distribution found for tensorflow"

#### Solution
To be able to run the code I had to create a virtual environment using Python 3.10, after having deactivated the old virtual environment.

**Creating a Virtual Environment:** Opened the terminal and navigated to the project directory using:
```
cd '/Users/tommaso/Desktop/File/DS Toolkits and Architectures'
```
Created a virtual environment named **myenv310** with the following command:
```
python3.10 -m venv myenv310
```
**Activating the virtual environment:** using
```
source myenv310/bin/activate
```
**Installing TensorFlow:** Installed TensorFlow in the activated virtual environment using:
```
pip install tensorflow-macos
```
It was necessary to ensure the virtual environment was using Python 3.10 to avoid compatibility issues.

**Running the code:** Ran the code using the command:
```
python mnist_convnet.py
```
The code successfully downloaded the MNIST dataset, built the neural network model, trained it, and evaluated its performance.
The evaluation yielded a **test accuracy** of approximately 99.14% and a test loss of 0.0256.

**Test Loss:** The test loss of 0.0256 indicates that the model made relatively few errors when predicting the test data, suggesting good performance and effective generalization to unseen data.

**Test Accuracy:** The test accuracy of 99.14% signifies that the model correctly classified about 99.14% of the test images, reflecting its effectiveness at recognizing and classifying handwritten digits.

#### Required Packages
In order to be able to run the Python script that uses libraries such as TensorFlow, NumPy and Matplotlib we need to install these packages using pip.
```
pip3 install tensorflow numpy matplotlib
```
#### Problem 1 
When running the code to install the libraries i got this ouput: "error: externally-managed-environment" After some research, I found out that this error indicates that my current Python environment is "externally managed" by Homebrew and it is not recommended to install packages directly using pip3 in this environment.

#### Solution 1
The problem can be overcome by creating a virtual environment that will allow us to install packages in an isolated environment without interfering with the Homebrew-managed Python.

- Create a virtual environment by running this code: python3 -m venv myenv
- Activate the virtual environment: source myenv/bin/activate
- Install the packages using pip: pip install tensorflow numpy matplotlib

#### Problem 2
When I tried to install the packages i got this output: "ERROR: Could not find a version that satisfies the requirement tensorflow (from versions: none) ERROR: No matching distribution found for tensorflow"
This means that pip could not find a comaptible version of TensorFlow for my Python version (Python 3.13)

#### Solution 2
To solve this problem we can create a virtual environment using a compatible Python version.
- Install Python 3.10 using Homebrew: brew install python@3.10
- Create a virtual environment using Python 3.10: python3.10 -m venv myenv
- Activate the virtual environment: source myenv/bin/activate
- Install the packages: pip install tensorflow numpy matplotlib
Now we have installed:
- Tensorflow: the core library for running our CNN
- NumPy: used for numerical operations and array handling
- Matplotlib: if we need to visualize data or results

## Task 5: Explanation of the MNIST CNN Code.
The code implements a convolutional neural network (CNN) using Keras and TensorFlow to classify handwritten digits from the MNIST dataset. A convolutional Neural network is a regularised type of feed forward neural network that learns features by itself. These type of neural network are preferred as they perform better with images, speech and audio signal input.The model at hand is trained to learn patterns in the images of digits and evaluate its performance on a test set.

```bash
python ../Code/minist_convnet.py    #The command to run the code file.
```

### Input and Output 

**Input**: The input to the neural network is a structural collection of grayscale images from the MNIST dataset, each of size 28x28 pixels. The images represent handwritten numerical digits ranging from 0 to 9. The dataset contains 60,000 training samples and 10,000 test samples of handwritten digits (0-9).

**Output**: The output is a probability distribution over 10 classes (digits 0-9), indicating the likelihood that the input image belongs to each class. The model used is sequential model as it is appropriate for plain stacking of layers. Since there are only single inputs and outputs in the model as well as layers sequential model can be used. The summary of the sequential model displayed different layer types and their respective output shape as well as parameter count. There are 7 layer types namely Conv2D, MaxPooling2D, Conv2D, MaxPooling2D_1, Flatten, Dropout, Dense. The model's predictions are typically evaluated using accuracy(0.02450996) and loss(0.9912299)metrics. There were 15 Epochs.

### Keras & TensorFlow

**Keras** is a high-level API of Tensorflow platform developed by Google and written in Python. It is modular and extensible, making it easy to build and train deep learning models. Keras acts as an interface for TensorFlow, allowing users to define and train neural networks more intuitively. Keras also allows full access to scalability and cross-platform capabilities of TensorFlow. The core data structure of Keras are layers and models.

**Tensorflow** library is a dependency of Keras as the latter is integrated into TensorFlow as tf.keras. Tensorflow is open source machine learning library devloped by google. Keras relies on Tensorflow as a backend. TensorFlow is an end-to-end platform for machine learning. It supports the following - numeric computation, GPU and distributed processing, Automatic differentiation, Model construction, training, and export. It operates on multidimentional arrays known as tensors

### Data Loading and Dependencies 
The MNIST dataset is **loaded** using Keras's built-in function 
```
keras.datasets.mnist.load_data()
```
This function downloads the dataset if it is not already available locally, splits it into training and testing sets, and normalizes the pixel values to be between 0 and 1 for better training performance.

The following **dependencies** are imported in the code:

- **TensorFlow**: the core library used to build and train the neural network model.
- **Keras modules**: these are used to construct the architecture of the CNN, defining layers such as convolutional, pooling, and dense (fully connected) layers.
- **NumPy**: a library for numerical operations, used for handling arrays and matrices in the data processing pipeline.

### Neural Network 

#### Architecture 
The architecture is typically a Convolutional Neural Network (CNN), which is particularly well-suited for image data. As mentioned above there were 7 layers in this model namely -
- **Convolutional layers (Conv2D)** - It is used for feature extraction. These layers extract features from the input images by applying filters to detect patterns such as edges and textures. Two Convolutional layers are used.
- **Pooling layers (MaxPooling2D)** - Used to downsample feature maps. These layers reduce the spatial dimensions of feature maps while retaining important information, which helps reduce computational complexity. Two Max Pooling 2D layers are used.
- **Flatten Layer** - Flatten layer is used to make the multidimensional input one-dimensional, commonly used in the transition from the convolution layer to the full connected layer. In other words, this layer converts the 2D feature maps into a 1D vector, preparing the data for the dense layer.
- **Dropout Layer** - Dropout is a powerful technique utilized in training Neural Networks to minimize the occurrence of overfitting. Primarily, it serves as a form of regularization, wherein during the training phase, certain neurons are randomly 'dropped out'. This process allows the model to generalize better and improve accuracy on unseen data.
- **Dense Layer**  -  The final layer of the model that outputs the probabilities for each class (digit 0-9). The primary advantage of dense layers is that they are able to capture complex patterns in data by allowing each neuron to interact with all the neurons in the previous layer. This makes dense layers well-suited for tasks such as image classification.

#### Reason to Employ Neural Network
A neural network is appropriate for this task due to the below mentioned reasons - 

**Complexity** - Handwritten digit classification is a complex pattern recognition problem that requires the ability to learn hierarchical features from the input images.

**Scalability** - CNNs are particularly effective for image processing tasks due to their ability to capture spatial relationships and patterns, making them suitable for recognizing digits in varying orientations and styles.

**Ability to learn** - Traditional machine learning methods may not perform as well on this type of problem, as they often rely on handcrafted features, while CNNs learn features automatically during training.

## Task 6 
Before beginning the project we made the gitignore as well as the ReadMe documentation and stored it in the Root Directory.
After completion of majority of our task, we updated the ReadMe file.




