### Local / dedicated server install
Local installation based on Ubuntu 16.04.

#### Requirements:
- nginx (```sudo apt install nginx```)
- npm (```sudo apt install npm```)
- ng (```sudo apt install ng-common```)
- latest version of node ():
```
    * sudo npm install n -g
    * sudo n stable
```
- python3.6, pip3.6 (https://stackoverflow.com/questions/42662104/how-to-install-pip-for-python-3-6-on-ubuntu-16-10):
```
    * sudo add-apt-repository ppa:jonathonf/python-3.6  # (only for 16.04 LTS)
    * sudo apt update
    * sudo apt install python3.6
    * wget https://bootstrap.pypa.io/get-pip.py
    * sudo python3.6 get-pip.py
```

#### Installation SKF and configuration:
Run on terminal
```
cd /tmp; git clone git://github.com/blabla1337/skf-flask.git
cd /tmp/skf-flask; pip3.6 install -r requirements.txt 
cd /tmp/skf-flask/Angular; npm install
cd /tmp/skf-flask/Angular; ng build --aot --configuration=production 
rm /etc/nginx/sites-enabled/default
cp /tmp/skf-flask/installations/local/site-tls.conf /etc/nginx/sites-enabled/default

mv /tmp/skf-flask /

# Change the JWT_SECRET value with below command
perl -pi -e "s/JWT_SECRET = ''/JWT_SECRET = 'THIS_SHOULD_BE_CHANGED_AND_RANDOM'/" /skf-flask/skf/settings.py
# Change the domain value with below command
perl -pi -e "s/\*/https:\/\/demo.securityknowledgeframework.org/" /skf-flask/skf/settings.py
# Change the domain value with below command
perl -pi -e "s/http:\/\/127.0.0.1:8888\/api/https:\/\/demo.securityknowledgeframework.org\/api/" /skf-flask/Angular/src/environments/environment.prod.ts
# Change the domain value with below command
perl -pi -e "s/localhost/demo.securityknowledgeframework.org/" /skf-flask/installations/local/skf-angular.sh

# Certificates stored in /skf-flask/ dir
openssl req -nodes -newkey rsa:4096 -keyout /skf-flask/server.key -out /skf-flask/server.csr  -subj "/CN=OWASP-SKF"
openssl x509 -req -days 365 -in /skf-flask/server.csr  -signkey /skf-flask/server.key -out ./skf-flask/server.pem

# Start nginx
sleep 5
sudo nginx

```

#### Run SKF (with terminal in Local folder):
```
# Start SKF services
cd /skf-flask/installations/local; bash wrapper.sh
```
Navigate to https://your_domain_value_you_used_above_commands

#### Error:
If you get the following error
```
nginx: [emerg] a duplicate default server for 0.0.0.0:80 in /etc/nginx/sites-enabled/default:17
```
If you are not using that file just remove it: (```sudo rm /etc/nginx/sites-enabled/default```)