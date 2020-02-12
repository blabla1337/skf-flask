FROM python:3.7 as BUILDER

LABEL maintainer="glenn.ten.cate@owasp.org"

RUN apt update &&\
    apt install -y apt-utils python3-nltk \
    default-libmysqlclient-dev 

FROM python:3.7
# second stage
LABEL maintainer="glenn.ten.cate@owasp.org"

RUN groupadd --gid 1000 user_skf && useradd --uid 1000 --gid user_skf -m user_skf &&  mkdir -p /home/user_skf

ADD ./ /home/user_skf/
RUN chmod a+rw /home/user_skf/skf/db /home/user_skf/skf/db/*
COPY ./Docker/alpine/skf-angular.sh  /skf-angular.sh
COPY ./Docker/alpine/entrypoint.sh  /entrypoint.sh
COPY ./Docker/alpine/skf-api.sh  /skf-api.sh
COPY ./Docker/alpine/wrapper.sh  /wrapper.sh


WORKDIR /home/user_skf/
#USER user_skf

RUN pip3 install --upgrade pip &&\
    pip3 install --user nltk &&\
    pip3 install --user  -r requirements.txt

#USER root

RUN apt update &&\
    apt install -y nodejs \
    npm

#USER user_skf

WORKDIR /home/user_skf/Angular
RUN npm install -g @angular/cli
RUN npm install

EXPOSE 443 80

ENV FLASK_APP=/home/user_skf/skf/app.py
ENV PYTHONPATH=/home/user_skf

# Start python API app
WORKDIR /home/user_skf
VOLUME [ "/home/user_skf" ]
ENTRYPOINT ["/entrypoint.sh"]
