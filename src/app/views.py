import os
import numpy as np
from flask import request, jsonify, current_app
from train import save_image, save_prediction, preprocess_image



# Endpoint for making predictions
def predict():
    try:
        # Get the image data from the POST request (base64 format)
        data = request.get_json()
        if 'image' not in data:
            return jsonify({'error': 'No image provided'}), 400

        # Preprocess the image using the utility function
        input_data = preprocess_image(data['image'])

        # Make a prediction using the model
        prediction = np.argmax(model.predict(input_data))

        # Save image to database
        input_id = save_image(label=None, image_array=input_data)

        # Save prediction to the database
        save_prediction(prediction, input_id)

        # Return prediction result to the client
        return jsonify({'prediction': int(prediction)}), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500

