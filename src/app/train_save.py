 # Training  and saving the model

def train_model(model, x_train, y_train, batch_size, epochs, validation_split=0.1):
	model.compile(loss = "categorical_crossentropy", optimiser="adam", metrics=["accuracy"]
	model.fit(x_train, y_train, batch_size=128, epochs=15, validation_split=0.1)
	return model

def save_model(model):
	model.save('models/mnist_model.keras')
