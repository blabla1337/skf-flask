# Deploying SKF on Amazon Web Services EKS

## Prep SKF Labs Cluster

1. Create a Kubernetes cluster, this will be used solely for the SKF Labs, we don't want them in the SKF k8s cluster as these labs are vulnerable by design.
```
AWS_REGION=eu-central-1
CLUSTER_NAME=SKF-Labs
SKF_CONFIG=/Users/$USER/.kube/skf-labs/config

eksctl create cluster -n $CLUSTER_NAME --version 1.21 -r $AWS_REGION --fargate --kubeconfig $SKF_CONFIG
```

2. Check your config with `kubectl --kubeconfig=$SKF_CONFIG config current-context` and make sure you only have the kube config content of the skf-labs cluster and not others.

Then you can check the cluster creation was successful with `kubectl --kubeconfig=$SKF_CONFIG get svc`, and you should see an output similar to:
```
> kubectl --kubeconfig=$SKF_CONFIG get svc
NAME         TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)   AGE
kubernetes   ClusterIP   10.100.0.1   <none>        443/TCP   37m
```

This response means that the cluster is running and that you are able to communicate with the Kubernetes API.

###  Create a Kubernetes Service Account with a ClusterRole to allow deployment of labs to this cluster
In order for our Main Site backend to be able to deploy labs to this isolated cluster, we will prepare a Kubernetes Service Account with the necessary permissions to manage this SKF Labs cluster.

1. First we will create our service account:
```
SA_NAME=skf-labs-deployer
kubectl --kubeconfig=$SKF_CONFIG create sa $SA_NAME
```

2. And then bind the cluster admin role to the service account so that it can manage our SKF Labs cluster:
```
kubectl --kubeconfig=$SKF_CONFIG create clusterrolebinding "$SA_NAME"-rolebindingClusterAdmin --clusterrole=cluster-admin --serviceaccount=default:$SA_NAME
```

3. Finally we export keys for serviceaccount:
```
SECRET_NAME=$(kubectl --kubeconfig=$SKF_CONFIG get sa skf-labs-deployer -o json | jq -r '.secrets[0].name')
TOKEN=$(kubectl --kubeconfig=$SKF_CONFIG get secret $SECRET_NAME -o json | jq -r '.data.token')
DECODED_TOKEN=$(echo -n $TOKEN | base64 -d)
```

We will need the DECODED_TOKEN variable later, to allow SKF cluster to authenticate with our new service account.

### Deploy nginx ingress controller

With Nginx Ingress Controller, we can have multiple ingress objects for multiple environments or namespaces with the same network load balancer.

However, although we want to use Fargate for simplicity and reduce cost of the labs we deploy, we can't deploy the Nginx Ingress controller to fargate. This is because Fargate has several limitations:
- There is a maximum of 4 vCPU and 30Gb memory per pod.
- Currently there is no support for stateful workloads that require persistent volumes or file systems.
- You cannot run Daemonsets, Privileged pods, or pods that use HostNetwork or HostPort.
- The only load balancer you can use is an Application Load Balancer.

If we try to deploy Nginx ingress controller to fargate, it will need a privileged pod but according to the third limitation above we can't, so we'll get the following error:
`Pod not supported on Fargate: invalid SecurityContext fields: AllowPrivilegeEscalation`

However, we can run Nginx ingress contoller on EKS managed nodes and the rest of our workload can be run on Fargate nodes, commonly referred to as a Hybrid Cluster.

#### Create a Managed Nodegroup

1. To create a managed nodegroup with 1 Node to deploy our nginx controller, we can execute:
`eksctl create nodegroup --cluster $CLUSTER_NAME -r $AWS_REGION --managed -N 1 -n nginx-nodegroup -t t3.large`

#### Deploy Nginx Ingress Controller

2. To deploy Nginx Ingress Controller to our new node, we just simply have to apply the latest Nginx-Ingress-Controller deployment for AWS:
`kubectl --kubeconfig=$SKF_CONFIG apply -f https://raw.githubusercontent.com/kubernetes/ingress-nginx/main/deploy/static/provider/aws/1.21/deploy.yaml`

