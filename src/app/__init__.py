from flask import Flask
import keras
from train import init_db

def create_app():

	app = Flask(__name__)

	#Load the model once and store in app context
	app.model = keras.models.load_model('src/app/model/mnist_model.keras')

	# Initialise the database
	with app.app_context():
		init_db()

	from app.views import predict
	app.add_url_rule('/predict', view_func=predict, methods=['POST'])

	return app
