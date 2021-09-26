# pull official base image
FROM python:3.7.10-slim-buster

# set work directory
WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt /usr/src/app/requirements.txt
RUN pip install -r requirements.txt
RUN pip uninstall -y findCPcore
RUN pip install -i https://test.pypi.org/simple/ findCPcore==0.1.3rc1

# copy project
COPY ./ /usr/src/app/
