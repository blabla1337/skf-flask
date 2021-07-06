#!/bin/bash

# dirty hack for making sure rabbitmq is running...
sleep 30

cd /home/user_api
export FLASK_APP=/home/user_api/skf/app.py
export PYTHONPATH=/home/user_api

# Start the SKF Python workers
python3.7 skf/rabbit_mq_workers/deployment-worker.py &
python3.7 skf/rabbit_mq_workers/deletion-worker.py &

# Run the SKF Python cleaner worker every 30 min
while true  
do  
  sleep 7200
  python3.7 skf/rabbit_mq_workers/cleaner-worker.py 
done