
# Running the code

# Steps 

1. Setting up the project directory:

   - Created a project directory on my desktop titled "DS Toolkits and Architectures".

# Problem 1

I tried to run the code in my virtual environment but the virtual environment was using python 3.13 and the error i got was: 

"ERROR: Could not find a version that satisfies the requirement tensorflow (from versions: none)
ERROR: No matching distribution found for tensorflow"

# Solution 1

To be able to run the code I had to create a virtual environment using Python 3.10, after having deactivated the old virtual environment.

2. Creating a Virtual Environment:

   - Opened the terminal and navigated to the project directory using:
   
   cd '/Users/tommaso/Desktop/File/DS Toolkits and Architectures'
     
   - Created a virtual environment named `myenv310` with the following command:
   
     python3.10 -m venv myenv310

3. Activating the virtual environment:

   - Activated the new virtual environment using:

     source myenv310/bin/activate
 
4. Installing TensorFlow:

   - Installed TensorFlow in the activated virtual environment using:

     pip install tensorflow-macos

It was necessary to ensure the virtual environment was using Python 3.10 to avoid compatibility issues.

5. Running the code:
   - Ran the code using the command:

     python mnist_convnet.py

   - The code successfully downloaded the MNIST dataset, built the neural network model, trained it, and evaluated its performance. 

The evaluation yielded a test accuracy of approximately 99.14% and a test loss of 0.0256.

- Test Loss: The test loss of 0.0256 indicates that the model made relatively few errors when predicting the test data, suggesting good performance and effective generalization to unseen data.

- Test Accuracy: The test accuracy of 99.14% signifies that the model correctly classified about 99.14% of the test images, reflecting its effectiveness at recognizing and classifying handwritten digits.



