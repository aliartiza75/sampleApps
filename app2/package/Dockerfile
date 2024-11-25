# This version of sw-base has kudu package installed in it
FROM python:3.14.0a2-alpine3.19


LABEL "MAINTAINER"="aliartiza75@yahoo.com"
LABEL "DESCRIPTIONS"="Dockerfile for app2"

# app directory for application containing code files
WORKDIR /usr/src/app2

# copy just the requirements.txt first to leverage Docker cache
COPY requirements.txt ./

RUN pip3 install -r requirements.txt
# copying code files and folders to worker directory

COPY . .

CMD flask run --host=$FLASK_HOST_IP --port=$((FLASK_HOST_PORT))