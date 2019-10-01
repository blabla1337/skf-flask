FROM alpine:3.10

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

RUN addgroup -g 1000 -S user_api
RUN adduser -u 1000 -S user_api -G user_api
RUN mkdir -p /home/user_api
RUN chmod -R 777 /home/user_api
WORKDIR /home/user_api
USER user_api

RUN git clone https://github.com/blabla1337/skf-flask.git

WORKDIR /home/user_api/skf-flask/Angular
RUN npm install

# Optimize vendor.bundle.js
RUN npm build -prod -aot ./

EXPOSE 4200

COPY --chown=user_api:user_api entrypoint.sh /home/user_api/skf-flask
COPY --chown=user_api:user_api wrapper.sh /home/user_api/skf-flask
COPY --chown=user_api:user_api skf-angular.sh /home/user_api/skf-flask

RUN ["chmod", "+x", "/home/user_api/skf-flask/entrypoint.sh"]
RUN ["chmod", "+x", "/home/user_api/skf-flask/wrapper.sh"]
RUN ["chmod", "+x", "/home/user_api/skf-flask/skf-angular.sh"]
ENTRYPOINT ["/home/user_api/skf-flask/entrypoint.sh"]

#docker build . -t skf-angular --no-cache
#docker run -ti -p 127.0.0.1:4200:4200 skf-angular
