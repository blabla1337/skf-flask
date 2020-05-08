#!/usr/bin/env sh

set -ex

ORIGIN=${FRONTEND_URI:-http://127.0.0.1:8788}

echo "angular will try to contact the api at: ${ORIGIN}/api"
find /usr/share/nginx/html -type f -exec sed -i -e "s,http://127.0.0.1:8888/api,${ORIGIN}/api,g" {} \;

cp $1 /etc/nginx/conf.d/site.conf
cat /etc/nginx/conf.d/site.conf

exec nginx -g "daemon off;"
