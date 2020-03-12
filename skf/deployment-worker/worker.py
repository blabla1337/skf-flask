#!/usr/bin/env python
import pika
from os import path
import yaml
from kubernetes import client, config
import time

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))
    
channel = connection.channel()
channel.queue_declare(queue='deployment_qeue')

def deploy_container(input_file):
    try:
        serialized_yaml = get_deployment_yaml("hello-world.yaml")
        response = create_deployment(serialized_yaml)
        metadata = validate_k8_response_success(response)
        return metadata
    except:
        return "The deployment has failed, check the logs!"


def get_deployment_yaml(get_yaml):
    with open(path.join(path.dirname(__file__), get_yaml)) as f:
        return yaml.safe_load(f)


def create_deployment(deployment):
    config.load_kube_config()
    k8s_apps_v1 = client.AppsV1Api()
    response = k8s_apps_v1.create_namespaced_deployment(body=deployment, namespace="default")
    return response


def validate_k8_response_success(response):
    return response.metadata


def on_request(ch, method, props, body):
    response = deploy_container(body)
    ch.basic_publish(exchange='',
                     routing_key=props.reply_to,
                     properties=pika.BasicProperties(correlation_id = \
                     props.correlation_id),
                     body=str(response))
    ch.basic_ack(delivery_tag=method.delivery_tag)

channel.basic_qos(prefetch_count=1)
channel.basic_consume(queue='deployment_qeue', on_message_callback=on_request)

print(" [x] Awaiting RPC requests")
channel.start_consuming()