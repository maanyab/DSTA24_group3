# Installing required packages to run the code
In order to be able to run the Python script that uses libraries such as TensorFlow, NumPy and Matplotlib we need to install these packages using pip.

Run this code: pip3 install tensorflow numpy matplotlib

# Problem 1
When running the code to install the libraries i got this ouput: "error: externally-managed-environment"
After some research, I found out that this error indicates that my current Python environment is "externally managed" by Homebrew and it is not recommended to install packages directly using pip3 in this environment.

# Solution 1
The problem can be overcome by creating a virtual environment that will allow us to install packages in an isolated environment without interfering with the Homebrew-managed Python.

Create a virtual environment by running this code: python3 -m venv myenv
Activate the virtual environment: source myenv/bin/activate
Install the packages using pip: pip install tensorflow numpy matplotlib

# Problem 2
When I tried to install the packages i got this output: 
"ERROR: Could not find a version that satisfies the requirement tensorflow (from versions: none)
 ERROR: No matching distribution found for tensorflow"

 This means that pip could not find a comaptible version of TensorFlow for my Python version (Python 3.13)

# Solution 2
To solve this problem we can create a virtual environment using a compatible Python version.

Install Python 3.10 using Homebrew: brew install python@3.10
Create a virtual environment using Python 3.10: python3.10 -m venv myenv
Activate the virtual environment: source myenv/bin/activate
Install the packages: pip install tensorflow numpy matplotlib

Now we have installed:
- Tensorflow: the core library for running our CNN
- NumPy: used for numerical operations and array handling
- Matplotlib: if we need to visualize data or results