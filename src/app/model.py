import tensorflow as tf

def load_model():
	# path to the model inside the Docker Container
	model_path = '/src/app/model/mnist_model.keras'
	model = tf.keras.models.load_model(model_path)
	return model

def prediction(model, image_array):

	# Get the model's prediction
	prediction = model.predict(image_array)
	return np.argmax(prediction)
