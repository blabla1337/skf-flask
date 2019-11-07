#############
### build ###
#############

# base image
FROM alpine:3.10 AS builder_img

LABEL maintainer="glenn.ten.cate@owasp.org"

# Get updated CA-Certificates list
RUN apk update --no-cache &&\
    apk add ca-certificates &&\
    apk add gcc \
    nodejs \
    nodejs-npm

RUN npm install -g @angular/cli

RUN addgroup -g 1000 -S user_angular
RUN adduser -u 1000 -S user_angular -G user_angular
RUN mkdir -p /home/user_angular
RUN chmod -R 777 /home/user_angular

WORKDIR /home/user_angular/Angular
ADD ./Angular ./
ADD ./Docker/alpine-cloud/angular/site.conf.template  /home/user_angular/site.conf.template

RUN npm install ./

# Optimize vendor.bundle.js
RUN npm update && npm run ng build -- --prod --output-path=/home/user_angular/Angular/dist
RUN ls -lah /home/user_angular/Angular
############
### prod ###
############

# base image
FROM nginx:1.14.1-alpine as run_img

## From builder stage copy over the artifacts in dist folder to default nginx public folder
COPY --from=builder_img /home/user_angular/Angular/dist /usr/share/nginx/html
## Copy our default nginx config
COPY --from=builder_img /home/user_angular/site.conf.template /home/user_angular/site.conf.template
ADD ./Docker/alpine-cloud/angular/entrypoint.sh  /home/user_angular/entrypoint.sh
## Remove default nginx website
RUN rm -rf /usr/share/nginx/html/*
RUN chmod +x /home/user_angular/entrypoint.sh
EXPOSE 80
CMD ["/home/user_angular/entrypoint.sh","/home/user_angular/site.conf.template"]

#First go to the main skf-flask folder and from there build the image
#docker build -f Docker/alpine-cloud/angular/Dockerfile . -t skf-angular --no-cache --build-arg ORIGIN=127.0.0.1
#docker run -ti -p 127.0.0.1:80:80 skf-angular