And if all resources (services, roles, clusterbindings, ingresses, etc) were created successfully, we should be able to watch our pods for the nginx namespace:
`kubectl --kubeconfig=$SKF_CONFIG get po -o wide -n ingress-nginx -w`

And wait until we see the controller is running under our managed node (1/1):
```
NAME                                        READY   STATUS      RESTARTS   AGE   IP               NODE                                              NOMINATED NODE   READINESS GATES
ingress-nginx-admission-create--1-rnkc2     0/1     Completed   0          26s   192.168.56.156   ip-192-168-33-166.eu-central-1.compute.internal   <none>           <none>
ingress-nginx-admission-patch--1-mp6g4      0/1     Completed   0          26s   192.168.40.59    ip-192-168-33-166.eu-central-1.compute.internal   <none>           <none>
ingress-nginx-controller-5756658855-dtkvv   1/1     Running     0          26s   192.168.41.233   ip-192-168-33-166.eu-central-1.compute.internal   <none>           <none>
```

3. After the service has an IP address (this might be found using `kubectl --kubeconfig=$SKF_CONFIG --namespace ingress-nginx get services -o wide ingress-nginx-controller` or going to the AWS EKS Portal and select the 'Services and networking/Services' pane under the 'Resources' tab and taking the value from the "hostname" field and the bottom of the Raw view), you'll need to add a wildcard DNS record - pointing all subdomains of your labs domain to the ingress controller IP.


### Setting SKF Labs environment variables
Now that we have our infrastructure ready for SKF Labs, we have to set all our environment variables.

1. We need to modify our config file in order to authenticate via our newly created. 
First we'll create a copy for it:
```
cp $SKF_CONFIG skf-labs.config
```
And then, leaving our certificate ($ca) and Server API URLs ($server_api-url) unmodified, edit it to follow the following format:
```
apiVersion: v1
clusters:
- cluster:
    certificate-authority-data: $ca
    server: $server_api-url
  name: $CLUSTER_NAME.$AWS_REGION.eksctl.io
contexts:
- context:
    cluster: $CLUSTER_NAME.$AWS_REGION.eksctl.io
    user: $SA_NAME@$CLUSTER_NAME.$AWS_REGION.eksctl.io
  name: $SA_NAME@$CLUSTER_NAME.$AWS_REGION.eksctl.io
current-context: $SA_NAME@$CLUSTER_NAME.$AWS_REGION.eksctl.io
kind: Config
preferences: {}
users:
- name: $SA_NAME@$CLUSTER_NAME.$AWS_REGION.eksctl.io
  user:
    token: $DECODED_TOKEN
```


2. Then, we can export it to base64 string:
```
cat skf-labs.config | base64
```
And paste the output value in the `configmaps.yaml` file under `skf` in `LABS_KUBE_CONF`

3. For AWS, we will only describe how to set up the subdomain deployment mode, so in `configmaps.yaml`, also set `SKF_LABS_DEPLOY_MODE` to `subdomain`.

4. Finally, in `configmaps.yaml`, set the value of `SKF_LABS_DOMAIN` to the domain ADDRESS of our ingress (the one with the wildcard record).


---------


## Prep Main SKF Cluster

1. Create a second Kubernetes cluster, this will be used for the SKF application
```
AWS_REGION=eu-central-1
CLUSTER_NAME=SKF
SKF_CONFIG=/Users/$USER/.kube/skf/config

eksctl create cluster -n $CLUSTER_NAME --version 1.21 -r $AWS_REGION --fargate --kubeconfig $SKF_CONFIG
```

2. Check your config with `kubectl --kubeconfig=$SKF_CONFIG config current-context` and make sure you only have the kube config content of the skf-labs cluster and not others.

Then you can check the cluster creation was successful with `kubectl --kubeconfig=$SKF_CONFIG get svc`, and you should see an output similar to:
```
> kubectl --kubeconfig=$SKF_CONFIG get svc
NAME         TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)   AGE
kubernetes   ClusterIP   10.100.0.1   <none>        443/TCP   37m
```

