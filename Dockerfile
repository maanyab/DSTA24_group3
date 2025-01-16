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

#Define Environment variable
ENV FLASK_APP=app.py

#Run the application
CMD ["bash", "-c", "python /src/train.py && flask run --host=0.0.0.0 --port=5000"]



