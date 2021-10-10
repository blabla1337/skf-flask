# Deploying AKF on Google GKE

## Prep SKF Labs Cluster

1. Create a Kubernetes cluster, this will be used for the SKF Labs, we don't want them in the SKF
   k8s cluster as these labs are vulnerable by design.

2. Make sure kubectl and gcloud are in the right place e.g. `kubectl config current-context`.

3. Create user for controlling the skf-labs cluster
```
gcloud iam service-accounts create labs-user

gcloud projects add-iam-policy-binding replace_with_your_project_name_in_gke \
    --member=serviceAccount:labs-user@replace_with_your_project_name_in_gke.iam.gserviceaccount.com \
    --role=roles/container.developer

 gcloud iam service-accounts keys create gsa-key.json \
    --iam-account=labs-user@replace_with_your_project_name_in_gke.iam.gserviceaccount.com
```

4. Now we need to create a base64 string from the gsa-key.json
```
cat gsa-key.json | base64
```
Now paste the output value in the `configmaps.yaml` file in `GOOGLE_APPLICATION_CREDENTIALS`

5. Also we need the google kube config file of the skf-labs cluster
```
gcloud container clusters get-credentials skf-labs -z europe-west4
```
Make sure you only have the kube config content of the skf-labs cluster and not others.

6. Now we need to create a base64 string from the skf-labs .kube/config file
```
cat ~/.kube/config | base64
```
Now paste the output value in the `configmaps.yaml` file in `LABS_KUBE_CONF`

<ol start="7"><li>

### Port Deploy Mode: Add firewall rule

The final step is to get the IP of the skf-labs pods in the VM instance overview
https://console.cloud.google.com/compute/instances and add the IP to the DNS for the labs domain.
Now, in `configmaps.yaml`, set the value of `SKF_LABS_DOMAIN` to this domain.

Finally, add the firewall rule to allow the Labs being exposed on the Pods and reachable:
```
gcloud compute --project=replace_with_your_project_name_in_gke \
    firewall-rules create allow-labs \
    --direction=INGRESS \
    --priority=1000 \
    --network=default \
    --action=ALLOW \
    --rules=tcp:10000-65000 \
    --source-ranges=0.0.0.0/0
```

### Subdomain Deploy Mode: Install ingress controller

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

After the ingress has an IP address (this might be found using `kubectl get ingress`), you'll need
to add a wildcard DNS record - pointing all subdomains of your labs domain to the ingress
controller.

Now, in `configmaps.yaml`, set the value of `SKF_LABS_DOMAIN` to this domain (the one with the
wildcard record).

</li></ol>

## Prep Main SKF Cluster

1. Clone the repo and edit `configmaps.yaml` and other yaml files as described [here](README.md),
   including the labs kube config from above.
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

8. Check out your IP and do your DNS stuff `kubectl get ingress`

Add the IP of the ingress controller to your DNS records, setting the frontend domain (the domain in
`FRONTEND_URI`).

Now visit your website, for example: https://beta.securityknowledgeframework.org
