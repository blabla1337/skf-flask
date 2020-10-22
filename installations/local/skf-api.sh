#!/bin/bash

# Start the SKF Python API
cd ../..
export FLASK_APP=skf/app.py
export PYTHONPATH=./
export FLASK_DEBUG=0
/usr/bin/env python3.6 skf/app.py
