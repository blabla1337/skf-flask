FROM alpine

# Thanks to Mariano Abdala <marianoabdala@gmail.com>
MAINTAINER Glenn ten Cate <glenn.ten.cate@owasp.org>

RUN apk update --no-cache && apk add python3 \
gcc \
sqlite \
nodejs \
musl-dev \
python3-dev \
libffi-dev \ 
py3-pip \
git 
RUN git clone -b rebuild https://github.com/blabla1337/skf-flask.git
WORKDIR /skf-flask
RUN pip3 install -r requirements.txt
ENV FLASK_APP=skf/app.py
ENV PYTHONPATH=/skf-flask
USER nobody
EXPOSE 8888
#ENTRYPOINT ["python3", "skf/app.py"]
