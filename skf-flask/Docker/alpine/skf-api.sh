#!/bin/bash

# Start the SKF Python API
cd /skf-flask 
export FLASK_APP=skf/app.py
export PYTHONPATH=/skf-flask
export FLASK_DEBUG=0
python3.7 skf/app.py 

