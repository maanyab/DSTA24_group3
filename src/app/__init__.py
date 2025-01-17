from flask import Flask
import keras
from app.views import predict

def create_app():

	app = Flask(__name__)

	#Load the model once and store in app context
	app.model = keras.models.load_model('src/app/model/mnist_model.keras')

	# Register Routes
	app.add_url_rule('/predict', view_func=predict, methods=['POST'])

	return app
