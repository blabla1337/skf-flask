#!/bin/bash

# Start the SKF Python API
cd /skf-flask 
export FLASK_APP=skf/app.py
export PYTHONPATH=/skf-flask
export FLASK_DEBUG=True
python3.6 skf/app.py 