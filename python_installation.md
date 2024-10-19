# Installing Python on macOS using Homebrew

# Step 1: Install Homebrew
Homebrew is a package manager for macOS that simplifies installing and managing software packages directly from the command line.

1. Open Terminal on MacOS
2. Run the following command to install Homebrew: 
   /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"


I found the code snippet for installing Homebrew on the official Homebrew website. The command is designed to streamline the installation process of Homebrew. Specifically, the code executes a shell script hosted at https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh on GitHub.

# Step 2: Install Python
To install the latest version of Python we need to run this command in the Terminal: brew install python
Homebrew will download and install Python with any necessary dependencies.

# Step 3: Verify the installation
Verify that Python has been succesfully installed by running this command: python3 --version
The output we see is: Python 3.13.0