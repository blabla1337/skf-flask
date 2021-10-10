#!/usr/bin/env python
from os import path
import datetime as dt
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
                    image_id = container.image_id.split('\n')
                    if image_id:
                        delete_all("undefined", item.metadata.namespace)
                    date_image = container.state.running.started_at
                    hour_image = date_image.strftime("%H").lstrip("0").replace(" 0", " ")
                    hour_now = dt.datetime.now().hour
                    if hour_image != hour_now:
                        delete_all(container.name, item.metadata.namespace)
                    if date_image == "":
                        delete_all(container.name, item.metadata.namespace)
                    print(" [x] The cleaner worker did some cleaning")
    except:
        print("[x] The cleaner worker is done")

# Do the cleaning magic
cleanK8s()

