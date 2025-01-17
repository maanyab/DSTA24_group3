FROM python:3.10-slim

# Set working directory
WORKDIR /src

#Copy files from outside app to container's working directory
COPY ./src /src
COPY ./requirement.txt /src/requirement.txt

#Install Dependencies
RUN pip install --no-cache-dir -r /src/requirement.txt

#Expose the port
EXPOSE 5000

#Run the application
CMD ["bash", "-c", "python /src/train.py && gunicorn --workers=3 --bind=0.0.0.0:5000 app:app"]



