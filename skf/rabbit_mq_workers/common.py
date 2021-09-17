import time
from sys import stderr
from kubernetes import client, config

def delete_all(instance_name, user_id):
    delete_ingress(deployment, user_id)
    delete_service(deployment, user_id)
    delete_deployment(deployment, user_id)

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
        print("Deployment deleted. status='%s'" % str(api_response.status))
    except Exception as err:
        print('Error deleteing deployment:', err, file=stderr)

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
        print("Deployment deleted. status='%s'" % str(api_response.status))
    except:
        print('Error deleting service:', err, file=stderr)

def delete_ingress(instance_name, user_id):
    try:
        config.load_kube_config()
        networking_v1_beta1_api = client.NetworkingV1beta1Api()
        api_response = networking_v1_beta1_api.delete_namespaced_ingress(
            name='ingress-'+instance_name,
            namespace=user_id,
            body=client.V1DeleteOptions(
                propagation_policy='Foreground',
                grace_period_seconds=5))
        print("Ingress deleted. status='%s'" % str(api_response.status))
    except:
        print('Error deleting ingress (this may not exist, that ok', err, file=stderr)

