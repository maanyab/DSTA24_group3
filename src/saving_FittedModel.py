""" 
Title: Saving and reloading the fitted model
Description: Functions to save and load the fitted Neural Network model
"""

import keras
import wandb

def save_fittedmodel(model, filename="/app/model/fitted_model.keras", wandb_filename = "trained_model.keras"):
    """
    Saves the trained model as specified file name locally as well as uploaded to wandb.

    Args:
        model: The trained model to be saved.
        filename (str): The name of the file the model will be saved as (default: '/app/model/fitted_model.keras').
    """
    model.save(filename)
    print(f"Model saved locally to {filename}")

    # Uploads the file to wandb 
    
    wandb.save(filename)  # Logs with the same container path
    wandb.log_artifact(filename, name=wandb_filename, type="model") #to ensure flexi
    print(f"Model logged to W&B with filename: {wandb_filename}")

def load_fittedmodel(filename="/app/model/fitted_model.keras"):
    """
    Loads the Fitted model that was saved using the above function.
    
    Args:
        filename (str): The name of the file from which the model will be loaded. 
                        The default file is '/app/model/fitted_model.keras'.
    
    Returns:
        The loaded Keras model.
    """
    model = keras.models.load_model(filename)
    return model
