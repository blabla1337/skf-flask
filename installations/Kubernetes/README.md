# Deploying to Kubernetes

The `Docker/alpine-cloud/k8s` directory contains the yaml files you'll need to deploy SKF.

You'll need to change some of the values in these files, below is a brief overview of each file,
including pointers to the values you'll definitely want to change - but you may need to change more!

At the bottom of this document, there is a list of [example deployments to various cloud
providers](#Example-deployments-to-cloud-providers) - these are definitely worth a read.

## `configmaps.yaml`

General configuration values.

Below are the important variables to be changed and explained:

```
  # The secret used for the signature creation of the JWT token, make it secure random value
  SKF_JWT_SECRET: please_change_this_value_to_be_random
```
```
  # This is the URL location of the API, this value will be used in the Angular SKF application to
  # send the request to
  SKF_API_URL: "https://beta.securityknowledgeframework.org/api"
```
```
  # Issues with the API? you can set to True to have more console output, only use in non Prod env!
  SKF_FLASK_DEBUG: "False"
```
```
  # SKF Database supports sqlite or mysql
  SKF_DB_URL: mysql+pymysql://root:admin-skf-secret@mysql/skf?charset=utf8mb4
```
```
  # When launching the Labs below URL will be used.
  # Ideally you create 2 DNS entries, one for the main SKF website and one for the SKF Labs.
  SKF_LABS_DOMAIN: "http://beta-labs.securityknowledgeframework.org"
```
```
  # By default, "port" mode deploys the lab as a NodePort service, on a random port on the
  # SKF_LABS_DOMAIN value.
  #
  # Setting the deploy mode to "subdomain" will create a new ingress rule for each lab, directing
  # a subdomain of SKF_LABS_DOMAIN to the lab. All subdomains should point to the clusters ingress
  # controller.
  SKF_LABS_DEPLOY_MODE: "port"
```
```
  # Ideally you create 2 DNS entries, one for the main SKF website and one for the SKF Labs.
  # Location of the Angular application.
  FRONTEND_URI: https://beta.securityknowledgeframework.org
```
```
  # Below is the variable where we place the base64 string of our .kube config file for the labs
  # cluster, for example the output of: cat ~/.kube/config | base64
  # IMPORTANT: This should only contain the config for the labs cluster!
  LABS_KUBE_CONF: HV1c5WWR6aGpWQ3RzVjFsSWFYcEhlQW81UkUxYU9ITnlZbWg0UkdK...a3RMUzB0TFFvPQ==
```
```
  # Below is the variable where we place the base64 string of our gsa-key.json file
  # file for example: cat gsa-key.json | base64
  GOOGLE_APPLICATION_CREDENTIALS: 35SAF3DFSFDSF3SFDSDF243SDSAGD34SDUkUxYU9ITnlZbWg0UkdK...a3RMUzB0TFFvPQ==
```

## `Deployment_backend.yaml`

SKF Api service and deployment. All the variables are in `configmap.yaml`.

You may wish to update the version of the container image. Make sure the version is updated for all
services though!

## `hpa_mam.yaml`

Horizontal auto-scaling for the API server. You might want to change the `minReplicas` and
`maxReplicas` values.

## `Deployment_mysql.yaml`

MySQL service, persistent volume claim and deployment. Authentication variables are set in
`configmaps.yaml` and also used by `Deployment_backend.yaml`. The persistent volume requests 8GiB by
default.

If you're deploying to a cloud provider, you might want to use their database service instead and
not deploy this. The database URL is set in `configmaps.yaml`.

If this is used, make sure you back up the persistent volume!

## `Deployment_rabbitmq.yaml`

RabbitMQ service and deployment. Authentication variables are set in `configmaps.yaml` and also used
by `Deployment_backend.yaml`.

## `Deployment_frontend.yaml`

SKF frontend service and deployment - this serves the static angular site using NGINX.

As with `Deployment_backend.yaml`, all the variables are in `configmap.yaml`. You may wish to update
the version of the container image - if you do, make sure to also update the version in
`Deployment_backend.yaml`!

## `ingress.yaml`

Ingress to the frontend service.

Below are the important variables to be changed and explained:

The below DNS name will be used to access the SKF application, please change it to your hostname and
the same ones you used in the configmaps.yaml file.

```
  - hosts:
    - beta.securityknowledgeframework.org
    secretName: beta.securityknowledgeframework.org
  rules:
  - host: beta.securityknowledgeframework.org
```

== Production ==

You will need to modify the Ingress to include certificate, this could be done using Let's Encrypt
manually, or automatically using
[Cert-Manager](https://cert-manager.io/docs/installation/kubernetes/).

Furthermore you need to change the ingress host to match your domain.

# Example deployments to cloud providers

We currently have guides for:
- [Google Kubernetes Engine (GKE)](GCP.md)
- [Azure Kubernetes Service (AKS)](Azure.md)

Please contribute a guide if you're deploying to another service!
