import numpy as np
from data_handling import prepare_data
from neuralnet_architecture import neuralnet_model
from train_save import train_model, save_model

def train():
	#load and preprocess data
	x_train, y_train, x_test, y_test = prepare_data()

	# create the neural network model
	model = neuralnet_model(input_shape=(28, 28, 1),num_classes=10)

	# train the model
	model = train_model(model, x_train, y_train)

	# Save the fitted model
	save_model(model)

if __name__=="__main__":
	train()


