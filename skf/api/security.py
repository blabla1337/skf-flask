import jwt, datetime

from skf import settings
from flask import request, abort
from skf.database import db
from skf.database.logs import logs



def security_headers():
    """This decorator passes multiple security headers"""
    if settings.FLASK_SERVER_NAME == 'localhost:8888':
        return {'X-Frame-Options': 'deny',
                'X-XSS-Protection': '1',
                'X-Content-Type-Options': 'nosniff',
                'Cache-Control': 'no-store, no-cache',
                'Server': 'Security Knowledge Framework API'}
    else:
        return {'X-Frame-Options': 'deny',
                'X-XSS-Protection': '1',
                'X-Content-Type-Options': 'nosniff',
                'Cache-Control': 'no-store, no-cache',
                'Strict-Transport-Security': 'max-age=16070400; includeSubDomains',
                'Server': 'Security Knowledge Framework API'}


def log(message, threat, status):
    """Create log entry and write events triggerd by the user, contains FAIL or SUCCESS and threat LOW MEDIUM HIGH"""
    now = datetime.datetime.now()
    dateLog = now.strftime("%Y-%m-%d")
    dateTime = now.strftime("%H:%M")
    ip = request.remote_addr
    event = logs(dateLog, dateTime, threat, ip, status, message)
    db.session.add(event)
    db.session.commit()

def val_alpha_num(value, countLevel):
    """User input validation for checking a-z A-Z 0-9"""
    match = re.findall(r"[a-zA-Z0-9_.-]", value)
    if match:
        log("User supplied not an a-zA-Z0-9 value", "HIGH", "FAIL")
        return False
    else:
        return True


def val_num(value, countLevel):
    """User input validation for checking numeric values only 0-9"""
    match = re.findall(r'[0-9]', str(value))
    if match:
        log("User supplied not an 0-9", "HIGH", "FAIL")
        return False
    else:
        return True


def val_alpha(value, countLevel):
    """User input validation for checking a-z A-Z"""
    match = re.findall(r'[a-zA-Z_]', str(value))
    if match:
        log("User supplied not an a-zA-Z", "HIGH", "FAIL")
        return False
    else:
        return True


def validate_privilege(self, privilege):
    """Validates the JWT privileges"""
    if not request.headers.get('Authorization'):
        log("Request sent with missing JWT header", "HIGH", "FAIL")
        abort(403, 'JWT missing authorization header')
    try:
        check_privilege = select_privilege_jwt(self)
    except jwt.exceptions.DecodeError:
        log("User JWT header could not be decoded", "HIGH", "FAIL")
        abort(403, 'JWT decode error')
    except jwt.exceptions.ExpiredSignature:
        log("User JWT header is expired", "HIGH", "FAIL")
        abort(403, 'JWT token expired')
    privileges = check_privilege['privilege'].split(':')
    for value in privileges:
        if value == privilege:
            return True
    log("User JWT header contains wrong privilege", "HIGH", "FAIL")
    return  abort(403, 'JWT wrong privileges')


def select_userid_jwt(self):
    """Returns the userID from the JWT authorization token"""
    token = request.headers.get('Authorization').split()[0]
    try:
        checkClaims = jwt.decode(token, settings.JWT_SECRET, algorithms='HS256')
    except jwt.exceptions.DecodeError:
        log("User JWT header could not be decoded", "HIGH", "FAIL")
        abort(403, 'JWT decode error')
    except jwt.exceptions.ExpiredSignature:
        log("User JWT header is expired", "HIGH", "FAIL")
        abort(403, 'JWT token expired')
    return checkClaims['UserId']


def select_privilege_jwt(self):
    """Returns the privileges from the JWT authorization token"""
    token = request.headers.get('Authorization').split()[0]
    try:
        check_privilege = jwt.decode(token, settings.JWT_SECRET, algorithms='HS256')
    except jwt.exceptions.DecodeError:
        log("User JWT header could not be decoded", "HIGH", "FAIL")
        abort(403, 'JWT decode error')
    except jwt.exceptions.ExpiredSignature:
        log("User JWT header is expired", "HIGH", "FAIL")
        abort(403, 'JWT token expired')
    return check_privilege
