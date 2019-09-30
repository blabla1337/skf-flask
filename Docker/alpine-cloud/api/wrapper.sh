#!/bin/bash

# Start the first process
/home/user_api/skf-flask/skf-api.sh &
status=$?
if [ $status -ne 0 ]; then
  echo "Failed to start skf_api_process: $status"
  exit $status
fi

# Naive check runs checks once a minute to see if either of the processes exited.
# This illustrates part of the heavy lifting you need to do if you want to run
# more than one service in a container. The container will exit with an error
# if it detects that either of the processes has exited.
# Otherwise it will loop forever, waking up every 60 seconds
  
while /bin/true; do
  PROCESS_1_STATUS=$(ps aux |grep -q skf-api* |grep -v grep)
  # If the greps above find anything, they will exit with 0 status
  # If they are not both 0, then something is wrong
  if [[ $PROCESS_1_STATUS -ne '0' ]]; then
    echo "The process has already exited."
    exit -1
  fi
  sleep 10
done
