import jwt, random, sys 

from flask_bcrypt import generate_password_hash, check_password_hash
from datetime import date, datetime, timedelta
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy import desc

from skf import settings
from skf.database import db
from skf.database.users import User
from skf.database.groups import Group
from skf.database.groupmembers import GroupMember
from skf.database.privileges import Privilege
from skf.api.security import log, val_num, val_alpha, val_alpha_num
import sys

def activate_user(user_id, data):
    log("User is activated", "HIGH", "PASS")
    val_num(user_id)
    val_num(data.get('accessToken'))
    val_alpha_num(data.get('userName'))
    userName = data.get('userName')
    userName = userName.replace(" ", "")
    result = User.query.filter(User.id == user_id).one()
    if not result.activated:
        if result.email == data.get('email'):
            if data.get('password') == data.get('repassword'):
                if data.get('accessToken') == result.accessToken:
                    pw_hash = generate_password_hash(data.get('password')).decode('utf-8')
                    result.password = pw_hash
                    result.access = True
                    result.activated = True
                    result.userName = userName
                    db.session.add(result)
                    db.session.commit()
                    return {'message': 'User successfully activated'}
    else:
        log("User triggered error activation failed", "HIGH", "FAIL")
        return {'message': 'User could not be activated'}


def login_user(data):
    log("User successfully logedin", "HIGH", "PASS")
    val_alpha_num(data.get('userName'))
    userName = data.get('userName')

    try:
        user = User.query.filter(User.userName == userName).one()
        if not user is None and user.activated and user.access \
            and check_password_hash(user.password, data.get('password')):
                payload = {
                    # userid
                    'UserId': user.id,
                    #issued at
                    'iat': datetime.utcnow(),
                    #privileges
                    'privilege': user.privilege.privilege,
                    #expiry
                    'exp': datetime.utcnow() + timedelta(minutes=120)
                    #claims for access api calls
                    #'claims': 'kb/items/update,project/items,non/existing/bla,'
                }
                token_raw = jwt.encode(payload, settings.JWT_SECRET, algorithm='HS256')
                if sys.version_info.major == 3:
                	unicode = str
                token = unicode(token_raw,'utf-8')
                return {'Authorization token': token, 'userName': userName}

        log("User triggered error login failed", "HIGH", "FAIL")
        return {'Authorization token': ''}

    except NoResultFound:
        log("User triggered error login failed", "HIGH", "FAIL")
        return {'Authorization token': ''}

def list_privileges():
    log("User requested privileges items", "MEDIUM", "PASS")
    result = Privilege.query.filter(Privilege.id != "1").paginate(1, 500, False)
    return result

def create_user(data):
    log("A new user created", "MEDIUM", "PASS")
    my_secure_rng = random.SystemRandom()
    val_num(data.get('privilege_id'))
    accessToken = my_secure_rng.randrange(10000000, 99999999)
    email = data.get('email')
    #access = False # By default
    #activated = False # By default
    privilege_id = 0
    password = ""
     
    try:
        user = User(email)
        user.privilege_id = privilege_id
        user.userName = accessToken
        user.accessToken  = accessToken
        # Add user to default groupmember issue #422
        user.group_id = 0
        #user.groups.add = Group.query.order_by(desc(Group.id)).first()

        print(user, file=sys.stderr)
        db.session.add(user)
        db.session.commit()

    except:
        db.session.rollback()
        raise

    result = User.query.filter(User.email == email).one()
    return result

def manage_user(user_id, data):
    log("Manage user triggered", "HIGH", "PASS")
    val_num(user_id)
    val_alpha(data.get('active'))
    status_activated = data.get('active').lower()=='true'

    user = User.query.get(user_id)
    user.access = status_activated
    try:
        db.session.add(user)
        db.session.commit()

    except Exception as e:
        db.session.rollback()
        log("User triggered error managing failed: {}".format(e), "HIGH", "FAIL")
        return {'message': 'User could not be managed'}
    
    return {'message': 'User successfully managed'}

def list_users():
    log("Overview of list users triggered", "HIGH", "PASS")
    result = User.query.paginate(1, 50, False)
    return result

