# Local deployment

You will need to install minikube by following the instructions on https://kubernetes.io/docs/tasks/tools/install-minikube/
Then you will need to enable minikube's Ingress addon by running

```
minikube addons enable ingress
```
Then you can deploy skf to your minikube instance by running:

```
for yaml in Docker/alpine-cloud/k8s/*.yaml; do
    kubectl apply -f $yaml;
done
```
By default the ingress listens for requests at `host.local` you will need to map this to minikube's ip.
You can find minikube's ip by running
```
minikube ip
```

Last step is to add this entry to your /etc/hosts
You can do so by running:
```
sudo echo host.local $(minikube ip) >> /etc/hosts
```
If kubectl shows two pods named skf-flask-front and skf-flask-back up and running then you can access SKF by browsing to
http://host.local



== Production ==

You will need to modify the Ingress to include certificate.
Furthermore you need to change the ingress  host to match your domain.
Last, you will need to edit configmaps.yaml to change the FRONTENT_URL value to point to where your domain is.

# GKE deployment
## Prep

1. Clone the repo and edit configmaps.yaml FRONTEND_URI, SKF_API_URL and JWT_SECRET.
2. Make sure kubectl and gcloud are in the right place e.g. `kubectl config current-context`
3. Deploy stuff:

```
for yaml in ~/skf-flask/Docker/alpine-cloud/k8s/*.yaml; do
    kubectl apply -f $yaml;
done
```

4. Init tiller

```
helm init --service-account tiller
```

5. Get a cert e.g. a Lets Encrypt cert locally using something like:

```
certbot -d skf-k8s.vuln-tracker.dev --manual --preferred-challenges dns certonly
kubectl create secret tls skf-k8s.vuln-tracker.dev --key privkey.pem --cert cert.pem
```

OR

deploy [Cert-Manager|https://cert-manager.io/docs/installation/kubernetes/] using helm

6. Deploy an nginx ingress controller:

```
helm install --name nginx-ingress stable/nginx-ingress --set rbac.create=true --set controller.publishService.enabled=true --set controller.service.externalTrafficPolicy=Local
```

7. Suss out your IP and do your DNS stuff `kubectl get ingress`.
