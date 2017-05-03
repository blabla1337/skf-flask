import jwt, secrets

from flask_bcrypt import generate_password_hash, check_password_hash
from datetime import date, datetime, timedelta

from skf import settings
from skf.database import db
from skf.database.users import users
from skf.database.privileges import privileges
from skf.api.security import val_num, val_alpha, val_alpha_num


def activate_user(user_id, data):
    val_num(user_id)
    user = users.query.filter(users.userID == user_id).one()
    if user.activated == "false":
        if user.email == data.get('email'):
            if data.get('password') == data.get('repassword'):
                pw_hash = generate_password_hash(data.get('password')).decode('utf-8')
                user.password = pw_hash
                user.access = "true"
                user.activated = "true"
                db.session.add(user)
                db.session.commit()



def login_user(data):
    username = data.get('username')
    val_alpha(username)
    if users.query.filter(users.userName == username).one():
        user = users.query.filter(users.userName == username).one()
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


def create_user(data):
    my_secure_rng = secrets.SystemRandom()
    pincode = my_secure_rng.randrange(10000000, 99999999)
    username = data.get('username')
    val_alpha_num(username)
    email = data.get('email')
    access = "false"
    activated = "false"
    # New users can only edit:read:delete
    privilege_id = "2"
    password = ""
    user = users(privilege_id, pincode, username, password, access, activated, email)
    try:
        db.session.add(user)
        db.session.commit()
        user_created = users.query.filter(users.email == email).one()
        return user_created
    except:
        return False