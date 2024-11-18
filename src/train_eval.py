"""
Title: Training and Evaluation 
Description: Functions to Train and Evaluate the Neural Network model
"""

def train_model(model, x_train, y_train, batch_size=128, epochs=15, validation_split=0.1):      #default input value for epochs, batch_size and validation_split
    """
    Trains the given model on the training data.

    Args:
        model: Compiled Keras model to be trained.
        x_train: Training input data.
        y_train: Training target data.
        epochs (int): Number of epochs to train the model (default: 15).
        validation_split (float): Fraction of training data to be used as validation (default: 0.1).

    Returns:
        a trained model
    """
    return model.fit(
        x_train,
        y_train,
        batch_size=batch_size,
        epochs=epochs,
        validation_split=validation_split
    )

#Evaluation of the fitted model

def evaluate_model(model, x_test, y_test):
    """
    Evaluates the trained model on the test data.

    Args:
        model: Trained Keras model to be evaluated.
        x_test: Test input data.
        y_test: Test target data.

    Returns:
        Loss and accuracy score of the model on the test data.
    """
    score = model.evaluate(x_test, y_test, verbose=0)
    print("Test loss:", score[0])
    print("Test accuracy:", score[1])
    return score