# Milestone 2 Report 

*DSTA24 Fall Term 2024 - Group 3*

__*Authors*__
- *Vishal Alluri* 
- *Maanya Bagga*
- *Tommaso Fruci*


## Task 3 

Installed the required packages to run the code file. However, encountered the "Timeout Error" while installing the Tensorflow package. 
Updated pip install as suggested by the output using the command below

``` pip install --upgrade pip```

After upgrading, installed TensorFlow again but did still encountered the same error(I did this while in the library).
Tried it again at my home network and this time it worked.

**Load and Train the model**
The existing code already loads the data and trains the model.

**Save a fitted model to saved model type**
As the version of tensorflow was 2.16, therefore I saved the file with saved model type. However, I encountered a ValueError stating that the save_format is deprecated in Keras 3. Thereafter I removed this argument as suggested in the error message and proceeded with passing the file name with '.keras' extension.
While trying to save the model, I ran into Attribute error as I accidently saved model history instead of model itself.

**load a saved model type**
Encountered a ValueError while loading the file as SavedModel format is not supported by ```load_model()``` in Keras 3. Added '.keras' extension to the file name

**Perform predictions using keras**
While researching I read that it is good practice to check if predictions remain the same after we save and reload the model. Hence, included a code that verifies the same. The ```np.testing.assert_allclose``` raises an assertion error if the predictions are too dissimilar. No assertion error was encountered and first five predictions using the fitted model were printed. 

As the file would be too large for Git Repository before commiting it was added to .gitignore


## Task 4 








## Appendix 

The following table presents the python packages used along with their versions and SHA256 hash digest

| **Package Name** | **Version** | **SHA256 Hash Digest** |
|------------------|-------------|------------------------|
|                  |             |                        |
