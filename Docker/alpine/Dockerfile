FROM alpine:3.10

LABEL maintainer="glenn.ten.cate@owasp.org"

# Get updated CA-Certificates list
RUN apk add ca-certificates

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
g++ \
git

RUN ln -s /usr/include/locale.h /usr/include/xlocale.h
RUN pip3 install --upgrade pip

RUN git clone https://github.com/blabla1337/skf-flask.git
# Start Angular app
WORKDIR /skf-flask/Angular
RUN npm install -g @angular/cli
RUN npm install
# Optimize vendor.bundle.js
RUN npm build -prod -aot ./

EXPOSE 443 80

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
ENTRYPOINT ["/entrypoint.sh"]
