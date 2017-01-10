FROM ubuntu:14.04
MAINTAINER Bob van den Heuvel <bvandenheuvel@schubergphilis.com
RUN DEBIAN_FRONTEND=noninteractive apt-get update && apt-get install -y python-pip sqlite3 lib32z1-dev python-dev libxml2-dev libxslt-dev libffi-dev libssl-dev git
RUN pip install https://github.com/mitsuhiko/flask/tarball/master

RUN git clone https://github.com/blabla1337/skf-flask.git
WORKDIR /skf-flask
RUN python setup.py install
WORKDIR /skf-flask/skf
ENTRYPOINT ["python", "skf.py", "--saas"]
