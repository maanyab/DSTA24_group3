from keras import Sequential
from keras import layers

def neuralnet_model(input_shape, num_classes):
	model = Sequential(
	     [
		layers.Input(shape=input_shape),
		layers.Conv2D(32, kernel_size=(3,3), activation="relu"),
		layers.MaxPooling2D(pool_size=(2,2)),
		layers.Conv2D(64, kernel_size=(5,5), activation="relu"),
		layers.MaxPooling2D(pool_size=(2,2)),
		layers.Flatten(),
		layers.Dropout(0.5),
		layers.Dense(num_classes, activation="softmax"),
	     ]
	)
	return model

