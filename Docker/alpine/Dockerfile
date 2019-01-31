FROM alpine:3.7

# Thanks to Mariano Abdala <marianoabdala@gmail.com>
MAINTAINER Glenn ten Cate <glenn.ten.cate@owasp.org>

RUN apk add alpine-sdk
RUN apk update --no-cache && apk add python3 \
gcc \
nginx \
sqlite \
nodejs \
nodejs-npm \
musl-dev \
python3-dev \
libffi-dev \
py3-pip \
openssl \
bash \
perl \
openblas-dev \
libstdc++ \ 
openblas \
git
RUN ln -s /usr/include/locale.h /usr/include/xlocale.h
RUN git clone https://github.com/leenabhegade/skf-flask.git
# Start Angular app
WORKDIR /skf-flask/Angular
RUN npm install -g @angular/cli
RUN npm install
# Optimize vendor.bundle.js
RUN npm build -prod -aot ./

EXPOSE 443 

# Start python API app
WORKDIR /skf-flask
RUN pip3 install -r requirements.txt
VOLUME [ "/skf-flask" ]
#USER nobody
COPY entrypoint.sh /
COPY wrapper.sh /
COPY skf-api.sh /
COPY skf-angular.sh /
RUN ["chmod", "+x", "/entrypoint.sh"]
RUN ["chmod", "+x", "/wrapper.sh"]
RUN ["chmod", "+x", "/skf-api.sh"]
RUN ["chmod", "+x", "/skf-angular.sh"]

EXPOSE 80

ENTRYPOINT ["/entrypoint.sh"]
