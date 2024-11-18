"""
Title: Making predictions from the fitted model
Description: Making predictions using the fitted model and comparing it with predictions from original model
"""


import numpy as np

def make_prediction(model, x_test):
    """
    Makes predictions using the fitted model on the test data.

    Args:
        model: The trained Keras model.
        x_test: The test data

    Returns:
        The predictions made by the model.
    """
    predictions = model.predict(x_test)
    return predictions




def compare_predictions(model1, model2, x_test):
    """
    Compares predictions made by the saved models and original on the same test data.

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
        
