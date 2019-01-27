Deployment of SKF Framework to Azure Web App for Containers
============================================================

This guide will allow you to run the OWASP Security Knowledge Framework in Azure. 

This guide assumes you have an Azure account and some experience using Azure. Additionally, it 
may incur some costs for creation of apps and container registery inside azure portal. Before 
deployment of the framework to the azure you will need to make sure below setup on azure is ready:

## Steps to be followed for the azure deployment
### Creation of an azure container registry in azure portal
Create an azure container registery in azure. Follow instructions in this 
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
You can fetch them from Access keys from your container regitry from azure portal. Change the 
username/image-name path in destination of docker tag command to an appropriate path.

If everything goes well your docker container registry will now contain the image
you pushed in the previous step. The next step is to create a web app and link the webapp
to the container registery and the image.

### Creation of web app for containers app in azure portal
Go to the dashboard and press the "Create new resource" icon. Search for "Web App for Containers" 
and specify the required details such as app name, subcription, resource group, select linux, 
app service plan and finally configure container. Choose "Azure Container Registry" and choose the registry, image, set tag as latest. 

After the web app is created, go in the web app service and you will see list of controls on the left side of the app service. Go in the "Application Settings". Add followings variables in the "Application Settings" in your app.

| Key	     							|	   Value 							| 
|---------------------------------------|---------------------------------------|
| HTTPS    	 							|  false								| 
| JWT_SECRET 							|  change_to_super_secret_value			|  
| WEBSITES_PORT 						|  80 									|
| WEBSITES_CONTAINER_START_TIME_LIMIT   |  800									|	
| ORIGIN								|  yourappservicename.azurewebsites.net |
---------------------------------------------------------------------------------	

You need to set the HTTPS to false as SSL is handled by azure so you don't want nginx to setup SSL for skf. You will need to run the nginx on port 80 and set the same value to WEBSITES_PORT so 
that azure can expose this port to the incoming connections.WEBSITES_CONTAINER_START_TIME_LIMIT is required to set because angular application takes sometime for building and if the container doesnot start in time the app will not start at all. ORIGIN should be set to the URL of your app. 
Once you create the webapp you will be able to see the url for it.

IN Application settings there is one more settings which is very important. There is a field called "Always On" , it should to be set ON so that

Go to container settings switch the Continous deployment to ON. This is required everytime you push to the registry either manually or through ci your azure should pull new image and deploy it. You can verify that you have set the continous deployment to on by checking for field DOCKER_ENABLE_CI in the Application settings.


