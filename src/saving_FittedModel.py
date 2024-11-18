"""
Title: Saving and reloading the fitted model
Description: Functions to save and load the fitted Neural Network model
"""



import keras

def save_fittedmodel(model, filename="fitted_model.keras"):
    """
    Saves the trained Keras model as specified file name.

    Args:
        model: The trained Keras model to be saved.
        filename (str): The name of the file where the model will be saved (default: 'fitted_model.keras').
    """
    model.save(filename)




def load_fittedmodel(filename="fitted_model.keras"):    #The default file would be fitted_model.keras unless otherwise specifies
    """
    Loads the Fitted model that was saved using the above function.
    Args:
        filename (str): The name of the file from which the model will be loaded (in this case it is a default 'fitted_model.keras').
    Returns:
        The loaded Keras model.
    """
    model = keras.models.load_model(filename)
    return model