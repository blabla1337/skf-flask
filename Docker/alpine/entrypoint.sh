#!/bin/ash

set -x 

HTTPS=${HTTPS:-'true'}

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

# Create Nginx dir
mkdir /run/nginx
# Generate files for Nginx
nginx
rm /etc/nginx/conf.d/default.conf

if [[ "$HTTPS" == "true" ]]; then
    cp /skf-flask/Docker/alpine/site-tls.conf /etc/nginx/conf.d/default.conf
else
    cp /skf-flask/Docker/alpine/front.conf /etc/nginx/conf.d/default.conf
fi

killall nginx
nginx

# Start the SKF Angular app
cd /skf-flask/Angular
npm start

# Start the SKF Python API
cd /skf-flask 
export FLASK_APP=skf/app.py
export PYTHONPATH=/skf-flask
python3.6 skf/app.py
