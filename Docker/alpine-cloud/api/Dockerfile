FROM alpine:3.10

LABEL maintainer="glenn.ten.cate@owasp.org"

# Get updated CA-Certificates list
RUN apk add ca-certificates
RUN apk update --no-cache && apk add python3 \
gcc \
sqlite \
python3-dev \
libffi-dev \
musl-dev \
py3-pip \
bash \
perl \
openblas-dev \
libstdc++ \ 
openblas \
g++ \
git

RUN ln -s /usr/include/locale.h /usr/include/xlocale.h

RUN pip3 install --upgrade pip

RUN addgroup -g 1000 -S user_api
RUN adduser -u 1000 -S user_api -G user_api
RUN mkdir -p /home/user_api
RUN chmod -R 777 /home/user_api
WORKDIR /home/user_api

#RUN git clone https://github.com/blabla1337/skf-flask.git
ADD ./ ./
WORKDIR /home/user_api/
COPY --chown=user_api:user_api Docker/alpine/entrypoint.sh /home/user_api
COPY --chown=user_api:user_api Docker/alpine/wrapper.sh /home/user_api
COPY --chown=user_api:user_api Docker/alpine/skf-api.sh /home/user_api

USER user_api

RUN pip3 install -r requirements.txt --user
EXPOSE 8888

RUN ["chmod", "+x", "/home/user_api/entrypoint.sh"]
RUN ["chmod", "+x", "/home/user_api/wrapper.sh"]
RUN ["chmod", "+x", "/home/user_api/skf-api.sh"]
ENTRYPOINT ["/home/user_api/entrypoint.sh"]


#First go to the main skf-flask folder and from there build the image
#docker build -f Docker/alpine-cloud/api/Dockerfile . -t skf-api --no-cache

#docker run -e "ORIGIN=localhost" -e "JWT_SECRET=change_this_super_secret_random_string" -ti -p 127.0.0.1:8888:8888 skf-api
