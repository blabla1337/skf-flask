#!/bin/bash

set -x 

ORIGIN=${ORIGIN:-'localhost'}

if [[ "$ORIGIN" != "" ]]; then
    perl -pi -e "s/http:\/\/127.0.0.1:8888\/api/https:\/\/$ORIGIN\/api/" /home/user_api/skf-flask/Angular/src/environments/environment.prod.ts
    perl -pi -e "s/http:\/\/127.0.0.1:8888\/api/https:\/\/$ORIGIN\/api/" /home/user_api/skf-flask/Angular/src/environments/environment.ts
else
    echo 'You need to select a ORIGIN location'
    exit
fi
