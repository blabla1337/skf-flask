#!/bin/bash

#We need to wait till the database is started...
sleep 20

# Start the first process
bash skf-api.sh &

# Start the first process
bash skf-angular.sh &

# Start the second process
bash skf-worker.sh &
