# Raspberry pi K8s Cluster

You need to build the hardware and cluster using the great project of Lucas Teligioridis:
https://github.com/blabla1337/raspbernetes

Also see his blog post about more in depth explanation:
https://itnext.io/headless-kubernetes-on-15-raspberry-pis-boot-in-under-8-minutes-808402ea2348

Remark:
All the docker images are ARM7 based, adding other images to it is fine but remember it needs to be available for ARM as well.
This setup is only for accessing it internally in the network, for public access change the externalIP value and update the skf.local string to reflect the DNS name.

After you have it all working and the Master and Workers are installed and configured correclty we can start deploying the OWASP-SKF:

## Prep

1. Update the fields accordingly and apply the k8s yaml files to your Pi K8s cluster
```
for yaml in Docker/alpine-cloud/k8s/*.yaml; do
    kubectl apply -f $yaml;
done
```

2. Install the nginx-ingress-controller
```
helm install nginx-ingress stable/nginx-ingress  \
    --set controller.image.repository=quay.io/kubernetes-ingress-controller/nginx-ingress-controller-arm \
    --set controller.image.tag=0.32.0 \
    --set defaultBackend.enabled=false \
    --set controller.publishService.enabled=true \
    --set controller.service.externalTrafficPolicy=Local 
```

3. Determine where the SKF app is running based on the IP's used for the Workers, in my case 192.168.0.161-163
```
kubectl get service -o wide
NAME                       TYPE           CLUSTER-IP       EXTERNAL-IP     PORT(S)                      AGE   SELECTOR
kubernetes                 ClusterIP      10.96.0.1        <none>          443/TCP                      7d    <none>
nginx-ingress-controller   LoadBalancer   10.111.86.168    192.168.0.163   80:31863/TCP,443:32685/TCP   26h   app.kubernetes.io/component=controller,app=nginx-ingress,release=nginx-ingress
rabbitmq                   ClusterIP      10.111.190.81    <none>          5672/TCP                     2d    app.kubernetes.io/instance=rabbitmq,app.kubernetes.io/name=rabbitmq
skf-flask-back             NodePort       10.108.106.194   <none>          8888:30936/TCP               2d    app.kubernetes.io/instance=skf-flask-back,app.kubernetes.io/name=skf-flask-back
skf-flask-front            NodePort       10.103.174.11    <none>          8788:30615/TCP               2d    app.kubernetes.io/instance=skf-flask-front,app.kubernetes.io/name=skf-flask-front

Go to the browser and find the IP: http://192.168.0.163:30615
You should see the SKF Angular website
```

4. Modify the config of the nginx-ingress-controller
```
kubectl get svc nginx-ingress-controller -o yaml > nginx-service.yaml 
and comment the following parts:
clusterIP: ...
  type: LoadBalancer
status:
  loadBalancer: {}

and add the below part to the port tree
  # The app is running on my worker3 that has the IP 192.168.0.163
  externalIPs:
    - 192.168.0.163

And apply the changes:
kubectl apply -f nginx-service.yaml 
```

5. Add IP to your DNS
Last step is to add the public IP of the DNS and in our case i used beta.securityknowledgeframework.org 
By default the ingress listens for requests at `skf.local` you will need to change this to the domain name that will run the SKF instance.

6. Get a cert e.g. a Lets Encrypt cert locally using something like:
```
certbot -d beta.securityknowledgeframework.org --manual --preferred-challenges dns certonly
kubectl create secret tls beta.securityknowledgeframework.org --key privkey.pem --cert cert.pem
```
OR
deploy [Cert-Manager|https://cert-manager.io/docs/installation/kubernetes/] using helm

Now open the browser and go to:
https://beta.securityknowledgeframework.org

