
# Official TensorFlow image latest 
FROM tensorflow/tensorflow:latest

# Working directory inside container
WORKDIR /app

# Copy project files into container
COPY requirements.txt /app
COPY ./src /app/src
COPY get_commit.sh /app/get_commit.sh  

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

#To give docker permission to run the file
RUN chmod +x /app/get_commit.sh

# Run the commit check script
RUN /app/get_commit.sh

# Setting Environment variable for W&B API key using entrypoint 
COPY Entrypoint.sh /app/Entrypoint.sh
RUN chmod +x /app/Entrypoint.sh

# Volume to store trained model outside container
VOLUME /app/model

# Default to run main script
ENTRYPOINT ["/app/Entrypoint.sh"]
CMD ["python", "/app/src/main.py"]







