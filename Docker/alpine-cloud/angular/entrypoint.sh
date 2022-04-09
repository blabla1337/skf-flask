#!/usr/bin/env sh

set -ex

ORIGIN=${FRONTEND_URI:-http://localhost:8888}
SKIP=${SKIP_LOGIN:-skfprovider}

echo "angular will try to contact the api at: ${ORIGIN}/api"
find /usr/share/nginx/html -type f -exec sed -i -e "s,http://localhost:8888,${ORIGIN},g" {} \;
cp $1 /etc/nginx/conf.d/site.conf
cat /etc/nginx/conf.d/site.conf
find /usr/share/nginx/html -type f -exec sed -i -e "s,skfprovider,${SKIP},g" {} \;
exec nginx -g "daemon off;"
