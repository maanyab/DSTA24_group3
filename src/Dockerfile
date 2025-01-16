FROM python:3.9-slim

# Set working directory
WORKDIR /app

#Copy files from outside app to container's working directory
COPY app.py /app/
COPY main.py /app/

#Copy the app folder into the container
COPY . /app

#Install Dependencies
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

#Expose the port
EXPOSE 5000

#Define Environment variable
ENV FLASK_APP=app.py

#Run the application
CMD ["flask", "run", "--host=0.0.0.0"]



