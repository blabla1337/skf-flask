#############
### build ###
#############

# base image
FROM node:12-alpine AS builder

LABEL maintainer="glenn.ten.cate@owasp.org"

WORKDIR /home/user_angular/Angular2

COPY ./Angular2 ./
COPY ./Docker/alpine-cloud/angular/site.conf.template  /home/user_angular/site.conf.template

# Optimize vendor.bundle.js
RUN npm --loglevel=error install &&\
    npm run build --prod

############
### run ###
############

## base image
## nginx-unprivileged uses UID=101 and GID=101 (user and group = nginx)
FROM nginxinc/nginx-unprivileged:1.18.0-alpine as run

## Set ARG for use in later RUN command
ARG GID=0

## Set user for installation steps
USER 0

## Remove default nginx website
RUN rm -rf /usr/share/nginx/html/*

## From builder stage copy over the artifacts in dist folder to default nginx public folder
COPY --from=builder /home/user_angular/Angular2/dist/Angular2 /usr/share/nginx/html

## Copy our default nginx config
COPY --from=builder /home/user_angular/site.conf.template /home/user_angular/site.conf.template

COPY ./Docker/alpine-cloud/angular/entrypoint.sh  /home/user_angular/entrypoint.sh

## Apply ownership and permission changes to function with nginx user, that will also work with OpenShift restricted SCC
RUN chown -R nginx:${GID} /home/user_angular/        &&\
    chmod -R g=u /home/user_angular/                 &&\
    chown -R nginx:${GID} /usr/share/nginx/html      &&\
    chmod -R g=u /usr/share/nginx/html               &&\
    chown -R nginx:${GID} /var/log/nginx             &&\
    chmod -R g=u /var/log/nginx                      &&\
    chmod +x /home/user_angular/entrypoint.sh

# nginx-unprivileged container binds on port 8080. Need to decide whether this is kept or deleted.
#RUN rm -f /etc/nginx/conf.d/default.conf

EXPOSE 8788

# Specify the user by number (nginx=101) to permit this to work with OpenShift "mustRunAsNonRoot" SCC permission as well as standard K8s deployments
USER 101

CMD ["/home/user_angular/entrypoint.sh","/home/user_angular/site.conf.template"]

#First go to the main skf-flask folder and from there build the image
#docker build -f Docker/alpine-cloud/angular/Dockerfile . -t skf-angular --no-cache
#docker run -ti -p 127.0.0.1:8788:8788 skf-angular
#docker buildx build -f Docker/alpine-cloud/angular/Dockerfile  --platform linux/amd64,linux/arm/v7 -t blabla1337/skf-angular:dev --push .