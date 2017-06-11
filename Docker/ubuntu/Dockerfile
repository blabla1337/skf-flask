FROM ubuntu:17.04

#Thanks to Bob van den Heuvel <bvandenheuvel@schubergphilis.com>
MAINTAINER Glenn ten Cate <glenn.ten.cate@owasp.org>

RUN DEBIAN_FRONTEND=noninteractive apt-get update && apt-get remove python3.5 && \
apt-get install -y python3.6 \
sqlite3 \
python3.6-dev \
libssl-dev \
libffi-dev \
wget \
git
RUN wget https://bootstrap.pypa.io/get-pip.py
RUN python3.6 get-pip.py
RUN git clone -b rebuild https://github.com/blabla1337/skf-flask.git
WORKDIR /skf-flask
RUN pip3.6 install -r requirements.txt
ENV PYTHONPATH=/skf-flask
EXPOSE 8888
#ENTRYPOINT ["python3.6", "skf/app.py"]