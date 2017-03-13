FROM alpine 

MAINTAINER Mariano Abdala <mariano.abdala@gmail.com>

RUN apk update --no-cache && apk add python \
    py2-pip \
    git \
    gcc \
    libffi \
    sqlite \
    python-dev \
    libxml2 \
    libxml2-dev \
    libxslt-dev \
    libffi-dev \
    libssl1.0 \
    musl-dev \
    openssl \
    openssl-dev && \
    pip install pip --upgrade && \
    pip install https://github.com/mitsuhiko/flask/tarball/master && \
    git clone https://github.com/blabla1337/skf-flask.git && \
    cd skf-flask && python setup.py install && \
    apk del git gcc openssl py2-pip musl-dev openssl-dev && \
    rm -fr /var/cache/* && \
    rm -fr .git dist build && \
    chown -R nobody:nobody /skf-flask

WORKDIR /skf-flask/skf

USER nobody

EXPOSE 5443

ENTRYPOINT ["python", "skf.py", "--saas"]
