import jwt, secrets

from flask_bcrypt import generate_password_hash, check_password_hash
from datetime import date, datetime, timedelta
from sqlalchemy.orm.exc import NoResultFound

from skf import settings
from skf.database import db
from skf.database.users import users
from skf.database.privileges import privileges
from skf.api.security import log, val_num, val_alpha, val_alpha_num


def activate_user(user_id, data):
    log("User is activated", "HIGH", "PASS")
    username = data.get('username')
    username = username.replace(" ", "")
    val_num(user_id)
    val_num(data.get('accessToken'))
    val_alpha_num(username)
    result = users.query.filter(users.userID == user_id).one()
    if result.activated == "false":
        if result.email == data.get('email'):
            if data.get('password') == data.get('repassword'):
                if data.get('accessToken') == result.accessToken:
                    pw_hash = generate_password_hash(data.get('password')).decode('utf-8')
                    result.password = pw_hash
                    result.access = "true"
                    result.activated = "true"
                    result.userName = username
                    db.session.add(result)
                    db.session.commit()
                    if not result:
                        log("User triggered error activation failed", "HIGH", "FAIL")
                        return {'message': 'User could not be activated'}
                    else:
                        return {'message': 'User successfully activated'}
                else:
                    log("User triggered error activation failed", "HIGH", "FAIL")
                    return {'message': 'User could not be activated'}
            else:
                log("User triggered error activation failed", "HIGH", "FAIL")
                return {'message': 'User could not be activated'}
        else:
            log("User triggered error activation failed", "HIGH", "FAIL")
            return {'message': 'User could not be activated'}
    else:
        log("User triggered error activation failed", "HIGH", "FAIL")
        return {'message': 'User could not be activated'}


def login_user(data):
    log("User successfully logedin", "HIGH", "PASS")
    username = data.get('username')
    val_alpha_num(username)
    try:
        user = users.query.filter(users.userName == username).one()
        if (users.query.filter(users.activated == "true").one()):
            if (users.query.filter(users.userName == username).one()):
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
                        'exp': datetime.utcnow() + timedelta(minutes=120)
                        #claims for access api calls
                        #'claims': 'kb/items/update,project/items,non/existing/bla,'
                    }
                    token_raw = jwt.encode(payload, settings.JWT_SECRET, algorithm='HS256')
                    token = str(token_raw,'utf-8')
                    return {'Authorization token': token}
                else:
                    log("User triggered error login failed", "HIGH", "FAIL")
                    return {'Authorization token': 'Wrong username/password'}
            else:
                log("User triggered error login failed", "HIGH", "FAIL")
                return {'Authorization token': 'Wrong username/password'}
    except NoResultFound:
        log("User triggered error login failed", "HIGH", "FAIL")
        return {'Authorization token': 'Wrong username/password'}


def create_user(data):
    log("A new user created", "MEDIUM", "PASS")
    my_secure_rng = secrets.SystemRandom()
    val_num(data.get('privilege'))
    pincode = my_secure_rng.randrange(10000000, 99999999)
    username = pincode
    email = data.get('email')
    access = "false"
    activated = "false"
    privilege_id = 0
    # New users can only edit:read:delete
    if data.get('privilege') == 1:
        log("User triggered error creating new user", "MEDIUM", "FAIL")
        return {'message': 'User could not be created'}
    else:
        privilege_id = data.get('privilege')
    password = ""
    user = users(privilege_id, pincode, username, password, access, activated, email)
    db.session.add(user)
    db.session.commit()
    result = users.query.filter(users.email == email).one()
    return result

