""" 
Title: Saving and reloading the fitted model
Description: Functions to save and load the fitted Neural Network model
"""

import wandb

def save_fittedmodel(model, path="./model/saved_model.keras"):
    """
    Saves the trained model as specified file name locally as well as uploaded to wandb.

    Args:
        model: The trained model to be saved.
        filename (str): The name of the file the model will be saved as (default: './model/saved_model.keras').
    """
    # Save the model locally
    model.save(path)

    # Upload the model to W&B
    wandb.save(path)
