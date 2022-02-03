#!/usr/bin/env python3
import os
import subprocess

port = 5000

print(f"session started at {port} port!!!")
one = subprocess.run(f"flask run | celery -A app.celery worker --loglevel=info", shell=True)

print("session finished!!!")