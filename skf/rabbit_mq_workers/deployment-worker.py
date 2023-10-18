#!/usr/bin/env python
import logging.config, os, pika, random, re, time
from skf import settings
from kubernetes import client, config

from sys import stderr


logging.config.fileConfig('logging.conf')
log = logging.getLogger(__name__)


creds = pika.PlainCredentials('admin', 'admin-skf-secret')
connection = pika.BlockingConnection(pika.ConnectionParameters(
    host=settings.RABBIT_MQ_CONN_STRING,
    credentials=creds,
))
channel = connection.channel()
channel.queue_declare(queue='deployment_qeue')

labs_namespace = settings.SKF_LABS_NAMESPACE

labs_domain = os.environ['SKF_LABS_DOMAIN']
subdomain_deploy = os.environ.get('SKF_LABS_DEPLOY_MODE') == 'subdomain'
if subdomain_deploy:
    (labs_protocol, labs_domain) = re.compile('(.*:\/\/)?(.*)').match(labs_domain).groups()
    if labs_protocol is None:
        labs_protocol = 'http://'
    print('Subdomain deploy using {}<lab>.{}'.format(labs_protocol, labs_domain))
else:
    print('Port deploy using {}:<port>'.format(labs_domain))

def deploy_container(rpc_body):
    user_id = string_split_user_id(rpc_body)
    deployment = string_split_deployment(rpc_body)
    create_labs_namespace(labs_namespace)
    deployment_object = create_deployment_object(deployment, user_id)
    create_deployment(deployment_object, labs_namespace, user_id)
    try:
        service_port = create_service_for_deployment(deployment, labs_namespace, user_id)
    except Exception as ex:
        log.error(ex)
        return {'message': 'Failed to deploy, error K8s API create service call!'} 
    time.sleep(15)
    response = get_service_exposed_ip(deployment, labs_namespace, user_id)
    if subdomain_deploy:
        hostname = '{}-{}-{}'.format(deployment, user_id, labs_domain)
        networking_v1_api = client.NetworkingV1Api()
        ingress_err = create_ingress(networking_v1_api, hostname, deployment, service_port, labs_namespace, user_id)
        if ingress_err is not None:
            return { 'message': ingress_err }
        return { 'message': "'" + labs_protocol + hostname + "'" }
    else:
        return get_host_port_from_response(response)

def create_labs_namespace(namespace):
    try:
        config.load_kube_config()
        api_instance = client.CoreV1Api()
        body = client.V1Namespace()
        body.metadata = client.V1ObjectMeta(name=namespace)
        api_response = api_instance.create_namespace(body)
    except:
        return {'message': 'Failed to deploy, error namespace creation!'} 

def create_deployment_object(deployment, user_id):
    try:
        # Configureate Pod template container
        container = client.V1Container(
            name=deployment + '-' + user_id,
            image="blabla1337/owasp-skf-lab:"+deployment,
            ports=[client.V1ContainerPort(container_port=5000)])
        # Create and configurate a spec section
        template = client.V1PodTemplateSpec(
            metadata=client.V1ObjectMeta(labels={"app": deployment + "-" + user_id}),
            spec=client.V1PodSpec(containers=[container]))
        # Create the specification of deployment
        spec = client.V1DeploymentSpec(
            replicas=1,
            template=template,
            selector={'matchLabels': {'app': deployment+"-"+user_id}})
        # Instantiate the deployment object
        deployment = client.V1Deployment(
            api_version="apps/v1",
            kind="Deployment",
            metadata=client.V1ObjectMeta(name=deployment+"-"+user_id),
            spec=spec)
        return deployment
    except:
        return {'message': 'Failed to deploy, error creation deployment object!'} 

def create_deployment(deployment, namespace, user_id):
    try:
        config.load_kube_config()
        k8s_apps_v1 = client.AppsV1Api()
        response = k8s_apps_v1.create_namespaced_deployment(body=deployment, namespace=namespace)
        return response
    except:
        return {'message': 'Failed to deploy, error K8s API create call!'} 

