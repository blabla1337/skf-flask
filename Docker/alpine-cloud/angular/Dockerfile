#############
### build ###
#############

# base image
FROM node:8.16.2-alpine AS builder

LABEL maintainer="glenn.ten.cate@owasp.org"

WORKDIR /home/user_angular/Angular

COPY ./Angular ./
COPY ./Docker/alpine-cloud/angular/site.conf.template  /home/user_angular/site.conf.template

# Optimize vendor.bundle.js
RUN npm --loglevel=error install &&\
    npm run build --prod

############
### prod ###
############

# base image
FROM nginx:1.14.1-alpine as run

## Remove default nginx website
RUN rm -rf /usr/share/nginx/html/*
## From builder stage copy over the artifacts in dist folder to default nginx public folder
COPY --from=builder /home/user_angular/Angular/dist /usr/share/nginx/html
## Copy our default nginx config
COPY --from=builder /home/user_angular/site.conf.template /home/user_angular/site.conf.template
COPY ./Docker/alpine-cloud/angular/entrypoint.sh  /home/user_angular/entrypoint.sh

RUN chmod +x /home/user_angular/entrypoint.sh

EXPOSE 8788
CMD ["/home/user_angular/entrypoint.sh","/home/user_angular/site.conf.template"]

#First go to the main skf-flask folder and from there build the image
#docker build -f Docker/alpine-cloud/angular/Dockerfile . -t skf-angular --no-cache
#docker run -ti -p 127.0.0.1:80:8788 skf-angular
