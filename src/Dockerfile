# pull official base image
FROM python:3.10

# set work directory
WORKDIR /usr/src/cpf

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install requirements
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

# copy project
COPY ./ ./src
