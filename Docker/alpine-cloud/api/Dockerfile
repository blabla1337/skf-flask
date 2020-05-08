#############
### build ###
#############

# base image
FROM python:3.7 as BUILDER

LABEL maintainer="glenn.ten.cate@owasp.org"

RUN apt update &&\
    apt install -y apt-utils python3-nltk \
    default-libmysqlclient-dev \
    vim

############
### run ###
############

# base image
FROM python:3.7

LABEL maintainer="glenn.ten.cate@owasp.org"

RUN apt update &&\
    apt install -y vim

RUN groupadd --gid 1000 user_api && useradd --uid 1000 --gid user_api -m user_api &&  mkdir -p /home/user_api

ADD ./ /home/user_api/
COPY ./Docker/alpine-cloud/api/entrypoint.sh  /home/user_api/entrypoint.sh

RUN touch /home/user_api/skf/db/db.sqlite
RUN chmod a+rw /home/user_api/skf/db /home/user_api/skf/db/*

WORKDIR /home/user_api/
USER user_api

RUN mkdir .kube
RUN pip3 install --upgrade pip &&\
    pip3 install --user nltk &&\
    pip3 install --user  -r requirements.txt

EXPOSE 8888

CMD ["/home/user_api/entrypoint.sh"]


#First go to the main skf-flask folder and from there build the image
#docker build -f Docker/alpine-cloud/api/Dockerfile . -t skf-api --no-cache

#docker run -e "ORIGIN=localhost" -e "JWT_SECRET=change_this_super_secret_random_string" -ti -p 127.0.0.1:8888:8888 skf-api
