#!/usr/bin/env python
import pika
from os import path
import yaml
from kubernetes import client, config
import time
import random

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()
channel.queue_declare(queue='deployment_qeue')


def deploy_container(rpc_body):
    user_id = string_split_user_id(rpc_body)
    deployment = string_split_deployment(rpc_body)
    create_user_namespace(user_id)
    deployment_object = create_deployment_object(deployment)
    create_deployment(deployment_object, user_id)
    create_service_for_deployment(deployment, user_id)
    time.sleep(5)
    response = get_service_exposed_ip(deployment, user_id)
    host_and_port = get_host_port_from_response(response)
    return host_and_port


def create_user_namespace(user_id):
    try:
        config.load_kube_config()
        api_instance = client.CoreV1Api()
        body = client.V1Namespace()
        body.metadata = client.V1ObjectMeta(name=user_id)
        api_response = api_instance.create_namespace(body)
    except:
        return False    


def create_deployment_object(deployment):
    # Configureate Pod template container
    container = client.V1Container(
        name=deployment,
        image="blabla1337/owasp-skf-lab:"+deployment,
        ports=[client.V1ContainerPort(container_port=5000)])
    # Create and configurate a spec section
    template = client.V1PodTemplateSpec(
        metadata=client.V1ObjectMeta(labels={"app": deployment}),
        spec=client.V1PodSpec(containers=[container]))
    # Create the specification of deployment
    spec = client.V1DeploymentSpec(
        replicas=1,
        template=template,
        selector={'matchLabels': {'app': deployment}})
    # Instantiate the deployment object
    deployment = client.V1Deployment(
        api_version="apps/v1",
        kind="Deployment",
        metadata=client.V1ObjectMeta(name=deployment),
        spec=spec)
    return deployment


def create_deployment(deployment, user_id):
    try:
        config.load_kube_config()
        k8s_apps_v1 = client.AppsV1Api()
        response = k8s_apps_v1.create_namespaced_deployment(body=deployment, namespace=user_id)
        return response
    except:
        return False


def create_service_for_deployment(deployment, user_id):
    try:
        config.load_kube_config()
        api_instance = client.CoreV1Api()
        service = client.V1Service()
        service.api_version = "v1"
        service.kind = "Service"
        service.metadata = client.V1ObjectMeta(name=deployment)
        spec = client.V1ServiceSpec()
        spec.type = "LoadBalancer"
        spec.selector = {"app": deployment}
        random_port = random.randrange(40000, 60000)
        spec.ports = [client.V1ServicePort(protocol="TCP", port=random_port, target_port=5000)]
        service.spec = spec
        response = api_instance.create_namespaced_service(namespace=user_id, body=service)
        return response
    except:
        return False


def get_service_exposed_ip(deployment, user_id):
    try:
        config.load_kube_config()
        api_instance = client.CoreV1Api()
        response = api_instance.read_namespaced_service(deployment, user_id, pretty=True)
        return response
    except:
        return False


def string_split_user_id(body):
    user_id = body.split(':')
    return user_id[1]


def string_split_deployment(body):
    deployment = body.split(':')
    return deployment[0]

def get_host_port_from_response(response):
    for bla in response.spec.ports:
        port = bla.port
    for bla in response.status.load_balancer.ingress:
        host = bla.hostname  
    return "i am running on  -  " + host + ":" + str(port)

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
