FROM python:3.10-slim-buster

WORKDIR /ieltsways-back

COPY /requirements/requirements.txt /ieltsways-back/requirements/

RUN pip install --upgrade pip

RUN apt-get update && apt-get upgrade -y

RUN pip install -r requirements/requirements.txt

COPY . /ieltsways-back

EXPOSE 8000 9000