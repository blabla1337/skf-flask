#############
### build ###
#############
# TO-DO Fix Angular versions and npm modules and so we an use the builder image step again :(

# base image
#FROM node:15-alpine AS builder

#LABEL maintainer="glenn.ten.cate@owasp.org"

#WORKDIR /home/user_angular/Angular2

#COPY ./Angular2 ./
#COPY ./Docker/alpine-cloud/angular/site.conf.template  /home/user_angular/site.conf.template

#RUN node -v

# Optimize vendor.bundle.js
#RUN npm --loglevel=error install &&\
#    npm run build --prod --loglevel=error

############
### run ###
############

# base image
FROM nginx:1.14.1-alpine as run


## Remove default nginx website
RUN rm -rf /usr/share/nginx/html/*

COPY ./Angular2/dist/Angular2 ./usr/share/nginx/html
COPY ./Docker/alpine-cloud/angular/site.conf.template  /home/user_angular/site.conf.template
COPY ./Docker/alpine-cloud/angular/entrypoint.sh  /home/user_angular/entrypoint.sh

## From builder stage copy over the artifacts in dist folder to default nginx public folder
#COPY --from=builder /home/user_angular/Angular2/dist/Angular2 /usr/share/nginx/html

## Copy our default nginx config
#COPY --from=builder /home/user_angular/site.conf.template /home/user_angular/site.conf.template


# not the most secure solution but the entrypoint needs to be able to copy the correct config into confd.d,
# also the Deployment has a  securityContext because, K8s best practices so the entrypoint needs to start as that user
# so even if we wanted, we cannot use Nginx to drop user privileges after the entrypoint starts
# TODO find a better way
RUN chown -R nginx:nginx /home/user_angular/ &&\
    chown -R nginx:nginx /usr/share/nginx/html &&\
    chown -R nginx:nginx /etc/nginx/conf.d/ &&\
    chown -R nginx:nginx /var/log/nginx &&\
    # move the .pid file somewhere we can run
    sed -i -e "s_/var/run/nginx.pid_/etc/nginx/conf.d/nginx.pid_g" /etc/nginx/nginx.conf &&\
    chmod +x /home/user_angular/entrypoint.sh

RUN ls -lart /usr/share/nginx/html | wc -l
# nginx default container tries to bind on port 80 before dropping privileges.
# there's no point in binding on a privileged port in our scenario
RUN rm -f /etc/nginx/conf.d/default.conf

EXPOSE 8788
USER nginx

CMD ["/home/user_angular/entrypoint.sh","/home/user_angular/site.conf.template"]

#First go to the main skf-flask folder and from there build the image
#docker build -f Docker/alpine-cloud/angular/Dockerfile . -t skf-angular --no-cache
#docker run -ti -p 127.0.0.1:8788:8788 skf-angular
#docker buildx build -f Docker/alpine-cloud/angular/Dockerfile  --platform linux/amd64,linux/arm/v7 -t blabla1337/skf-angular:dev --push .