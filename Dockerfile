# Use an official Ubuntu runtime as a parent image
FROM python:3.12.5

# Set the working directory in the container
WORKDIR /app

# Copy all of the application's files into the container
COPY ./ /app
RUN rm -rf /app/db
RUN cat .env.exemplo > .env

# Update pip
RUN pip install --upgrade pip

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

RUN chmod -R +x ./

# Install system dependencies
RUN apt-get update && apt-get install -y wget unzip

# Install Chrome WebDriver
RUN wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
RUN apt-get install -y ./google-chrome-stable_current_amd64.deb
RUN rm google-chrome-stable_current_amd64.deb

# Clean package installer files
RUN apt-get clean