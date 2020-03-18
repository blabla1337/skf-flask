#!/bin/bash

cd /home/user_api
export FLASK_APP=/home/user_api/skf/app.py
export PYTHONPATH=/home/user_api

# Start the SKF Python API
/home/user_api/.local/bin/gunicorn --bind 0.0.0.0:8888 wsgi:app
