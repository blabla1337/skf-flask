#!/bin/bash

# Start the SKF Python API
cd /home/user_skf/skf/rabbit_mq_workers
export PYTHONPATH=/home/user_skf
python3.7 deployment-worker.py 
python3.7 deletion-worker.py 

