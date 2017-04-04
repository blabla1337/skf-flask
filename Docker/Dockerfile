FROM ubuntu:14.04
MAINTAINER Glenn ten Cate <glenn.ten.cate@owasp.org>
RUN DEBIAN_FRONTEND=noninteractive apt-get update && apt-get install -y python3 python3-pip sqlite3 python-dev libssl-dev libffi-dev git
RUN iptables -I INPUT -p tcp -s 0.0.0.0/0 --dport 9000 -j ACCEPT
RUN git clone -b rebuild https://github.com/blabla1337/skf-flask.git
WORKDIR /skf-flask
RUN pip3 install -r requirements.txt
ENV PYTHONPATH=/skf-flask
ENTRYPOINT ["python3", "skf/app.py"]
