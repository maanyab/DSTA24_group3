#

VM install
- Windows extra download
- Ubuntu download

Install VScode, installgit via sudo apt install git

Using python 3.12.4 from anaconda
- New environment to isolate dependecies for this project conda create --name DSTA1_env python=3.12.4
- To activate: conda activate DSTA1_env

Initially I wrongly assumed that there was no python installed as python --version gave an error, but later realised that it does exist when python3 --version. But the coda environment was still used instead of venv, to increase familiarity as future use cases will probably go beyond only using python packages to more data science - non python dependencies.