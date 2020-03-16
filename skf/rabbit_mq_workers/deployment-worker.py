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

def deploy_container(yaml_file):
    serialized_yaml = get_deployment_yaml(yaml_file)
    create_deployment(serialized_yaml)
    create_service_for_deployment(yaml_file)
    time.sleep(20)
    metadata = get_service_exposed_ip(yaml_file)
    return metadata


def get_deployment_yaml(get_yaml):
    with open(path.join(path.dirname(__file__), 'lab-config-files/'+get_yaml+'.yaml')) as f:
        return yaml.safe_load(f)


def create_deployment(deployment):
    config.load_kube_config()
    k8s_apps_v1 = client.AppsV1Api()
    response = k8s_apps_v1.create_namespaced_deployment(body=deployment, namespace="default")
    return response


def create_service_for_deployment(yaml_file):
    config.load_kube_config()
    api_instance = client.CoreV1Api()
    service = client.V1Service()
    service.api_version = "v1"
    service.kind = "Service"
    service.metadata = client.V1ObjectMeta(name=yaml_file)
    spec = client.V1ServiceSpec()
    spec.type = "LoadBalancer"
    spec.selector = {"app": "test-application"}
    spec.ports = [client.V1ServicePort(protocol="TCP", port=5000, target_port=5000)]
    service.spec = spec
    response = api_instance.create_namespaced_service(namespace="default", body=service)
    return response


def get_service_exposed_ip(yaml_file):
    config.load_kube_config()
    api_instance = client.CoreV1Api()
    response = api_instance.read_namespaced_service(yaml_file, 'default', pretty=True)
    return response


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