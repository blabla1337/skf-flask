from flask import Flask
from flask.ext.bcrypt import Bcrypt

app = Flask(__name__)
bcrypt = Bcrypt(app)

pw_hash = bcrypt.generate_password_hash('test-skf')

print pw_hash

if bcrypt.check_password_hash('$2a$12$47rc7flY6Ap/xfNzn4eeN.nTEavsTTEci77OESYDzNA94y/PuyRSu', 'hunters2'):
    print "true"
