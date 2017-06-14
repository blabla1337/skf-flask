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
linux-headers \ 
python3-dev \
uwsgi-python3 \
libffi-dev \ 
py3-pip \
openssl \
git 
RUN git clone -b rebuild https://github.com/blabla1337/skf-flask.git
# Start Angular app
WORKDIR /skf-flask/Angular
RUN npm install
RUN npm start
EXPOSE 443

# Start python API app
WORKDIR /skf-flask
RUN pip3 install -r requirements.txt
ENV FLASK_APP=skf/app.py
ENV PYTHONPATH=/skf-flask
VOLUME [ "/skf-flask" ]
#USER nobody
#ENTRYPOINT ["entrypoint.sh"]
