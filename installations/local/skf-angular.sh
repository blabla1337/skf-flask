#!/bin/bash

# Start the SKF Angular app
<<<<<<< HEAD
cd ../../Angular2
ng serve --public-host localhost:443
=======
cd ../../Angular
configuration=${1:-production}
ng serve --configuration=$configuration --public-host localhost:443
>>>>>>> origin/master
