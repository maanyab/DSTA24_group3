"""
Title: Data Handling
Description: Functions to load and Preprocess MNIST Datasets
"""


import numpy as np
import keras
import wandb


def prepare_data(num_classes=10):
    """
    Loads and Preprocess the MNIST dataset to prepare it for 
    training and testing.
    """
    # Load the data and split it between train and test sets
    (x_train, y_train), (x_test, y_test) = keras.datasets.mnist.load_data()

    # Scale images to the [0, 1] range
    x_train = x_train.astype("float32") / 255
    x_test = x_test.astype("float32") / 255

    # Reshape images to include the channel dimension
    x_train = np.expand_dims(x_train, -1)
    x_test = np.expand_dims(x_test, -1)
    
    # Print dataset information
    print("x_train shape:", x_train.shape)
    print(x_train.shape[0], "train samples")
    print(x_test.shape[0], "test samples")
    
    # Convert class vectors to binary class matrices (one-hot encoding)
    y_train = keras.utils.to_categorical(y_train, num_classes)
    y_test = keras.utils.to_categorical(y_test, num_classes)

    #logging a few sample images to W&B
    wandb.log({"sample_images": [wandb.Image(x_train[i], caption=f"Label: {y_train[i]}") for i in range(5)]})
    
    return x_train, y_train, x_test, y_test