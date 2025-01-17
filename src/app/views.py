import base64
import numpy as np
import tensorflow as tf
import io
from flask import Blueprint, request, jsonify
from app.model import load_model, prediction
from app.database import save_image
from PIL import Image

main_bp = Blueprint('main', __name__)

#load pre trained keras model
model =  load_model()

@main_bp.route('/predict',methods=['POST'])
def predict():
	try:
#Get the JSON payload from the POST request
		data =  request.get_json()

		if 'image' not in data:
			return jsonify({'error': 'No image provided in the request'}), 400

		# Decode the base64 image to a numpy array
		image_data = base64.b64decode(data['image'].split(',')[-1])
		image = Image.open(io.BytesIO(image_data)).convert('L')
		image =image.resize((28,28))
		image_array = np.array(image)

		# Reshaping the image for neural network
		image_array = image_array.reshape(1,28,28,1).astype('float32')/255.0

		#Get Predictions
		predictions = prediction(model, image_array)
		predicted_label = int(np.argmax(predictions))

		#Save preditions to the Database
		save_image(predictions, image_array)

		#Return the prediction to the user
		return jsonify({'prediction': int(predicted_label)})

	except Exception as e:
		return jsonify ({'error': str(e)}), 500
