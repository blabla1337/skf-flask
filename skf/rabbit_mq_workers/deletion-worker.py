#!/usr/bin/env python
import pika, time
from skf import settings
from common import delete_all

creds = pika.PlainCredentials('admin', 'admin-skf-secret')
connection = pika.BlockingConnection(pika.ConnectionParameters(
    host=settings.RABBIT_MQ_CONN_STRING,
    credentials=creds
))
channel = connection.channel()
channel.queue_declare(queue='deletion_qeue')

def delete_container(rpc_body):
    user_id = string_split_user_id(rpc_body)
    deployment = string_split_deployment(rpc_body)
    delete_all(deployment, user_id)
    time.sleep(3)
    return {'message': 'If present, the container image was deleted from the cluster!'} 

def string_split_user_id(body):
    try:
        user_id = body.split(':')
        return user_id[1]
    except:
        return {'message': 'Failed to deploy, error no user_id found!'} 


def string_split_deployment(body):
    try:
        deployment = body.split(':')
        return deployment[0]
    except:
        return {'message': 'Failed to delete, error no deployment found!'} 


def on_request(ch, method, props, body):
    response = delete_container(str(body, 'utf-8'))
    ch.basic_publish(exchange='',
                     routing_key=props.reply_to,
                     properties=pika.BasicProperties(correlation_id = \
                     props.correlation_id,
                     expiration='30000'),
                     body=str(response))
    ch.basic_ack(delivery_tag=method.delivery_tag)

channel.basic_qos(prefetch_count=1)
channel.basic_consume(queue='deletion_qeue', on_message_callback=on_request)

print(" [x] Awaiting RPC requests")
channel.start_consuming()
