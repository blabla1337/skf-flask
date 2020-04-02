## Local / dedicated server install

Local installation based on Ubuntu 16.04.

### Requirements:
- If you have `ng-common` and `ng-latin` on your system then remove them
    + `sudo apt purge ng-common ng-latin`
- nginx
    + `sudo apt install nginx`
- npm
    + `sudo apt install npm`
- ng
    + `sudo npm install -g @angular/cli`
- git
    + `sudo apt install git`
- latest version of node ():
```
    * sudo npm install n -g
    * sudo n 8.9
    * sudo ln -s  /usr/bin/nodejs /usr/bin/node
```

- python3.6, pip3.6 (https://stackoverflow.com/questions/42662104/how-to-install-pip-for-python-3-6-on-ubuntu-16-10):
```
    * sudo add-apt-repository ppa:jonathonf/python-3.6  # (only for 16.04 LTS)
    * sudo apt update
    * sudo apt install python3.6
    * wget https://bootstrap.pypa.io/get-pip.py
    * sudo python3.6 get-pip.py
```

### Installation SKF and configuration:

* __Clone repository and install dependencies__

```
cd /tmp; git clone git://github.com/blabla1337/skf-flask.git
cd /tmp/skf-flask; sudo pip3.6 install -r requirements.txt
cd /tmp/skf-flask/Angular; npm install
cd /tmp/skf-flask/Angular; ng build --aot --configuration=production
```

* __Configure nginx__

```
sudo rm /etc/nginx/sites-enabled/default
sudo cp /tmp/skf-flask/installations/local/site-tls.conf /etc/nginx/sites-enabled/default
```

* `mv /tmp/skf-flask /`

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

```bash
openssl req -nodes -newkey rsa:4096 -keyout /skf-flask/server.key -out /skf-flask/server.csr  -subj "/CN=OWASP-SKF"
```

```bash
openssl x509 -req -days 365 -in /skf-flask/server.csr  -signkey /skf-flask/server.key -out /skf-flask/server.pem
```

* __Start nginx__

```bash
service restart nginx
```
or if you use `systemctl`

```bash
systemctl start nginx.service
```


### Run SKF (with terminal in Local folder):

```
cd /skf-flask/installations/local; bash wrapper.sh
```

Navigate to https://your_domain_value_you_used_above_commands

You can also run API and Frontend part separately for __development__ process. To do so run the following commands:

* In one terminal window run: `./skf-api.sh`
* In another terminal window run : `./skf-angular.sh development`

#### Error:

If you get the following error

```
nginx: [emerg] a duplicate default server for 0.0.0.0:80 in /etc/nginx/sites-enabled/default:17
```

If you are not using that file just remove it: (```sudo rm /etc/nginx/sites-enabled/default```)
