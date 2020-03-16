#!/usr/bin/env python
import pika
from os import path
import yaml
from kubernetes import client, config
import time
import random

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))
    
channel = connection.channel()
channel.queue_declare(queue='deployment_qeue')

def deploy_container(yaml_file):
    #create_user_namespace()
    serialized_yaml = get_deployment_yaml(yaml_file)
    create_deployment(serialized_yaml)
    create_service_for_deployment(yaml_file)
    time.sleep(5)
    metadata = get_service_exposed_ip(yaml_file)
    return metadata



def get_deployment_yaml(get_yaml):
    try:
        with open(path.join(path.dirname(__file__), 'lab-config-files/'+get_yaml+'.yaml')) as f:
            return yaml.safe_load(f)
    except: 
        return False

"""
def create_user_namespace():
    try:
        config.load_kube_config()
        api_instance = client.CoreV1Api()
        body = client.V1Namespace()
        body.metadata = client.V1ObjectMeta(name="gelukt")
        api_response = api_instance.create_namespace(body)
        print(api_response)
    except:
        return False    
"""

def create_deployment(deployment):
    try:
        config.load_kube_config()
        k8s_apps_v1 = client.AppsV1Api()
        response = k8s_apps_v1.create_namespaced_deployment(body=deployment, namespace="default")
        return response
    except:
        return False


def create_service_for_deployment(yaml_file):
    try:
        config.load_kube_config()
        api_instance = client.CoreV1Api()
        service = client.V1Service()
        service.api_version = "v1"
        service.kind = "Service"
        service.metadata = client.V1ObjectMeta(name=yaml_file)
        spec = client.V1ServiceSpec()
        spec.type = "LoadBalancer"
        spec.selector = {"app": "test-application"}
        random_port = random.randrange(40000, 60000)
        spec.ports = [client.V1ServicePort(protocol="TCP", port=random_port, target_port=5000)]
        service.spec = spec
        response = api_instance.create_namespaced_service(namespace="default", body=service)
        return response
    except:
        return False


def get_service_exposed_ip(yaml_file):
    try:
        config.load_kube_config()
        api_instance = client.CoreV1Api()
        response = api_instance.read_namespaced_service(yaml_file, 'default', pretty=True)
        return response
    except:
        return False


def on_request(ch, method, props, body):
    response = deploy_container(str(body, 'utf-8'))
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