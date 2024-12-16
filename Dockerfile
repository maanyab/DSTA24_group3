
# Official TensorFlow image latest 
FROM tensorflow/tensorflow:2.10.0-py3

# Working directory inside container
WORKDIR /app

# Copy project files into container
COPY requirements.txt /app
COPY ./src /app/src
RUN pip install --no-cache-dir -r requirements.txt

# Set entry-point
CMD ["python", "src/db_prediction.py"]