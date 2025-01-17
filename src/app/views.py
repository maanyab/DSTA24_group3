import os
import numpy as np
from flask import request, jsonify
import keras
from train import save_image, save_prediction, init_db, preprocess_image  
from app import app

# Load the pre-trained model
model = keras.models.load_model("src/app/mnist_model.keras")

# Endpoint for making predictions
@app.route('/predict', methods=['POST'])
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

# Initialize database tables (before the first request)
@app.before_first_request
def init_db_tables():
    init_db()  

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

	
