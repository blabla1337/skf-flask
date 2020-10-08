#!/usr/bin/env python
import time, random, yaml
from os import path
import datetime as dt
from kubernetes import client, config


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
                        delete_service("undefined", item.metadata.namespace)
                        delete_deployment("undefined", item.metadata.namespace)
                    date_image = container.state.running.started_at
                    hour_image = date_image.strftime("%H").lstrip("0").replace(" 0", " ")
                    hour_now = dt.datetime.now().hour
                    if hour_image != hour_now:
                        delete_service(container.name, item.metadata.namespace)
                        delete_deployment(container.name, item.metadata.namespace)
                    if date_image == "":
                        delete_service(container.name, item.metadata.namespace)
                        delete_deployment(container.name, item.metadata.namespace)
                    print(" [x] The cleaner worker did some cleaning")
    except:
        print("[x] The cleaner worker is done")


def delete_deployment(instance_name, user_id):
    try:
        config.load_kube_config()
        api_instance = client.AppsV1Api()
        api_response = api_instance.delete_namespaced_deployment(
            name=instance_name,
            namespace=user_id,
            body=client.V1DeleteOptions(
                propagation_policy='Foreground',
                grace_period_seconds=5))
        print("Deployment labs deleted. status='%s'" % str(api_response.status))
    except:
        print("Deployment delete labs error")


def delete_service(instance_name, user_id):
    try:
        config.load_kube_config()
        api_instance = client.CoreV1Api()
        api_response = api_instance.delete_namespaced_service(
            name=instance_name,
            namespace=user_id,
            body=client.V1DeleteOptions(
                propagation_policy='Foreground',
                grace_period_seconds=5))
        print("Service labs deleted. status='%s'" % str(api_response.status))
    except:
        print("Service delete labs error")



# Do the cleaning magic
cleanK8s()


