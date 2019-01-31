Deployment of SKF Framework to Azure Web App for Containers
============================================================

This guide will allow you to run the OWASP Security Knowledge Framework in Azure. 

This guide assumes you have an Azure account and some experience using Azure. Additionally, it 
may incur some costs for creation of web apps and container registery inside azure portal. Before 
deployment of the framework to the azure you will need to make sure below setup on azure is ready:

## Steps to be followed for the Azure deployment
### Creation of an Azure container registry in Azure portal
Create an Azure container registery in azure. Follow instructions in this 
tutorial link https://docs.microsoft.com/en-us/azure/container-registry/container-registry-get-started-portal from microsoft to create an azure container registry. After creating the registry make note of your registry name, username and password which you can get from
the "Access keys" section in your container registry controls.

### Push SKF framework image to the Azure container registery from your local machine
First pull the github repo to your local machine and make sure your inside the Docker/alpine folder
in the repo. 

``` 
docker build -t image-name:latest .

docker login yourregistryname.azurecr.io

docker tag image-name:latest yourregistryname.azurecr.io/username/image-name

docker push yourregistryname.azurecr.io/username/image-name
```

Change the image-name to the relevant image name. Change the yourregistryname to the registry
name you setup in the previous step. The docker login command will ask you for username and password.
You can fetch them from Access keys from your container registry from azure portal. Specify a relevant 
username/image-name path in destination of docker tag command to an appropriate path. Now use docker push 
to push the image to the azure registry.

If everything goes well your azure container registry will now contain the image
you pushed in the previous step. The next step is to create a web app and link the webapp
to the container registery and the image.

### Creation of web app for containers app in azure portal
Go to the dashboard and press the "Create new resource" icon. Search for "Web App for Containers" 
and specify the required details such as app name, subcription, resource group, select linux, 
app service plan and finally configure container. Choose "Azure Container Registry" and select the registry, image, tag. 

After the web app is created, go in the web app service and you will see list of controls on the left side of the app service. Go in the "Application Settings". Add following variables in the "Application Settings" in your app.

| Key	     							|	   Value 							| 
|---------------------------------------|---------------------------------------|
| HTTPS    	 							|  false								| 
| JWT_SECRET 							|  change_to_super_secret_value			|  
| WEBSITES_PORT 						|  80 									|
| WEBSITES_CONTAINER_START_TIME_LIMIT   |  800									|	
| ORIGIN								|  yourappservicename.azurewebsites.net |
---------------------------------------------------------------------------------	

You need to set the HTTPS to false because SSL is handled by azure so you don't want nginx to setup SSL for skf seperately. You will need to run docker container on port 80 so set the value of WEBSITES_PORT to 80 and azure can route traffic to this port. WEBSITES_CONTAINER_START_TIME_LIMIT is required to be set because angular application takes longer for building and if the container does not start in time the app will not start at all because of azure timeout. ORIGIN should be set to the URL of your app (You will find URL in the app service overview section). 

In Application settings there is one more settings which is very important. There is a field called "Always On", it should to be set ON so that the app is available all the times.

Go to Container Settings and switch the Continous deployment option to ON. Everytime you push new image to the registry either manually or through a ci your azure web app service should pull new image and deploy it automatically. You can verify that you have set the continous deployment to "ON" by checking for field DOCKER_ENABLE_CI in the Application settings.

For debuging your application and checking the logs for your app you will need to get access to the logs. You can retain the logs of your application through  "Diagnostics logs" in app service panel.
Select the option "File System" and set the qouta and retention period of your logs. You can view logs in container settings or you can go to "Advancecd Tools" --> "Go". You will find all app specific information
in that page. Click the link  "Current Docker logs" and it will provide you links to access the log info, alternatively you can download logs. 

Finally you can verify that your app is deployed by visiting the app URL. The URL can be found in the app service overview section. Bear in mind that the app may take some time to finish deployment so verify the logs to check the status of the app deployment.
