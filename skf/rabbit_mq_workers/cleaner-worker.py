#!/usr/bin/env python
from os import path
import datetime as dt
from datetime import datetime
from kubernetes import client, config

from common import delete_all

def cleanK8s():
    try:
        config.load_kube_config()
        api_instance = client.CoreV1Api()
        api_response = api_instance.list_namespaced_pod("")
        for item in api_response.items:
            for container in item.status.container_statuses:
                if "owasp-skf-lab" in container.image:      
                    date_image = container.state.running.started_at
                    format_dt = "%Y-%m-%d %H:%M:%S"
                    date = date_image.strftime(format_dt)
                    dt_obj_img = datetime.strptime(date, format_dt)
                    dt_now = dt.datetime.now().strftime(format_dt)
                    dt_obj_now = datetime.strptime(dt_now, format_dt)
                    diff = dt_obj_now - dt_obj_img 
                    hours_diff = diff.total_seconds() / 3600
                    if int(hours_diff) > 4:
                        delete_all(container.name, item.metadata.namespace)
                    if date_image == "":
                        delete_all(container.name, item.metadata.namespace)
                    print(" [x] The cleaner worker did some cleaning")
    except:
        print("[x] The cleaner worker is done")

# Do the cleaning magic
cleanK8s()
