#!/bin/bash

# Start the SKF Python API
cd ../..
export FLASK_APP=skf/app.py
export PYTHONPATH=.
export SKF_FLASK_DEBUG='False'

/usr/bin/env python3 skf/app.py
