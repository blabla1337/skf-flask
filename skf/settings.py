# Flask settings
# FLASK_SERVER_NAME = FLASK_HOST+":"+str(FLASK_PORT)
FLASK_HOST = '0.0.0.0'
FLASK_PORT = 8888
FLASK_DEBUG = False  # Do not use debug mode in production
CHATBOT_LOG = "db"
SKF_API_URL = "https://demo.securityknowledgeframework.org/api/"

# Flask-Restplus settings
RESTPLUS_SWAGGER_UI_DOC_EXPANSION = 'list'
RESTPLUS_VALIDATE = True
RESTPLUS_MASK_SWAGGER = False
RESTPLUS_ERROR_404_HELP = False
DATABASE = "db/db.sqlite"

# SQLAlchemy settings
#SQLALCHEMY_DATABASE_URI = 'mysql://ricco:the_password@localhost/bla'
#SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:H5hng15K@localhost/skf?charset=utf8mb4' 
SQLALCHEMY_DATABASE_URI = 'sqlite:///'+DATABASE

SQLALCHEMY_TRACK_MODIFICATIONS = True
SQLALCHEMY_ECHO = False

# JWT settings
JWT_SECRET = 'sadasdasdasdas'
ORIGINS = '*'

# Google Scraping
GOOGLE = False
API_KEY = 'AIzaSyDP1iLdfgvct3BQKLAKQaD3UG6LVgiJSLs'
CSE_ID = '007944217764671561800:ve3xx693pke'


#temp defect dojo push settings
DOJO_API_KEY = 'admin:1dfdfa2042567ec751f6b3fa96038b743ea6f1cc'
DOJO_URL = 'https://defectdojo.herokuapp.com/api/v2/import-scan/'

# TESTING settings
TESTING = False
