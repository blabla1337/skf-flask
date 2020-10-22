## Local / dedicated server install

<<<<<<< HEAD
Local installation based on Ubuntu 20.04. and its possible but we do recommend to install it on a K8s Cluster as its easier and more stable.

### Requirements:
=======
Local installation based on Ubuntu 16.04.

### Requirements:
- If you have `ng-common` and `ng-latin` on your system then remove them
    + `sudo apt purge ng-common ng-latin`
>>>>>>> origin/master
- nginx
    + `sudo apt install nginx`
- npm
    + `sudo apt install npm`
- ng
    + `sudo npm install -g @angular/cli`
- git
    + `sudo apt install git`
<<<<<<< HEAD
- curl
    + `sudo apt install curl`

=======
- latest version of node ():
```
    * sudo npm install n -g
    * sudo n 12.18 #or higher version
    * sudo ln -s  /usr/bin/nodejs /usr/bin/node
```

- python3.6, pip3.6 (https://askubuntu.com/questions/865554/how-do-i-install-python-3-6-using-apt-get):
```
    * sudo add-apt-repository ppa:deadsnakes/ppa
    * sudo apt-get update
    * sudo apt-get install python3.6
    * wget https://bootstrap.pypa.io/get-pip.py
    * sudo python3.6 get-pip.py
```
>>>>>>> origin/master

### Installation SKF and configuration:

* __Clone repository and install dependencies__

```
<<<<<<< HEAD
cd /tmp; git clone git://github.com/blabla1337/skf-flask.git 
cd /tmp/skf-flask; sudo pip3 install -r requirements.txt
cd /tmp/skf-flask/Angular2; npm install
cd /tmp/skf-flask/Angular2; ng build --aot 
=======
cd /tmp; git clone git://github.com/blabla1337/skf-flask.git
cd /tmp/skf-flask; sudo pip3.6 install -r requirements.txt
cd /tmp/skf-flask/Angular; npm install
cd /tmp/skf-flask/Angular; ng build --aot --configuration=production
>>>>>>> origin/master
```

* __Configure nginx__

```
sudo rm /etc/nginx/sites-enabled/default
sudo cp /tmp/skf-flask/installations/local/site-tls.conf /etc/nginx/sites-enabled/default
<<<<<<< HEAD
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
=======
```

* `mv /tmp/skf-flask /`
>>>>>>> origin/master

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

<<<<<<< HEAD
Put your own certificate files in the /skf-flask dir and name them like below
OR if you want self signed (dunno why but hey i dont judge) do the steps below

=======
>>>>>>> origin/master
```bash
openssl req -nodes -newkey rsa:4096 -keyout /skf-flask/server.key -out /skf-flask/server.csr  -subj "/CN=OWASP-SKF"
```

```bash
openssl x509 -req -days 365 -in /skf-flask/server.csr  -signkey /skf-flask/server.key -out /skf-flask/server.pem
```

* __Start nginx__

```bash
<<<<<<< HEAD
sudo systemctl restart nginx
=======
service restart nginx
```
or if you use `systemctl`

```bash
systemctl start nginx.service
>>>>>>> origin/master
```


### Run SKF (with terminal in Local folder):

```
cd /skf-flask/installations/local; bash wrapper.sh
```

Navigate to https://your_domain_value_you_used_above_commands

<<<<<<< HEAD
=======
You can also run API and Frontend part separately for __development__ process. To do so run the following commands:

* In one terminal window run: `./skf-api.sh`
* In another terminal window run : `./skf-angular.sh development`

>>>>>>> origin/master
#### Error:

If you get the following error

```
nginx: [emerg] a duplicate default server for 0.0.0.0:80 in /etc/nginx/sites-enabled/default:17
```

If you are not using that file just remove it: (```sudo rm /etc/nginx/sites-enabled/default```)
