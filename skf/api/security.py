import jwt, datetime, re

from skf import settings
from flask import request, abort
from skf.api.restplus import api
from skf.database import db
from skf.database.logs import Log


def security_headers():
    """This decorator passes multiple security headers"""
    return {'X-Frame-Options': 'deny',
            'X-XSS-Protection': '1',
            'X-Content-Type-Options': 'nosniff',
            'Cache-Control': 'no-store, no-cache',
            'Strict-Transport-Security': 'max-age=16070400',
            'Server': 'Security Knowledge Framework API'}


def log(message, threat, status):
    """Create log entry and write events triggerd by the user, contains FAIL or SUCCESS and threat LOW MEDIUM HIGH"""
    now = datetime.datetime.now()
    dateLog = now.strftime("%Y-%m-%d")
    dateTime = now.strftime("%H:%M")
    try:
        ip = request.remote_addr
        if request.headers.get('Authorization'):
            token = request.headers.get('Authorization').split()[0]
            checkClaims = jwt.decode(token, settings.JWT_SECRET, algorithms='HS256')
            user_id = checkClaims['UserId']
            #event = Log(dateLog, dateTime, threat, ip, message, status, user_id)
            #db.session.add(event)
            #db.session.commit()
        else:
            user_id = "0"
            #event = Log(dateLog, dateTime, threat, ip, message, status, user_id)
            #db.session.add(event)
            #db.session.commit()
    except:
        user_id = "0"
        ip = "0.0.0.0"
        event = "Datelog: "+dateLog+" "+" Datetime: "+dateTime+" "+"Threat: "+threat+" "+" IP:"+ip+" "+"UserId: "+user_id+" "+"Status: "+status+" "+"Message: "+message


def val_alpha(value):
    """User input validation for checking a-zA-Z"""
    match = re.findall(r"[^\w]|[\d]", str(value))
    if match:
        log("User supplied not an a-zA-Z ?", "MEDIUM", "FAIL")
        abort(400, "Validation Error")
    else:
        return True


def val_alpha_num(value):
    """User input validation for checking a-z A-Z 0-9 _ . - ?"""
    match = re.findall(r"[^\ \w\.-\?]", value)
    if match:
        log("User supplied not an a-z A-Z 0-9 _ . - ? value", "MEDIUM", "FAIL")
        abort(400, "Validation Error")
    else:
        return True

def val_alpha_num_special(value):
    """User input validation for checking a-z A-Z 0-9 _ . - ' , " """
    match = re.findall(r"[^\ \w_\.\-\\|\\'\",\+\(\)\/\:@\?\&\=\%\!\#\^\;]", str(value))
    if match:
        log("User supplied not an a-z A-Z 0-9 _ . , - / ! # ^ & +' \" value", "MEDIUM", "FAIL")
        abort(400, "Validation Error on val_alpha_num_special")
    else:
        return True

def val_num(value): 
    """User input validation for checking numeric values only 0-9"""
    if not isinstance( value, int ):
        log("User supplied not an 0-9", "MEDIUM", "FAIL")
        abort(400, "Validation Error on val_num")
    else:
        return True


def val_float(value): 
    """User input validation for checking float values only 0-9 ."""
    if not isinstance(value, float):
        log("User supplied not a float value.", "MEDIUM", "FAIL")
        abort(400, "Validation Error on val_float")
    else:
        return True