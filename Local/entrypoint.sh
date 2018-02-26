#!/bin/bash

set -x 

HTTPS=${HTTPS:-'true'}
JWT_SECRET=${JWT_SECRET:-'changeme'}
ORIGIN=${ORIGIN:-'localhost'}

# Creation of certificates
if [[ "$HTTPS" == "true" ]]; then
    if [[ -e "./server.pem" && -e "./server.key" ]]; then
        CERT="./server.pem"
        KEY="./server.key"
    else
        if [[ ! -z "$CERT" && ! -z "$KEY" ]]; then
            echo "$CERT" > "./server.pem"
            echo "$KEY" > "./server.key"
        else
            openssl req -nodes -newkey rsa:4096 -keyout ./server.key -out ./server.csr  -subj "/CN=OWASP-SKF"       
            openssl x509 -req -days 365 -in ./server.csr  -signkey ./server.key -out ./server.pem
            rm ./server.csr
        fi
        CERT="./server.pem"
        KEY="./server.key"
    fi
    PORT=443
else
    CERT=""
    KEY=""
    PORT=80
fi

if [[ "$JWT_SECRET" != "changeme" ]]; then
    perl -pi -e "s/JWT_SECRET = ''/JWT_SECRET = '$JWT_SECRET'/" ../skf/settings.py
else
    echo 'You need to select a JWT_SECRET'
    exit
fi

if [[ "$ORIGIN" != "" ]]; then
    perl -pi -e "s/\*/https:\/\/$ORIGIN/" ../skf/settings.py
else
    echo 'You need to select a ORIGIN location'
    exit
fi

if [[ "$HTTPS" == "true" ]]; then
    cp site-tls.conf /etc/nginx/conf.d/default.conf
else
    cp site.conf /etc/nginx/conf.d/default.conf
fi

# Start nginx
sleep 5
sudo nginx

# Start SKF services
bash wrapper.sh
