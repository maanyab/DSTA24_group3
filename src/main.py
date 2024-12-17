"""
Title: Simple MNIST convnet
Description: A simple convnet that achieves ~99% test accuracy on MNIST.
"""

"""
## Setup
"""
from data_handling import prepare_data
from neuralnet_architecture import neuralnet_model
from train_eval import train_model
from saving_FittedModel import save_fittedmodel

def main():
    # Load and preprocess data
    x_train, y_train, x_test, y_test = prepare_data()
    
    # Create the neural network model
    model = neuralnet_model(input_shape=(28, 28, 1),num_classes=10)
    
    # Train the model
    model = train_model(model, x_train, y_train)
    
    # Save the model 
    save_fittedmodel(model, filename="/app/model/saved_model.keras")

if __name__ == "__main__":
    main()