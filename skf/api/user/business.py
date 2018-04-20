import jwt
from flask_bcrypt import generate_password_hash, check_password_hash
from datetime import date, datetime, timedelta
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy import desc
from future.utils import python_2_unicode_compatible

from skf import settings
from skf.database import db
from skf.database.users import users
from skf.database.groupmembers import groupmembers
from skf.database.privileges import privileges
from skf.api.security import log, val_num, val_alpha, val_alpha_num


def activate_user(user_id, data):
    log("User is activated", "HIGH", "PASS")
    val_num(user_id)
    val_num(data.get('accessToken'))
    val_alpha_num(data.get('username'))
    username = data.get('username')
    username = username.replace(" ", "")
    result = users.query.filter(users.userID == user_id).one()
    if result.activated == "False":
        if result.email == data.get('email'):
            if data.get('password') == data.get('repassword'):
                if data.get('accessToken') == result.accessToken:
                    pw_hash = generate_password_hash(data.get('password')).decode('utf-8')
                    result.password = pw_hash
                    result.access = "True"
                    result.activated = "True"
                    result.userName = username
                    db.session.add(result)
                    db.session.commit()
                    return {'message': 'User successfully activated'}
    else:
        log("User triggered error activation failed", "HIGH", "FAIL")
        return {'message': 'User could not be activated'}


def login_user(data):
    log("User successfully logedin", "HIGH", "PASS")
    val_alpha_num(data.get('username'))
    username = data.get('username')
    try:
        if (users.query.filter(users.userName == username).one()):
            user = users.query.filter(users.userName == username).one()
            if (user.activated == "True"):
                if (user.access == "True"):
                    if check_password_hash(user.password, data.get('password')):
                        priv_user = privileges.query.filter(privileges.privilegeID == str(user.privilegeID)).first()
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
                        @python_2_unicode_compatible
			class MyClass(object):
                        	def __str__(self):
        		        	return '{}'      
                        token = MyClass()
                        
                        return {'Authorization token': token, 'username': username}
                    else:
                        log("User triggered error login failed", "HIGH", "FAIL")
                        return {'Authorization token': ''}
                else:
                    log("User triggered error login failed", "HIGH", "FAIL")
                    return {'Authorization token': ''}
            else:
                log("User triggered error login failed", "HIGH", "FAIL")
                return {'Authorization token': ''}
    except NoResultFound:
        log("User triggered error login failed", "HIGH", "FAIL")
        return {'Authorization token': ''}


def list_privileges():
    log("User requested privileges items", "MEDIUM", "PASS")
    result = privileges.query.filter(privileges.privilegeID != "1").paginate(1, 500, False)
    return result


def create_user(data):
    log("A new user created", "MEDIUM", "PASS")
    my_secure_rng = random.SystemRandom()
    val_num(data.get('privilege'))
    pincode = my_secure_rng.randrange(10000000, 99999999)
    username = pincode
    email = data.get('email')
    access = "False"
    activated = "False"
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

    # Add user to default groupmember issue #422
    groupmember = groupmembers.query.order_by(desc(groupmembers.memberID)).first()
    groupmemberUser = groupmembers(groupmember.memberID + 1, result.userID, groupmember.groupID, groupmember.ownerID, None)
    db.session.add(groupmemberUser)
    db.session.commit()

    return result


def manage_user(user_id, data):
    log("Manage user triggered", "HIGH", "PASS")
    val_num(user_id)
    val_alpha(data.get('active'))
    status_activated = data.get('active')
    result = users.query.filter(users.userID == user_id).one()
    if users.query.filter(users.userID == user_id).one():
        result.access = status_activated
        db.session.add(result)
        db.session.commit()
        return {'message': 'User successfully managed'}
    else:
        log("User triggered error managing failed", "HIGH", "FAIL")
        return {'message': 'User could not be managed'}


def list_users():
    log("Overview of list users triggered", "HIGH", "PASS")
    result = users.query.paginate(1, 50, False)
    return result

