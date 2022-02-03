#!/bin/bash
app="9873311/flask_task"
docker build -t ${app} .
docker-compose up
