"""
Title: Simple MNIST convnet
Description: A simple convnet that achieves ~99% test accuracy on MNIST.
"""

"""
## Setup
"""
import numpy as np
from data_handling import prepare_data
from neuralnet_architecture import neuralnet_model
from train_eval import train_model
from saving_FittedModel import save_fittedmodel
from predicting import make_prediction, upload_predictions
 

def main():
    # Load and preprocess data
    x_train, y_train, x_test, y_test = prepare_data()
    
    # Create the neural network model
    model = neuralnet_model(input_shape=(28, 28, 1),num_classes=10)
    
    # Train the model
    model = train_model(model, x_train, y_train, x_test, y_test)

    # Save the fitted model locally 
    save_fittedmodel(model)

    # Make predictions
    predictions = make_prediction(model, x_test)

    # Log confusion matrix
    #log_confusion_matrix(np.argmax(y_test, axis=1), predictions)

    # Upload predictions
    upload_predictions(predictions)

if __name__ == "__main__":
    main()

