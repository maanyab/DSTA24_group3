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
from predicting import make_prediction                    #add compare_predictions if the user would like to import the compare module too            

def main():
    # Step 1: Load and preprocess data
    x_train, y_train, x_test, y_test = prepare_data()
    
    # Step 2: Create the neural network model
    model = neuralnet_model(input_shape=(28, 28, 1),num_classes=10)
    
    # Step 3: Train the model
    model = train_model(model, x_train, y_train)

    #Step 4: Evaluate the model
    evaluate_model(model, x_test, y_test)
    
    # Step 5: Save the model (this is now handled in the train_model function)
    save_fittedmodel(model)
    
    # Step 6: Load the model (for demonstration purposes)
    loaded_model = load_fittedmodel("fitted_model.keras")
    
    # Step 7: Make predictions 
    predictions = make_prediction(loaded_model, x_test)
    print("Fitted Model Predictions:", predictions[:5])

if __name__ == "__main__":
    main()