"""
Title: Making predictions from the fitted model
Description: Making predictions using the fitted model and comparing it with predictions from original model
"""

import wandb
import numpy as np

def make_prediction(model, x_test):
    """
    Makes predictions using the fitted model on the test data and saves it to wandb as a file

    Args:
        model: The trained model.
        x_test: The test data

    Returns:
        The predictions made by the model.
        Text file in which the predictions made by the model are saved
    """
    predictions = model.predict(x_test)
    # save predictions in a file before uploading 
    np.savetxt("/app/predictions.txt", predictions)

    #uploading predictions to wandb
    wandb.save("/app/predictions.txt")

    return predictions



def compare_predictions(model1, model2, x_test):
    """
    Compares predictions made by the saved model and original on the same test data.

    Args:
        model1: The first model to compare.
        model2: The second model to compare.
        x_test: The test data used for predictions.
    
    Returns:
        bool: True if the predictions from both models are close (within an acceptable tolerance), False otherwise.
    """
    try:
        np.testing.assert_allclose(
            model1.predict(x_test), 
            model2.predict(x_test)
        )
        return True
    except AssertionError:
        print("Predictions from the two models differ.")
        return False
    

    


