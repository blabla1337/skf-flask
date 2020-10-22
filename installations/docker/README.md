### Docker

The fastest way to start using the SKF project is using the pre-built containers hosted at Docker hub. This container always has the very latest version from the master repository. 
1. In order to get SKF running on your local machine we start by cloning the github repository:

```
git clone https://github.com/blabla1337/skf-flask.git
```

2. Install Docker
```
https://docs.docker.com/get-docker/
```

3. Enable local Kubernetes cluster in Docker Desktop
Getting your OWASP SKF instance ready to deploy the labs on your local machine we need to configure your local docker desktop to also enable a local kubernetes cluster. In order to achieve this we go to “Docker desktop -> preferences” where we will find the tab “Kubernetes”
[![SKF local K8s](https://uploads-ssl.webflow.com/5cc6b31ab2ea2ea91b3735d6/5e85f15098a7d63b7faeac36_M0QofKrJDrvOa7Uw4L6ABnnvS0TUeOc0STMQuG0JQnn5qmgL-GgBq50C9f_WfIn484abtascDiMX-nzEib-MXTQilTJrzfMnvIn8f_xtK93Bm3pWqxyZUHCNfTQ8BqnV-sbFudUS.png)](https://www.zerocopter.com/blog-en/enable-software-developers-to-build-secure-applications-by-design-with-owasp-skf) 

First we want to select “Enable Kubernetes” after which we press on “Apply and restart” to make your Docker desktop pull all the configuration files needed for a successful Kubernetes installation.

For Linux users you may want to look at Minikube for deploying locally. Alternatively if you do not want to go through all the hassle of installing a local kubernetes cluster you can also provide the configuration file from the cloud provider of your choosing, or simply choose to clone the lab repository and run them as flask applications with python as described here. After setting up our local cluster it is time to perform a “docker-compose up” command in the root directory of the SKF project.

4. Profit! Ready to go
```
cd skf-flask
docker-compose up
```

The application will greet you on:
http://localhost

If you are done don't forget to kill it again with:
```
docker-compose down
```

5. Location of SKF images
We also have a list of old OWASP-SKF Docker images available:

Angular:
https://hub.docker.com/repository/docker/blabla1337/skf-angular

API:
https://hub.docker.com/repository/docker/blabla1337/skf-api

SKF-Labs:
https://hub.docker.com/repository/docker/blabla1337/owasp-skf-lab
