#!/bin/bash

set -x 

JWT_SECRET=${JWT_SECRET:-'changeme'}
ORIGIN=${ORIGIN:-'localhost'}


if [[ "$JWT_SECRET" != "changeme" ]]; then
    perl -pi -e "s/JWT_SECRET = ''/JWT_SECRET = '$JWT_SECRET'/" /home/user_api/skf-flask/skf/settings.py
else
    echo 'You need to select a JWT_SECRET'
    exit
fi

if [[ "$ORIGIN" != "" ]]; then
    perl -pi -e "s/\*/https:\/\/$ORIGIN/" /home/user_api/skf-flask/skf/settings.py
else
    echo 'You need to select a ORIGIN location'
    exit
fi

# Start SKF services
/home/user_api/skf-flask/wrapper.sh

