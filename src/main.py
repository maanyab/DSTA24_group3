"""
Title: Simple MNIST convnet
Description: A simple convnet that achieves ~99% test accuracy on MNIST.
"""

"""
## Setup
"""
from data_handling import *
from neuralnet_architecture import *
from train_eval import *
from saving_FittedModel import *
from predicting import make_prediction                      #change to * if the user would like to import the compare module too            

def main():
    # Step 1: Load and preprocess data
    x_train, y_train, x_test, y_test = prepare_data()
    
    # Step 2: Create the neural network model
    model = neuralnet_model()
    
    # Step 3: Train the model
    model = train_model(model, x_train, y_train)

    #Step 4: Evaluate the model
    evaluate_model(model, x_test, y_test)
    
    # Step 5: Save the model (this is now handled in the train_model function)
    save_fittedmodel(model)
    
    # Step 6: Load the model (for demonstration purposes)
    loaded_model = load_fittedmodel("fitted_model.keras")
    
    # Step 7: Make predictions
    test_input = x_test  
    predictions = make_prediction(loaded_model, test_input)
    print("Fitted Model Predictions:", predictions[:5])