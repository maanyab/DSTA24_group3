
# Official TensorFlow image latest 
FROM tensorflow/tensorflow:latest

# Working directory inside container
WORKDIR /app

# Copy project files into container
COPY requirements.txt /app
COPY ./src /app/src
RUN pip install --no-cache-dir -r requirements.txt

# Setting Environment variable for W&B API key using entrypoint 
COPY Entrypoint.sh /app/Entrypoint.sh
RUN chmod +x /app/Entrypoint.sh

# Volume to store trained model outside container
VOLUME /app/model

# Default to run main script
ENTRYPOINT ["/bin/bash","/app/Entrypoint.sh"]
CMD ["python", "/app/src/main.py"]
