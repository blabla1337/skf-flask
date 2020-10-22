# Kubernetes configmaps.yaml 

Before we can deploy SKF application in a K8s platform we need to modify the configmaps.yaml
Below are the important variables to be changed and explained:

```
  # The secret used for the signature creation of the JWT token, make it secure random value
  SKF_JWT_SECRET: please_change_this_value_to_be_random
```
```
  # This is the URL location of the API, this value will be used in the Angular SKF application to send the request to
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
  # Ideally you create 2 DNS entries, one for the main SKF website and one for the SKF Labs
  SKF_LABS_DOMAIN: "http://beta-labs.securityknowledgeframework.org"
```
```
  # Ideally you create 2 DNS entries, one for the main SKF website and one for the SKF Labs
  # Location of the Angular application
  FRONTEND_URI: https://beta.securityknowledgeframework.org
```
```
  # Below is the variable where we place the base64 string of our .kube config file
  # file for example: cat ~/.kube/config | base64
  LABS_KUBE_CONF: HV1c5WWR6aGpWQ3RzVjFsSWFYcEhlQW81UkUxYU9ITnlZbWg0UkdK...a3RMUzB0TFFvPQ==
```

We also need to modify the ingress.yaml
Below are the important variables to be changed and explained:

The below DNS name will be used to access the SKF application, please change it to your hostname and the same ones you used in the configmaps.yaml file.

```
  - hosts:
    - beta.securityknowledgeframework.org
    secretName: beta.securityknowledgeframework.org
  rules:
  - host: beta.securityknowledgeframework.org
```

== Production ==

You will need to modify the Ingress to include certificate.
Furthermore you need to change the ingress  host to match your domain.

# GKE example deployment SKF app
## Prep SKF Labs env

1. Create a Kubernetes cluster, this will be used for the SKF Labs, we dont want them in the SKF k8s cluster as these labs are vulnerable by design
2. Make sure kubectl and gcloud are in the right place e.g. `kubectl config current-context`
3. Init tiller

Maybe not needed depending if you use helm2 or helm3
```
# For helm2 use the command below
helm init --service-account tiller
```

4. Deploy an nginx ingress controller:

```
helm install --name nginx-ingress stable/nginx-ingress --set rbac.create=true --set controller.publishService.enabled=true --set controller.service.externalTrafficPolicy=Local
OR with helm3:
helm install nginx-ingress stable/nginx-ingress --set rbac.create=true --set controller.publishService.enabled=true --set controller.service.externalTrafficPolicy=Local
```

5. Check out your IP and do your DNS stuff `kubectl get ingress`
Add the IP of the ingress controller to your DNS records
beta-labs.securityknowledgeframework.org 213.219.179.111

6. Grab the ~/.kube/config file of this SKF Labs k8s cluster and convert to base64 string, we need to set it in the configmaps.yaml

## Prep SKF env

1. Clone the repo and edit configmaps.yaml as mentioned in the above text 
2. Create a second Kubernetes cluster, this will be used for the SKF application
3. Make sure kubectl and gcloud are in the right place e.g. `kubectl config current-context`
4. Deploy all the stuff, to the SKF k8s cluster:

```
cd skf-flask
for yaml in Docker/alpine-cloud/k8s/*.yaml; do
    kubectl apply -f $yaml;
done
```

5. Init tiller

Maybe not needed depending if you use helm2 or helm3
```
# For helm2 use the command below
helm init --service-account tiller
```

6. Get a cert e.g. a Lets Encrypt cert locally using something like:

```
certbot -d beta.securityknowledgeframework.org --manual --preferred-challenges dns certonly
kubectl create secret tls beta.securityknowledgeframework.org --key privkey.pem --cert cert.pem
```
OR
deploy [Cert-Manager|https://cert-manager.io/docs/installation/kubernetes/] using helm

7. Deploy an nginx ingress controller:

```
helm install --name nginx-ingress stable/nginx-ingress --set rbac.create=true --set controller.publishService.enabled=true --set controller.service.externalTrafficPolicy=Local
OR with helm3:
helm install nginx-ingress stable/nginx-ingress --set rbac.create=true --set controller.publishService.enabled=true --set controller.service.externalTrafficPolicy=Local
```

8. Check out your IP and do your DNS stuff `kubectl get ingress`
Add the IP of the ingress controller to your DNS records
beta.securityknowledgeframework.org 213.219.179.222

Now visit your website, for example: https://beta.securityknowledgeframework.org
