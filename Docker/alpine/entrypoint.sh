#!/bin/bash

set -x 

HTTPS=${HTTPS:-'true'}
JWT_SECRET=${JWT_SECRET:-'changeme'}
ORIGIN=${ORIGIN:-'localhost'}


# Creation of certificates
if [[ "$HTTPS" == "true" ]]; then
    if [[ -e "/home/user_skf/server.pem" && -e "/home/user_skf/server.key" ]]; then
        CERT="/home/user_skf/server.pem"
        KEY="/home/user_skf/server.key"
    else
        if [[ ! -z "$CERT" && ! -z "$KEY" ]]; then
            echo "$CERT" > "/home/user_skf/server.pem"
            echo "$KEY" > "/home/user_skf/server.key"
        else
            openssl req -nodes -newkey rsa:4096 -keyout /home/user_skf/server.key -out /home/user_skf/server.csr  -subj "/CN=OWASP-SKF"       
            openssl x509 -req -days 365 -in /home/user_skf/server.csr  -signkey /home/user_skf/server.key -out /home/user_skf/server.pem
            rm /home/user_skf/server.csr
        fi
        CERT="/home/user_skf/server.pem"
        KEY="/home/user_skf/server.key"
    fi
    PORT=443
else
    CERT=""
    KEY=""
    PORT=80
fi

if [[ "$JWT_SECRET" != "changeme" ]]; then
    perl -pi -e "s/JWT_SECRET = ''/JWT_SECRET = '$JWT_SECRET'/" /home/user_skf/skf/settings.py
else
    echo 'You need to select a JWT_SECRET'
    exit
fi

if [[ "$ORIGIN" != "" ]]; then
    perl -pi -e "s/\*/https:\/\/$ORIGIN/" /home/user_skf/skf/settings.py
    perl -pi -e "s/http:\/\/127.0.0.1:8888\/api/https:\/\/$ORIGIN\/api/" /home/user_skf/Angular/src/environments/environment.prod.ts
else
    echo 'You need to select a ORIGIN location'
    exit
fi

# Create Nginx dir
mkdir /run/nginx

# Generate files for Nginx
nginx
sleep 5
rm /etc/nginx/sites-enabled/default

# Stop nginx
pkill nginx

if [[ "$HTTPS" == "true" ]]; then
    cp /home/user_skf/Docker/alpine/site-tls.conf /etc/nginx/sites-enabled/default.conf
else
    cp /home/user_skf/Docker/alpine/site.conf /etc/nginx/sites-enabled/default.conf
fi

# Start nginx
sleep 5
nginx

# Start SKF services
/wrapper.sh
