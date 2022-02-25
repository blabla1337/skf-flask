# Deploying SKF on Azure AKS

## Prep SKF Labs Cluster

1. Create a Kubernetes cluster, this will be used for the SKF Labs, we don't want them in the SKF
   k8s cluster as these labs are vulnerable by design.

2. Now we need to create a base64 string from the skf-labs kube config file
```
az aks get-credentials \
    --resource-group <resource group> \
    --name <labs cluster name> \
    --admin \
    --file '-' | base64 -w 0
```
Now paste the output value in the `configmaps.yaml` file in `LABS_KUBE_CONF`

3. Configure kubectl to control our cluster:

```
az aks get-credentials \
    --resource-group <resource group> \
    --name <labs cluster name> \
    --admin
```

Check your config with `kubectl config current-context`.

Make sure you only have the kube config content of the skf-labs cluster and not others.

4. For Azure, we will only describe how to set up the subdomain deployment mode.

In `configmaps.yaml`, set `SKF_LABS_DEPLOY_MODE` to `subdomain`.

Now install the nginx ingress controller. With helm3, this can be installed using:
```
# If you haven't previously added the repo:
helm repo add ingress-nginx https://kubernetes.github.io/ingress-nginx
helm repo update

helm install ingress-nginx ingress-nginx/ingress-nginx \
    --set rbac.create=true \
    --set controller.publishService.enabled=true \
    --set controller.service.externalTrafficPolicy=Local \
    --set controller.setAsDefaultIngress=true
```
For helm2, the instructions are the same as below, for the main cluster.

5. After the ingress has an IP address (this might be found using `kubectl get ingress OR kubectl --namespace default get services -o wide -w ingress-nginx-controller`) or go to the Azure page and select 'Services & Ingress' and take the value from the ingress-nginx-controller External-IP , you'll
   need to add a wildcard DNS record - pointing all subdomains of your labs domain to the ingress
   controller IP.

Now, in `configmaps.yaml`, set the value of `SKF_LABS_DOMAIN` to this domain (the one with the
wildcard record).

## Prep Main SKF Cluster

1. Clone the repo and edit `configmaps.yaml` and other yaml files as described [here](README.md),
   including the labs kube config from above.
2. Create a second Kubernetes cluster, this will be used for the SKF application
3. Make sure kubectl is configured to control **only this cluster**

```
az aks get-credentials \
    --resource-group <resource group> \
    --name <labs cluster name> \
    --admin
```

Check everything with
```
kubectl config current-context
```

4. Deploy all the stuff to the SKF k8s cluster:

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

6. Get a certificate e.g. a Let's Encrypt cert locally using something like:

```
certbot -d beta.securityknowledgeframework.org --manual --preferred-challenges dns certonly
kubectl create secret tls beta.securityknowledgeframework.org --key privkey.pem --cert cert.pem
```

For a production deployment, you're probably better off using
[Cert-Manager|https://cert-manager.io/docs/installation/kubernetes/] to keep your certificates
up-to-date automatically.

7. Deploy an nginx ingress controller:

With helm2:
```
helm install --name nginx-ingress stable/nginx-ingress \
    --set rbac.create=true \
    --set controller.publishService.enabled=true \
    --set controller.service.externalTrafficPolicy=Local
```
With helm3:
```
# If you haven't previously added the repo:
helm repo add ingress-nginx https://kubernetes.github.io/ingress-nginx
helm repo update

helm install ingress-nginx ingress-nginx/ingress-nginx \
    --set rbac.create=true \
    --set controller.publishService.enabled=true \
    --set controller.service.externalTrafficPolicy=Local \
    --set controller.setAsDefaultIngress=true
```

8. Check out your IP and do your DNS stuff `kubectl get ingress OR kubectl --namespace default get services -o wide -w ingress-nginx-controller`

Add the IP of the ingress controller to your DNS records, setting the frontend domain (the domain in
`FRONTEND_URI`).

Now visit your website, for example: https://beta.securityknowledgeframework.org
