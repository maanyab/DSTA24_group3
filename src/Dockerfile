FROM python:3.9-slim

# Set working directory
WORKDIR/app

#Install Dependencies
COPY requirements.txt
RUN pip install --no cache-dir -r requirements.txt

#copy application code 
COPY ..

#Expose the port
EXPOSE 5000

#Run the application
CMD["python","app.py"]