def create_service_for_deployment(deployment, namespace, user_id):
    config.load_kube_config()
    api_instance = client.CoreV1Api()
    service = client.V1Service()
    service.api_version = "v1"
    service.kind = "Service"
    service.metadata = client.V1ObjectMeta(name=deployment + "-" + user_id)

    spec = client.V1ServiceSpec()
    spec.type = "NodePort"
    spec.selector = {"app": deployment + "-" + user_id}
    # Why a random port?
    random_port = random.randrange(40000, 60000)
    spec.ports = [client.V1ServicePort(protocol="TCP", port=random_port, target_port=5000)]
    service.spec = spec

    response = api_instance.create_namespaced_service(namespace=namespace, body=service)
    return random_port

def get_service_exposed_ip(deployment, namespace, user_id):
    try:
        config.load_kube_config()
        api_instance = client.CoreV1Api()
        response = api_instance.read_namespaced_service(deployment+"-"+user_id, namespace, pretty=True)
        return response
    except:
        return {'message': 'Failed to deploy, error service no exposed IP!'} 

def string_split_user_id(body):
    try:
        user_id = body.split(':')
        return user_id[1]
    except:
        return {'message': 'Failed to deploy, error no user_id found!'} 

def string_split_port(host_port):
    try:
        port = host_port.split(':')
        return port[1]
    except:
        return {'message': 'Failed to create ingress, error no port found!'} 

def string_split_host(host_port):
    try:
        host = host_port.split(':')
        return host[0]
    except:
        return {'message': 'Failed to deploy, error no host found!'} 

def string_split_deployment(body):
    try:
        deployment = body.split(':')
        return deployment[0]
    except:
        return {'message': 'Failed to deploy, error no deployment found!'} 

def get_host_port_from_response(response):
    try:
        for service in response.spec.ports:
            node_port = service.node_port
        return {'message': "'"+ labs_domain + ":" + str(node_port)+"'"}
    except:
        return {'message': 'Failed to deploy, error no host or port!'} 

def on_request(ch, method, props, body):
        response = deploy_container(str(body, 'utf-8'))
        ch.basic_publish(exchange='',
                        routing_key=props.reply_to,
                        properties=pika.BasicProperties(correlation_id = \
                        props.correlation_id,
                        expiration='30000'),
                        body=str(response))
        ch.basic_ack(delivery_tag=method.delivery_tag)

def create_ingress(networking_v1_api, hostname, deployment, service_port, namespace, user_id):
    try:
        body = client.V1Ingress(
            api_version="networking.k8s.io/v1",
            kind="Ingress",
            metadata=client.V1ObjectMeta(name="ingress-"+deployment+"-"+user_id, annotations={
                "kubernetes.io/ingress.class": "nginx",
                #"nginx.ingress.kubernetes.io/rewrite-target": "/",
            }),
            spec=client.V1IngressSpec(
                rules=[client.V1IngressRule(
                    host=hostname,
                    http=client.V1HTTPIngressRuleValue(
                        paths=[client.V1HTTPIngressPath(
                            path="/",
                            path_type="Prefix",
                            backend=client.V1IngressBackend(
                               service = client.V1IngressServiceBackend(
                                            port=client.V1ServiceBackendPort(number=service_port),
                                            name=deployment+"-"+user_id)
                               )
                        )]
                    )
                )]
            )
        )
        # Creation of the Deployment in specified namespace
        # (Can replace "default" with a namespace you may have created)
        networking_v1_api.create_namespaced_ingress(
            namespace=namespace,
            body=body
        )
        return None
    except Exception as ex:
        print('Error creating ingress:', ex, file=stderr)
        log.error(ex)
        return 'Failed to create ingress!'

channel.basic_qos(prefetch_count=1)
channel.basic_consume(queue='deployment_qeue', on_message_callback=on_request)

print(" [x] Awaiting RPC requests")
channel.start_consuming()
