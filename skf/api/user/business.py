import jwt

from flask_bcrypt import generate_password_hash, check_password_hash
from datetime import date, datetime, timedelta

from skf import settings
from skf.database import db
from skf.database.users import users
from skf.database.privileges import privileges


def activate_user(user_id, data):
    user = users.query.filter(users.userID == user_id).one()
    if users.query.filter(users.activated == "false").one():
        if users.query.filter(users.accessToken == data.get('accessToken')).one():
            if data.get('password') == data.get('repassword'):
                pw_hash = generate_password_hash(data.get('password')).decode('utf-8')
                user.password = pw_hash
                user.access = "true"
                user.activated = "true"
                user.email = data.get('repassword')
                db.session.add(user)
                db.session.commit()


def login_user(data):
    username = data.get('username')
    if users.query.filter(users.userName == data.get('username')).one():
        user = users.query.filter(users.userName == data.get('username')).one()
        if check_password_hash(user.password, data.get('password')):
            priv_user = privileges.query.filter(str(user.privilegeID)).first()

            payload = {
            # userid
            'UserId': user.userID,
            #issued at
            'iat': datetime.utcnow(),
            #privileges
            'privilege': priv_user.privilege,
            #expiry
            'exp': datetime.utcnow() + timedelta(minutes=120),
            #claims for access api calls
            'claims': 'kb/items/update,project/items,non/existing/bla,'
            }
            token_raw = jwt.encode(payload, settings.JWT_SECRET, algorithm='HS256')
            token = str(token_raw,'utf-8')
            return token
