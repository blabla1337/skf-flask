FROM python:3.7 as BUILDER

LABEL maintainer="glenn.ten.cate@owasp.org"

RUN apt update &&\
    apt install -y apt-utils python3-nltk
    
FROM python:3.7
# second stage
LABEL maintainer="glenn.ten.cate@owasp.org"

RUN groupadd --gid 1000 user_api && useradd --uid 1000 --gid user_api -m user_api &&  mkdir -p /home/user_api

ADD ./ /home/user_api/
RUN chmod a+rw /home/user_api/skf/db /home/user_api/skf/db/*

WORKDIR /home/user_api/
USER user_api

EXPOSE 8888

RUN pip3 install --upgrade pip &&\
    pip3 install --user nltk &&\
    pip3 install --user  -r requirements.txt

CMD ["/home/user_api/.local/bin/gunicorn", "--bind", "0.0.0.0:8888", "wsgi:app"]