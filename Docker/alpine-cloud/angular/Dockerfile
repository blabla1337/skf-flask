#############
### build ###
#############

# base image
FROM alpine:3.10 AS builder

LABEL maintainer="glenn.ten.cate@owasp.org"

# Get updated CA-Certificates list
RUN apk add ca-certificates
RUN apk update --no-cache && apk add gcc \
nodejs \
nodejs-npm \
bash \
perl \
git

RUN npm install -g @angular/cli

RUN addgroup -g 1000 -S user_angular
RUN adduser -u 1000 -S user_angular -G user_angular
RUN mkdir -p /home/user_angular
RUN chmod -R 777 /home/user_angular
WORKDIR /home/user_angular
USER user_angular

RUN git clone https://github.com/blabla1337/skf-flask.git
WORKDIR /home/user_angular/skf-flask/Angular
RUN npm install
ARG ORIGIN=127.0.0.1
RUN perl -pi -e "s/http:\/\/127.0.0.1:8888\/api/https:\/\/$ORIGIN\/api/" /home/user_angular/skf-flask/Angular/src/environments/environment.prod.ts
RUN perl -pi -e "s/http:\/\/127.0.0.1:8888\/api/https:\/\/$ORIGIN\/api/" /home/user_angular/skf-flask/Angular/src/environments/environment.ts

# Optimize vendor.bundle.js
RUN npm run ng build -- --prod --output-path=dist

############
### prod ###
############

# base image

FROM nginx:1.14.1-alpine
## Copy our default nginx config
COPY --from=builder /home/user_angular/skf-flask/Docker/alpine-cloud/angular/site.conf /etc/nginx/conf.d/
## Remove default nginx website
RUN rm -rf /usr/share/nginx/html/*
## From ‘builder’ stage copy over the artifacts in dist folder to default nginx public folder
COPY --from=builder /home/user_angular/skf-flask/Angular/dist /usr/share/nginx/html
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]

#docker build . -t skf-angular --no-cache --build-arg ORIGIN=127.0.0.1
#docker run -ti -p 127.0.0.1:4200:80 skf-angular
