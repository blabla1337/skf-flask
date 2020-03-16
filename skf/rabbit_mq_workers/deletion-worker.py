#!/usr/bin/env python
import pika
from os import path
import yaml
from kubernetes import client, config
import time

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))
    
channel = connection.channel()
channel.queue_declare(queue='deletion_qeue')

def delete_container(instance_name):
    delete_deployment(instance_name)
    delete_service(instance_name)
    return "asdasd"

def delete_deployment(instance_name):
    config.load_kube_config()
    api_instance = client.AppsV1Api()
    api_response = api_instance.delete_namespaced_deployment(
        name=instance_name,
        namespace="default",
        body=client.V1DeleteOptions(
            propagation_policy='Foreground',
            grace_period_seconds=5))
    print("Deployment deleted. status='%s'" % str(api_response.status))


def delete_service(instance_name):
    config.load_kube_config()
    api_instance = client.CoreV1Api()
    api_response = api_instance.delete_namespaced_service(
        name=instance_name,
        namespace="default",
        body=client.V1DeleteOptions(
            propagation_policy='Foreground',
            grace_period_seconds=5))
    print("Deployment deleted. status='%s'" % str(api_response.status))


def on_request(ch, method, props, body):
    response = delete_container(str(body, 'utf-8'))
    ch.basic_publish(exchange='',
                     routing_key=props.reply_to,
                     properties=pika.BasicProperties(correlation_id = \
                     props.correlation_id),
                     body=str(response))
    ch.basic_ack(delivery_tag=method.delivery_tag)

channel.basic_qos(prefetch_count=1)
channel.basic_consume(queue='deletion_qeue', on_message_callback=on_request)

print(" [x] Awaiting RPC requests")
channel.start_consuming()