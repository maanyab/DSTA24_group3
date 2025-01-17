import numpy as np
import keras

def prepare_data(num_classes=10):
	#load the data and split between train and test sets
	(x_train, y_train), (x_test,y_test) = keras.datasets.mnist.load_data()

	#Scale image to the [0,1] range
	x_train=x_train.astype("float32") / 255
	x_test =x_test.astype("float32") / 255

	#Reshape images to include the channel dimension
	x_train=np.expand_dims(x_train, -1)
	x_test=np.expand_dims(x_test, -1)

	# Convert class vectors to binary class matrices(one-hot encoding)
	y_train=keras.utils.to_categorical(y_train, num_classes)
	y_test=keras.utils.to_categorical(y_test, num_classes)
	return x_train, y_train, x_test, y_test

