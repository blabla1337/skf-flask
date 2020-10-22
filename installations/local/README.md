## Local / dedicated server install

Local installation based on Ubuntu 20.04. and its possible but we do recommend to install it on a K8s Cluster as its easier and more stable.

### Requirements:
- nginx
    + `sudo apt install nginx`
- npm
    + `sudo apt install npm`
- ng
    + `sudo npm install -g @angular/cli`
- git
    + `sudo apt install git`
- curl
    + `sudo apt install curl`


### Installation SKF and configuration:

* __Clone repository and install dependencies__

```
cd /tmp; git clone git://github.com/blabla1337/skf-flask.git 
cd /tmp/skf-flask; sudo pip3 install -r requirements.txt
cd /tmp/skf-flask/Angular2; npm install
cd /tmp/skf-flask/Angular2; ng build --aot 
```

* __Configure nginx__

```
sudo rm /etc/nginx/sites-enabled/default
sudo cp /tmp/skf-flask/installations/local/site-tls.conf /etc/nginx/sites-enabled/default
mv /tmp/skf-flask /
```

* __Configure & install RabbitMQ__

```
sudo echo "deb http://www.rabbitmq.com/debian/ testing main" >> /etc/apt/sources.list
sudo curl http://www.rabbitmq.com/rabbitmq-signing-key-public.asc | sudo apt-key add -
sudo apt-get update
sudo apt-get install rabbitmq-server
# To start the service:
service rabbitmq-server start
sudo rabbitmqctl add_user admin admin-skf-secret
sudo rabbitmqctl set_user_tags admin administrator
sudo rabbitmqctl set_permissions -p / admin ".*" ".*" ".*"
```

* __Configure kubernetes config file for Labs__

For also launching the labs from the SKF application we need to create a Kubernetes cluster in one of the platforms like Google.
When you created the cluster you need to place the kubernetes config file in the location ~/.kube/config of the machine you run the SKF app

```

#### Edit Settings

* __Change the JWT_SECRET value with below command__

```bash
perl -pi -e "s/JWT_SECRET = ''/JWT_SECRET = 'THIS_SHOULD_BE_CHANGED_AND_RANDOM'/" /skf-flask/skf/settings.py
```

* __Change the domain value with below command__

```bash
perl -pi -e "s/\*/https:\/\/demo.securityknowledgeframework.org/" /skf-flask/skf/settings.py
```

* __Change the domain value with below command__

```bash
perl -pi -e "s/http:\/\/127.0.0.1:8888\/api/https:\/\/demo.securityknowledgeframework.org\/api/" /skf-flask/Angular/src/environments/environment.prod.ts
```

* __Change the domain value with below command__

```bash
perl -pi -e "s/localhost/demo.securityknowledgeframework.org/" /skf-flask/installations/local/skf-angular.sh
```

* __Certificates stored in /skf-flask/ dir__

Put your own certificate files in the /skf-flask dir and name them like below
OR if you want self signed (dunno why but hey i dont judge) do the steps below

```bash
openssl req -nodes -newkey rsa:4096 -keyout /skf-flask/server.key -out /skf-flask/server.csr  -subj "/CN=OWASP-SKF"
```

```bash
openssl x509 -req -days 365 -in /skf-flask/server.csr  -signkey /skf-flask/server.key -out /skf-flask/server.pem
```

* __Start nginx__

```bash
sudo systemctl restart nginx
```


### Run SKF (with terminal in Local folder):

```
cd /skf-flask/installations/local; bash wrapper.sh
```

Navigate to https://your_domain_value_you_used_above_commands

#### Error:

If you get the following error

```
nginx: [emerg] a duplicate default server for 0.0.0.0:80 in /etc/nginx/sites-enabled/default:17
```

If you are not using that file just remove it: (```sudo rm /etc/nginx/sites-enabled/default```)
