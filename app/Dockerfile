#Use official python image, 3.9-slim due to compatibility, stability and reducing the size of the base images
FROM python:3.9-slim

#Create a working directory 
WORKDIR /app

#Copy the src code directory to the app 
COPY src/ /app

#Install the needed python libraries
RUN pip install -r requirements.txt

#Exposing the port 
EXPOSE 5000

#Set environment variable for testing
ENV NAME World

#Run the application
CMD ["python","app.py"]