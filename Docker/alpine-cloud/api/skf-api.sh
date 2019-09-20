#!/bin/bash

# Start the SKF Python API
cd /home/user_api/skf-flask 
export FLASK_APP=skf/app.py
export PYTHONPATH=/home/user_api/skf-flask
export FLASK_DEBUG=0
python3.7 skf/app.py 
