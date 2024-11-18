# Official TensorFlow image latest 
FROM tensorflow/tensorflow:latest

# Working directory inside container
WORKDIR /app

# Copy project files into container
COPY requirements.txt /app
COPY ./src /app/src

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Volume to store trained model outside container
VOLUME /app/model

# Default to run main script
CMD ["python", "/app/src/main.py"]
