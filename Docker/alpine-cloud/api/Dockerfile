############
### run ###
############

# base image
FROM python:3.7-slim-stretch

LABEL maintainer="glenn.ten.cate@owasp.org"

RUN apt-get update &&\
    apt-get install -y --no-install-recommends \
    libblas-dev \
    liblapack-dev \
    libatlas-base-dev \
    gfortran \
    procps \
    vim \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Create user_api user and group.
RUN groupadd --gid 1000 user_api && useradd --uid 1000 --gid user_api -m user_api && mkdir -p /home/user_api

# Now we'll be run as user_api inside the home directory
WORKDIR /home/user_api
USER user_api

RUN mkdir .kube .config .config/pip
RUN echo "[global]\nextra-index-url=https://www.piwheels.org/simple" >> .config/pip/pip.conf
RUN pip3 install --upgrade pip --no-cache-dir &&\
    pip3 install --user nltk --no-cache-dir &&\
    pip3 install --user cython --no-cache-dir 

# Enrich ntlk data sets
RUN python3 -m nltk.downloader punkt stopwords 

# Magic below for PI docker image speeding up
RUN if [ `ps auwxf | grep qemu-arm | wc -l` = 4 ]; \
then \
  pip3 install --user numpy==1.19.0rc2 scipy==1.5.0rc2 --no-cache-dir; \
else \
  pip3 install --user numpy scipy --no-cache-dir; \
fi 

# Intall packages from requirements.txt
COPY --chown=user_api:user_api ./requirements.txt /home/user_api/requirements.txt
RUN pip3 install --user  -r requirements.txt --no-cache-dir

COPY --chown=user_api:user_api ./Docker/alpine-cloud/api/entrypoint.sh  /home/user_api/entrypoint.sh

COPY --chown=user_api:user_api ./ /home/user_api/
RUN touch /home/user_api/skf/db/db.sqlite && chmod a+rw /home/user_api/skf/db /home/user_api/skf/db/*

EXPOSE 8888

CMD ["/home/user_api/entrypoint.sh"]


# First go to the main skf-flask folder and from there build the image
#     DOCKER_BUILDKIT=1 docker build -f Docker/alpine-cloud/api/Dockerfile . -t blabla1337/skf-api:dev --no-cache
#     docker buildx build -f Docker/alpine-cloud/api/Dockerfile  --platform linux/amd64,linux/arm/v7 -t blabla1337/skf-api:dev --push .
#     docker run -e "ORIGIN=localhost" -e "JWT_SECRET=change_this_super_secret_random_string" -ti -p 127.0.0.1:8888:8888 skf-api
#
# Running with DOCKER_BUILDKIT is not required, however allows the Angular2 directory to be excluded from skf-api builds.
