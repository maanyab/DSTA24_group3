"""
Title: Builing  a Neural Network Model
Description: Function to build a neural network model 
"""

from keras import Sequential
from keras import layers

def neuralnet_model(input_shape, num_classes):
    """
    Create a Convolutional Neural Network (CNN) model.

        input_shape (tuple): Shape of the input data.
        num_classes (int): Number of output classes.

    It returns a Sequential model
    """
    model = Sequential(
        [
            layers.Input(shape=input_shape),
            layers.Conv2D(32, kernel_size=(3, 3), activation="relu"),
            layers.MaxPooling2D(pool_size=(2, 2)),
            layers.Conv2D(64, kernel_size=(3, 3), activation="relu"),
            layers.MaxPooling2D(pool_size=(2, 2)),
            layers.Flatten(),
            layers.Dropout(0.5),
            layers.Dense(num_classes, activation="softmax"),
        ]
    )
    return model