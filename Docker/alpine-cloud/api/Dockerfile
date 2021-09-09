############
### build ###
#############

# base image
FROM python:3.7 as BUILDER

LABEL maintainer="glenn.ten.cate@owasp.org"

RUN apt-get update &&\
    apt-get install -y --no-install-recommends apt-utils python3-nltk \
    default-libmysqlclient-dev \
    vim \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

############
### run ###
############

# base image
FROM python:3.7-slim

LABEL maintainer="glenn.ten.cate@owasp.org"

RUN apt-get update &&\
    apt-get install -y --no-install-recommends \
    libblas-dev \
    liblapack-dev \
    libatlas-base-dev \
    gfortran \
    procps \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

RUN groupadd --gid 1000 user_api && useradd --uid 1000 --gid user_api -m user_api &&  mkdir -p /home/user_api

ADD ./ /home/user_api/
COPY ./Docker/alpine-cloud/api/entrypoint.sh  /home/user_api/entrypoint.sh

RUN touch /home/user_api/skf/db/db.sqlite
RUN chmod a+rw /home/user_api/skf/db /home/user_api/skf/db/*

RUN chown -R user_api /home/user_api/
WORKDIR /home/user_api/

USER user_api

RUN mkdir .kube
#magic below for PI docker image speeding up
RUN mkdir .config
RUN mkdir .config/pip
RUN echo "[global]" >> .config/pip/pip.conf
RUN echo "extra-index-url=https://www.piwheels.org/simple" >> .config/pip/pip.conf

RUN pip3 install --upgrade pip --no-cache-dir &&\
    pip3 install --user nltk --no-cache-dir &&\
    pip3 install --user cython --no-cache-dir 

#enrich ntlk data sets 
RUN python3 -m nltk.downloader punkt stopwords 

#magic below for PI docker image speeding up
RUN if [ `ps auwxf | grep qemu-arm | wc -l` = 4 ]; \
then \
  pip3 install --user numpy==1.19.0rc2 scipy==1.5.0rc2 --no-cache-dir; \
else \
  pip3 install --user numpy scipy --no-cache-dir; \
fi 
RUN pip3 install --user  -r requirements.txt --no-cache-dir


EXPOSE 8888

CMD ["/home/user_api/entrypoint.sh"]


#First go to the main skf-flask folder and from there build the image
#docker build -f Docker/alpine-cloud/api/Dockerfile . -t blabla1337/skf-api:dev --no-cache
#docker buildx build -f Docker/alpine-cloud/api/Dockerfile  --platform linux/amd64,linux/arm/v7 -t blabla1337/skf-api:dev --push .
#docker run -e "ORIGIN=localhost" -e "JWT_SECRET=change_this_super_secret_random_string" -ti -p 127.0.0.1:8888:8888 skf-api
