"""
Title: Simple MNIST convnet
Description: A simple convnet that achieves ~99% test accuracy on MNIST.
"""

"""
## Setup
"""
from data_handling import prepare_data
from neuralnet_architecture import neuralnet_model
from train_eval import train_model, evaluate_model
from saving_FittedModel import save_fittedmodel, load_fittedmodel

#add compare_predictions if the user would like to import the compare models too
from predicting import make_prediction
                      

def main():
    # Load and preprocess data
    x_train, y_train, x_test, y_test = prepare_data()
    
    # Create the neural network model
    model = neuralnet_model(input_shape=(28, 28, 1),num_classes=10)
    
    # Train the model
    model = train_model(model, x_train, y_train)

    # Evaluate the model
    evaluate_model(model, x_test, y_test)
    
    # Save the fitted model locally 
    save_fittedmodel(model, filename="/app/model/fitted_model.keras")

    # Uploads the trained model
    #wandb.save()

    # Load the fitted model 
    loaded_model = load_fittedmodel(filename="/app/model/fitted_model.keras")
    
    # Make predictions 
    predictions = make_prediction(loaded_model, x_test)
    print("Fitted Model Predictions:", predictions[:5])

if __name__ == "__main__":
    main()