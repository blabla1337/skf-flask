#!/bin/bash

set -x 

HTTPS=${HTTPS:-'true'}
JWT_SECRET=${JWT_SECRET:-'changeme'}
ORIGIN=${ORIGIN:-'localhost'}


# Creation of certificates
if [[ "$HTTPS" == "true" ]]; then
    if [[ -e "/skf-flask/server.pem" && -e "/skf-flask/server.key" ]]; then
        CERT="/skf-flask/server.pem"
        KEY="/skf-flask/server.key"
    else
        if [[ ! -z "$CERT" && ! -z "$KEY" ]]; then
            echo "$CERT" > "/skf-flask/server.pem"
            echo "$KEY" > "/skf-flask/server.key"
        else
            openssl req -nodes -newkey rsa:4096 -keyout /skf-flask/server.key -out /skf-flask/server.csr  -subj "/CN=OWASP-SKF"       
            openssl x509 -req -days 365 -in /skf-flask/server.csr  -signkey /skf-flask/server.key -out /skf-flask/server.pem
            rm /skf-flask/server.csr
        fi
        CERT="/skf-flask/server.pem"
        KEY="/skf-flask/server.key"
    fi
    PORT=443
else
    CERT=""
    KEY=""
    PORT=80
fi

if [[ "$JWT_SECRET" != "changeme" ]]; then
    perl -pi -e "s/JWT_SECRET = ''/JWT_SECRET = '$JWT_SECRET'/" /skf-flask/skf/settings.py
else
    echo 'You need to select a JWT_SECRET'
    exit
fi

if [[ "$ORIGIN" != "" ]]; then
    perl -pi -e "s/\*/https:\/\/$ORIGIN/" /skf-flask/skf/settings.py
    perl -pi -e "s/https:\/\/localhost\/api/https:\/\/$ORIGIN\/api/" /skf-flask/Angular/src/environments/environment.prod.ts
else
    echo 'You need to select a ORIGIN location'
    exit
fi

# Create Nginx dir
mkdir /run/nginx

# Generate files for Nginx
nginx
sleep 5
rm /etc/nginx/conf.d/default.conf

# Stop nginx
killall nginx

if [[ "$HTTPS" == "true" ]]; then
    cp /skf-flask/Docker/alpine/site-tls.conf /etc/nginx/conf.d/default.conf
else
    cp /skf-flask/Docker/alpine/site.conf /etc/nginx/conf.d/default.conf
fi

# Start nginx
sleep 5
nginx

# Start SKF services
/wrapper.sh
