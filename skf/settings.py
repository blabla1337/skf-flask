import os
import secrets

# Flask settings
# FLASK_SERVER_NAME = FLASK_HOST+":"+str(FLASK_PORT)
FLASK_HOST = '0.0.0.0'
FLASK_PORT = 8888
# Do not use debug mode in production
FLASK_DEBUG = os.environ.get("SKF_FLASK_DEBUG") or 'False'
CHATBOT_LOG = "db"
SKF_API_URL = os.environ.get("SKF_API_URL") or "https://beta.securityknowledgeframework.org/api/"
ORIGINS = '*'

# Flask-Restplus settings
RESTPLUS_SWAGGER_UI_DOC_EXPANSION = 'list'
RESTPLUS_VALIDATE = True
RESTPLUS_MASK_SWAGGER = False
RESTPLUS_ERROR_404_HELP = False

# Database settings
DATABASE = os.environ.get("SKF_DB_URL") or "sqlite:///db/db.sqlite"
#SQLALCHEMY_DATABASE_URI = 'mysql://root:H5hng15K@localhost/skf?charset=utf8mb4'
#SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://foo:bar@35.190.203.79/skf?charset=utf8mb4'
SQLALCHEMY_DATABASE_URI = DATABASE
SQLALCHEMY_TRACK_MODIFICATIONS = True
SQLALCHEMY_ECHO = False

# JWT settings
JWT_ENABLED = os.environ.get("JWT_ENABLED") or 'False'
JWT_SECRET = os.environ.get("SKF_JWT_SECRET") or secrets.token_hex(32)


# Google Scraping
GOOGLE = False
API_KEY = os.environ.get("SKF_GOOGLE_API_KEY") or ''
CSE_ID = os.environ.get("SKF_GOOGLE_CSE_ID") or ''

# temp defect dojo push settings
DOJO_API_KEY = os.environ.get("SKF_DOJO_API_KEY") or ''
DOJO_URL = os.environ.get("SKF_DOJO_URL") or ''

# TESTING settings
TESTING = (os.environ.get("SKF_TESTING") == 'True') or False

#RABBIT MQ settings
RABBIT_MQ_CONN_STRING = os.environ.get("RABBIT_MQ_CONN_STRING") or 'localhost'
RABBITMQ_DEFAULT_USER = os.environ.get("RABBITMQ_DEFAULT_USER") or 'guest'
RABBITMQ_DEFAULT_PASS = os.environ.get("RABBITMQ_DEFAULT_PASS") or 'guest'

# SKF-LABS settings
LABS_KUBE_CONF = os.environ.get("LABS_KUBE_CONF") or '~/.kube/config'