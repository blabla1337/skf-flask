#!/bin/bash

set -x
ORIGIN=${ORIGIN:-'localhost'}

# Start the SKF Angular app
cd /skf-flask/Angular
ng serve --configuration=production --publicHost $ORIGIN
