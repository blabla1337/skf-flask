#!/bin/bash

set -ex

if [ "$LABS_KUBE_CONF" != "~/.kube/config" ]
then
 echo $LABS_KUBE_CONF | base64 -d > /home/user_api/.kube/config
fi

#to get the base64 string of your .kube/config run:
#cat ~/.kube/config | base64

cd /home/user_api
export FLASK_APP=/home/user_api/skf/app.py
export PYTHONPATH=/home/user_api

# init the database
/home/user_api/.local/bin/flask initdb

# Start the SKF Python API
/home/user_api/.local/bin/gunicorn --bind 0.0.0.0:8888 --workers=6 --threads=3 wsgi:app
