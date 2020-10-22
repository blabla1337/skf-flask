#!/bin/bash

# Start the SKF Python API
cd /home/user_skf 
export FLASK_APP=skf/app.py
export PYTHONPATH=/home/user_skf
export FLASK_DEBUG=0
python3.7 skf/app.py 

