#!/bin/bash

# Start the SKF Angular app
cd ../../Angular
configuration=${1:-production}
ng serve --configuration=$configuration --public-host localhost:443
