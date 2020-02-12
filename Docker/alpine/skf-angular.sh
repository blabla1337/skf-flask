#!/bin/bash

set -x
ORIGIN=${ORIGIN:-'localhost'}

# Start the SKF Angular app
cd /home/user_skf/Angular
ng serve --configuration=production  --host 0.0.0.0 --publicHost $ORIGIN
