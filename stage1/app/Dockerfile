FROM ubuntu:latest

# Install and updade ubuntu tool
RUN apt-get update && apt-get install -y curl

# RUN apt-get install -y python-pip python-dev

RUN apt-get update \
    && apt-get install -y python3-pip python3-dev \
    && cd /usr/local/bin \
    && ln -s /usr/bin/python3 python \
    && pip3 install --upgrade pip
	
RUN pip3 install --upgrade setuptools

# RUN pip3 install pycurl

# The working directory where the app is copied
WORKDIR /App

# Copy the app's source files
COPY ./requirements.txt /App/requirements.txt
COPY . .

# install the dependencies in python environment
RUN pip3 install -r requirements.txt

# The port to serve the app
EXPOSE 5000 6379

# Start the app at the launch
CMD ["python3", "app_server.py"]

# Build the app in the VM
# sudo docker build -t flask-app:latest .
# Run the app
# sudo docker run -d -p 5000:5000 --name flaskapp flask-app:latest 