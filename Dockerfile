# syntax=docker/dockerfile:1
FROM tiangolo/uwsgi-nginx-flask:python3.8-alpine
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /code
COPY requirements.txt /code/
RUN pip install pip --upgrade
RUN pip install -r requirements.txt

COPY . /code/

