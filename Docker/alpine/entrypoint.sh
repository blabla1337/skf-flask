
HTTPS=${HTTPS:-'true'}

# Creation of certificates
if [[ "$HTTPS" == "true"]]; then
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

rm /run/nginx/conf.d/default.conf
if [[ "$HTTPS" == "true" ]]; then
    cp /site-tls.conf /run/nginx/conf.d/default.conf
else
    cp /front.conf /run/nginx/conf.d/default.conf
fi
# Reload Nginx
nginx