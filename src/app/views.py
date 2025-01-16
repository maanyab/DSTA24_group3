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

@app.route('/predict',methods=['POST'])
def predict():
	try:
#Get the JSON payload from the POST request
		data =  request.get_jason()

		if 'image' not in data:
		    return jsonify({'error': 'No image provided in the request'}), 400

		# Decode the base64 image to a numpy array
		image_data = base64.b64decode(data['image'])
		image = Image.open(io.bytesIO(image_data)).convert('L')
		image_array = np.array(image)

		# Reshaping the image for neural network
		imgae_array = image_array.reshape(1,28,28,1).astype('float32')/255.0

		#Get Predictions
		predictions = prediction(model, image_array)

		#Save preditions to the Database
		save_image(prediction,image)

		#Return the prediction to the user
		return jsonify({'prediction': int(prediction)})

	except Exception as e:
	 return jsonify ({'error': str(e)}), 500
