#!/usr/bin/env sh

set -ex

BACKEND="${BACKEND_URI:-http://skf-flask-back.default.svc.cluster.local:8888}"
BACKEND_DOM=$(echo ${BACKEND_URI} | cut -d'/' -f3 | cut -d':' -f1,2)

ORIGIN=${FRONTEND_URI:-http://127.0.0.1:8888}
FRONT_DOMAIN=$(echo ${FRONTEND_URI} | cut -d'/' -f3 | cut -d':' -f1,2)

CERT="${SERVER_CERT_PATH:-/skf-flask/server.pem}"
KEY="${SERVER_CERT_KEY:-/skf-flask/server.key}"

HTTPS="${TLS:-\"true\"}"

NGINX_HTTPS_BLOCK=`cat << EOF
       listen 443 ssl http2;
        ssl_certificate \\${NGINX_SERVER_CERT_PATH};
        ssl_certificate_key \\${NGINX_SERVER_CERT_KEY};
        # Strong TLS settings
        ssl_protocols TLSv1.2;
        ssl_ciphers 'ECDHE-RSA-AES256-GCM-SHA384:ECDHE-RSA-AES128-GCM-SHA256:ECDHE-RSA-AES256-SHA384:ECDHE-RSA-AES128-SHA256';
        ssl_prefer_server_ciphers on;
        if (\\$scheme = http) {
            return 301 https://$host:443$request_uri;
        }
EOF
`

if [[ ${HTTPS} == "false" ]]; then
    # ability to turn off TLS for development
    export TLS_BLOCK=""
else
    export TLS_BLOCK="${NGINX_HTTPS_BLOCK}"
    export NGINX_SERVER_CERT_PATH="${CERT}"
    export NGINX_SERVER_CERT_KEY="${KEY}"
fi

echo "angular will try to contact the api at: ${ORIGIN}/api"
find /usr/share/nginx/html -type f -exec sed -i -e "s,http://127.0.0.1:8888/api,${ORIGIN}/api,g" {} \;
# grep -r "${BACKEND}" $1

export SKF_BACKEND_DOMAIN=${BACKEND_DOM}
export SKF_BACKEND_URL=${BACKEND}
export NGINX_SERVER_NAME=${FRONT_DOMAIN}

envsubst "\${SKF_BACKEND_URL}\${NGINX_SERVER_NAME}\${SKF_BACKEND_DOMAIN}}\${NGINX_SERVER_CERT_KEY}\${NGINX_SERVER_CERT_PATH}\${TLS_BLOCK}"< $1 > /etc/nginx/conf.d/site.conf

# below code is because envsubst won't substitute the values in the NGINX https block
sed -i -e "s,\${NGINX_SERVER_CERT_PATH},${NGINX_SERVER_CERT_PATH},g" /etc/nginx/conf.d/site.conf
sed -i -e "s,\${NGINX_SERVER_CERT_KEY},${NGINX_SERVER_CERT_KEY},g" /etc/nginx/conf.d/site.conf



cat /etc/nginx/conf.d/site.conf

exec nginx -g "daemon off;"
