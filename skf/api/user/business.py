import jwt, random, sys 
from flask import abort
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
from skf.api.security import log, val_num, val_alpha, val_alpha_num, val_alpha_num_special

def activate_user(user_id, data):
    username = strip_whitespace_from_username(data.get("username"))
    result = get_user_result_by_id(user_id)
    user_is_already_activated(result.activated)     
    compare_email(result.email, data.get('email'))
    compare_passwords(data.get('password'), data.get('repassword'))
    compare_access_tokens(result.accessToken, data.get('accessToken'))
    pw_hash = generate_password_hash(data.get('password')).decode('utf-8')
    activate_account(username, pw_hash, user_id)
    log("User is activated", "HIGH", "PASS")
    return {'message': 'User successfully activated'}


def login_user(data):
    user = get_user_result_by_username(data.get("username"))
    is_user_activated(user)
    does_user_has_access(user)
    check_password(user, data.get("password"))
    log("User successfully logedin", "HIGH", "PASS")
    token = create_jwt_token_for_user(user)
    return {'Authorization token': token, 'username': user.username}

def create_user(data):
    log("A new user created", "MEDIUM", "PASS")
    my_secure_rng = random.SystemRandom()
    try:
        user = User(data.get('email'))
        user.privilege_id = data.get('privilege_id')
        user.username = accessToken
        user.accessToken  = my_secure_rng.randrange(10000000, 99999999)
        user.group_id = 0
        db.session.add(user)
        db.session.commit()
    except:
        db.session.rollback()
        raise
    result = User.query.filter(User.email == data.get('email')).one()
    return result

def manage_user(user_id, data):
    log("Manage user triggered", "HIGH", "PASS")
    user = get_user_result_by_id(user_id)
    user.access = data.get('active').lower()=='true'
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

def get_user_result_by_username(username):
    try:
        user = User.query.filter(User.username == username).one()
        return user
    except:
        return abort('Login was failed', 400)

def is_user_activated(user):
    if not user.activated:
        return abort('Login was failed', 400)

def does_user_has_access(user):
    if not user.access:
        return abort('Login was failed', 400)

def check_password(password_from_db, supplied_password):
    if not check_password_hash(password_from_db.password, supplied_password):
        return abort('Login was failed', 400)

def create_jwt_token_for_user(user):
    payload = {
        'UserId': user.id,
        'iat': datetime.utcnow(),
        'privilege': user.privilege.privilege,
        'exp': datetime.utcnow() + timedelta(minutes=120)
    }
    token_raw = jwt.encode(payload, settings.JWT_SECRET, algorithm='HS256')
    if sys.version_info.major == 3:
        unicode = str
    token = unicode(token_raw,'utf-8')
    return token

def get_user_result_by_id(user_id):
    return User.query.filter(User.id == user_id).one() 

def strip_whitespace_from_username(username):
    refactor = username.replace(" ", "")
    return refactor

def user_is_already_activated(result):
    if result == True:
        return abort('Login was failed', 400)

def compare_email(email_from_query, email_from_form):
    if email_from_query != email_from_form:
        return abort('Login was failed', 400)

def compare_passwords(password, repassword):
    if password != repassword:
        return abort('Login was failed', 400)

def compare_access_tokens(token_from_query, token_from_form):
    val_num(token_from_form)
    if token_from_query != token_from_form:
        return abort('Login was failed', 400)

def activate_account(username, pw_hash, user_id):
    activate = get_user_result_by_id(user_id)
    activate.password = pw_hash
    activate.access = True
    activate.activated = True
    activate.username = username
    db.session.add(activate)
    db.session.commit()

def list_privileges():
    log("User requested privileges items", "MEDIUM", "PASS")
    result = Privilege.query.paginate(1, 500, False)
    return result

