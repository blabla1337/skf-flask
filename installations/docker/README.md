### Docker

The fastest way to start using the SKF project is using the pre-built container hosted at Docker hub. This container always has the very latest version from the master repository. Change the JWT_SECRET value to a new random secret string before starting the docker image.

First run the docker pull command to get the latest image
```
docker pull blabla1337/skf-flask
```
Then start the docker image 
```
docker run -e "ORIGIN=localhost" -e "JWT_SECRET=change_this_super_secret_random_string" -ti -p 127.0.0.1:443:443 blabla1337/skf-flask
```
You can also store the database outside of the Docker container so all the data becomes persistent.
Replace the /Users/gibson/Desktop/development/skf-flask/skf/db/db.sqlite with your local db.sqlite file and then run:
```
docker run -v /Users/gibson/Desktop/development/skf-flask/skf/db/db.sqlite:/skf-flask/skf/db/db.sqlite -e "ORIGIN=localhost" -e "JWT_SECRET=change_this_super_secret_random_string" -ti -p 127.0.0.1:443:443 blabla1337/skf-flask
```

The application will greet you on:
https://localhost

We also have a list of old OWASP-SKF Docker images available:
https://cloud.docker.com/repository/docker/blabla1337/skf-flask/tags