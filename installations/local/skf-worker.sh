#!/bin/bash

# dirty hack for making sure rabbitmq is running...
sleep 30

cd ../..
export FLASK_APP=skf/app.py
export PYTHONPATH=.

# Start the SKF Python workers
python3 skf/rabbit_mq_workers/deployment-worker.py &
python3 skf/rabbit_mq_workers/deletion-worker.py &

# Run the SKF Python cleaner worker every 30 min
while true  
do  
  python3 skf/rabbit_mq_workers/cleaner-worker.py 
  sleep 7200  
done