FROM alpine

# Thanks to Mariano Abdala <marianoabdala@gmail.com>
MAINTAINER Glenn ten Cate <glenn.ten.cate@owasp.org>

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
git 
RUN git clone -b rebuild https://github.com/blabla1337/skf-flask.git
# Start Angular app
WORKDIR /skf-flask/Angular
RUN npm install
EXPOSE 443

# Start python API app
WORKDIR /skf-flask
RUN pip3 install -r requirements.txt
VOLUME [ "/skf-flask" ]
#USER nobody
COPY entrypoint.sh /
RUN ["chmod", "+x", "/entrypoint.sh"]
ENTRYPOINT ["/entrypoint.sh"]
