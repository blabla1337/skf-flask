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
USER user_api

#RUN ln -s /usr/include/locale.h /usr/include/xlocale.h
RUN git clone https://github.com/blabla1337/skf-flask.git -b dev
RUN pip3 install -r skf-flask/requirements.txt --user

EXPOSE 8888

COPY --chown=user_api:user_api entrypoint.sh /home/user_api/skf-flask
COPY --chown=user_api:user_api wrapper.sh /home/user_api/skf-flask
COPY --chown=user_api:user_api skf-api.sh /home/user_api/skf-flask

RUN ["chmod", "+x", "/home/user_api/skf-flask/entrypoint.sh"]
RUN ["chmod", "+x", "/home/user_api/skf-flask/wrapper.sh"]
RUN ["chmod", "+x", "/home/user_api/skf-flask/skf-api.sh"]
ENTRYPOINT ["/home/user_api/skf-flask/entrypoint.sh"]

#docker build . -t skf-api --no-cache
#docker run -e "ORIGIN=localhost" -e "JWT_SECRET=change_this_super_secret_random_string" -ti -p 127.0.0.1:8888:8888 skf-api