This response means that the cluster is running and that you are able to communicate with the Kubernetes API.

### Deploy nginx ingress controller

#### Create a Managed Nodegroup

1. To create a managed nodegroup with 1 Node to deploy our nginx ingress controller, we can execute:
`eksctl create nodegroup --cluster $CLUSTER_NAME -r $AWS_REGION --managed -N 1 -n nginx-nodegroup -t t3.large`

#### Deploy Nginx Ingress Controller

2. To deploy Nginx Ingress Controller to our new node, we just simply have to apply the latest Nginx-Ingress-Controller deployment for AWS:
`kubectl --kubeconfig=$SKF_CONFIG apply -f https://raw.githubusercontent.com/kubernetes/ingress-nginx/main/deploy/static/provider/aws/1.21/deploy.yaml`

And if all resources (services, roles, clusterbindings, ingresses, etc) were created successfully, we should be able to watch our pods for the nginx namespace:
`kubectl --kubeconfig=$SKF_CONFIG get po -o wide -n ingress-nginx -w`

And wait until we see the controller is running under our managed node (1/1):
```
NAME                                        READY   STATUS      RESTARTS   AGE   IP               NODE                                              NOMINATED NODE   READINESS GATES
ingress-nginx-admission-create--1-rnkc2     0/1     Completed   0          26s   192.168.56.156   ip-192-168-33-166.eu-central-1.compute.internal   <none>           <none>
ingress-nginx-admission-patch--1-mp6g4      0/1     Completed   0          26s   192.168.40.59    ip-192-168-33-166.eu-central-1.compute.internal   <none>           <none>
ingress-nginx-controller-5756658855-dtkvv   1/1     Running     0          26s   192.168.41.233   ip-192-168-33-166.eu-central-1.compute.internal   <none>           <none>
```

3. After the service has an IP address (this might be found using `kubectl --kubeconfig=$SKF_CONFIG --namespace ingress-nginx get services -o wide ingress-nginx-controller` or going to the AWS EKS Portal and select the 'Services and networking/Services' pane under the 'Resources' tab and taking the value from the "hostname" field and the bottom of the Raw view), you'll need to add a wildcard DNS record - pointing all subdomains of your labs domain to the ingress controller IP.

### Setting final variables of Main SKF cluster

1. Now edit `configmaps.yaml` again to add the FRONTEND_URI and API_URI and other yaml files as described [here](README.md).

2. If we've chosen to deploy with a MySQL instead of an SQLite, as our MySQL deployment needs a PVC (Persistent Volume Claim), we'd need to install [Amazon's EFS CSI driver](https://docs.aws.amazon.com/eks/latest/userguide/efs-csi.html) to be able to deploy it successfully to Fargate.
As we already have a nodegroup for our Nginx Ingress Controller, it is much easier to set the mysql in a different namespace than default so that it deploys within our EC2 nodegroup.

In order to make SKF Backend able to connect to our different namespace, make sure your SKF_DB_URL specifies the [Kubernetes DNS name](https://kubernetes.io/docs/concepts/services-networking/dns-pod-service/) of our service, by specifying the namespace with the following format:
`mysql+pymysql://{USER}:{PASSWORD}@{SERVICE}.{NAMESPACE}.svc.cluster.local/{DATABASE}?charset=utf8mb4` 

So it looks similar to:
`mysql+pymysql://root:admin-skf-secret@mysql.mysql.svc.cluster.local/skf?charset=utf8mb4`

3. Finally edit `ingress.yaml` to match our new host.


### Deploying the main application
1. Deploy all the stuff to the SKF k8s cluster:

```
for yaml in skf/*.yaml; do
    kubectl --kubeconfig=$SKF_CONFIG apply -f $yaml;
done
```

For a production deployment, you're probably better off using [Cert-Manager|https://cert-manager.io/docs/installation/kubernetes/] to keep your certificates up-to-date automatically.

Now visit your website, for example: https://beta.securityknowledgeframework.org
