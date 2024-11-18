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

Our aim was to put particular definitions in separate files so that they can be used for various other programs as well. The manner in which we broke our code down will also make it easier to collaborate among our team members as in the future we can work on particular modules independently. We modulised our code keeping in mind whether or not two functions are usually used together, if so then they go in the same file. For instance, if we are loading the data, we would have to do some preprocessing. There both functionality are included in the same file. Lastly, the intent was to structure the code in the way that it has a number of modular functions, therefore instead of waiting for the whole code to run, we can test each funtion individually to ensure the code works smoothly (unit testing).

The table below shows code breakdown into modules -

| **File/Module Name**    |**Functionality** |
|------------------|------------------|
|data_handling.py               | This Module loads and preprocesses the data. If same data is to be used for different models this ensures consistency.|  
|neuralnet_architecture.py      | This module handles the building of neural network model. Putting it in a separate function ensures that we can make changes to model without affecting the training logic.|
|train_eval.py                  | contains the function for training and evaluating the trained model.
|saving_FittedModel.py          | saves the fitted model with .keras extensiona and loads the fitted model
|predicting.py                  | Module to makes predictions using the saved model
|main.py                        | Orchestrates the overall workflow by importing functions from the above modules. Serves as the single entry point to execute the pipeline (python main.py).


**Problems**

## Appendix 

The following table presents the python packages used along with their versions and SHA256 hash digest

| **Package Name** | **Version** | **SHA256 Hash Digest** |
|------------------|-------------|------------------------|
|                  |             |                        |
