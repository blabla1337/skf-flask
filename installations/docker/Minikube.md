### Local minikube installation

For Linux users that want to deploy a local Kubernetes instance, they might want to install [minikube](https://minikube.sigs.k8s.io/docs/start/). 
Once installed, we can start the minikube with the following command:

```
minikube start --embed-certs=true
```
The above command, will initialize and start minikube service (it might take few minutes). Also, it will embed the required certificates and keys within the ~./kube/config file.

Once done, check that minikube is running properly:

```
owasp@owasp-virtual-machine:~$ minikube status
minikube
type: Control Plane
host: Running
kubelet: Running
apiserver: Running
kubeconfig: Configured
```

Then we need to change the docker-compose.yaml file. 
First we need to get the base64 encode of the ~./kube/config file:

```
cat ~./kube/config | base64 | tr -d '\n'
```

Copy the output of the above command and set it as value for the ```LABS_KUBE_CONF``` variable:

```
# docker-compose.yaml
...
LABS_KUBE_CONF: HV1c5WWR6aGpWQ3RzVjFsSWFYcEhlQW81UkUxYU9ITnlZbWg0UkdK...a3RMUzB0TFFvPQ==
...
```

Since it might be possible to get file ownership issues, it's also suggested to set the absolute path for the ```volumes``` attribute, within the skf-api configuration section:

```
# docker-compose.yaml
...
...
skf-api:
    container_name: skf-api_container
    depends_on:
      - "rabbitmq"
      - "nginx"
      - "mysql"
    restart: always
    volumes:
      - /home/your_username/.kube/config:/home/user_api/.kube/config
...
...
```

We also need to change the value for the ```SKF_LABS_DOMAIN``` (localhost by default), with the minikube IP address (or with a hostname that resolves to the same IP) that you can find looking at  ~./kube/config (by default should be 192.168.49.2):

```
# ~./kube/config
apiVersion: v1
clusters:
- cluster:
    certificate-authority-data: base64_data_encoded
    extensions:
    - extension:
        last-update: Wed, 10 Nov 2021 17:46:33 CET
        provider: minikube.sigs.k8s.io
        version: v1.24.0
      name: cluster_info
    server: https://192.168.49.2:8443
  name: minikube
contexts:
- context:
...
...
```
```
# docker-compose.yaml
...
SKF_LABS_DOMAIN=http://192.168.49.2
...
```

At this point we could start the skf application (within the skf-flask directory) with:

```
docker-compose up
```
Observe the output logs:
it might be possible that the skf-api_container container will fail to 'touch' the /home/user_api/.kube/config, due to file permission issues (it has to do with how docker handles file ownership).
If you see such an error, connect as root to the skf-api_container:
```
docker exec -it -u0 skf-api_container /bin/bash
```
and change the /home/user_api/.kube/config permission as follow:
```
chmod 666 /home/user_api/.kube/config
```
We almost done, but we need to fix the last thing: when we started minikube, a new (separate) bridge network has been created and because of containers isolation (for more information check this [page](https://docs.docker.com/network/iptables/)), it won't be possible to get network communication between minikube and skf containers (as they will be in 2 different bridges).
So we need to add 2 custom rules to the ```DOCKER-USER``` chain in ```iptables``` to allow communication between the 2 bridges:
```
sudo iptables -I DOCKER-USER -i br-xxxxxxxxxxxx -o br-yyyyyyyyyyyy -j ACCEPT
sudo iptables -I DOCKER-USER -i br-yyyyyyyyyyyy -o br-xxxxxxxxxxxx -j ACCEPT
```
where ```br-xxxxxxxxxxxx``` and ```br-yyyyyyyyyyyy``` need to match the relevant bridge interfaces in your system (you can use ```brctl show``` to find them). Also, remember to make the iptabels rules persistent (i.e. using ```iptables-persistent```).

Finally you can run again:
```
docker-compose up
```

and you should be able to connect to the dashboard and deploy the labs.


