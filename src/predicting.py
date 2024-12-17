"""
Title: Making predictions from the fitted model
Description: Making predictions using the fitted model and comparing it with predictions from original model
"""

import wandb
import numpy as np

def make_prediction(model, x_test):
    """
    Makes predictions using the fitted model on the test data

    Args:
        model: The trained model.
        x_test: The test data

    Returns:
        The predictions made by the model.
        Text file in which the predictions made by the model are saved
    """
    predictions = np.argmax(model.predict(x_test), axis=1)

    return predictions

def upload_predictions(predictions, filename="predictions.txt"):
    """
    Save predictions to a file and upload to W&B.
    """
    # Save predictions to a text file
    np.savetxt(filename, predictions, fmt="%d")

    # Log the file to W&B
    wandb.save(filename)
