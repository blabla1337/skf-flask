from flask_restplus import fields
from skf.api.restplus import api

activate = api.model('activate', {
    'accessToken': fields.Integer(required=True, description='Authentication token that was generated'),
    'email': fields.String(required=True, description='Email of the user'),
    'password': fields.String(required=True, description='Password of the user'),
    'repassword': fields.String(required=True, description='Retyped password'),
})

login = api.model('login', {
    'username': fields.String(required=True, description='The username of the user'),
    'password': fields.String(required=True, description='The password of the user'),
})

create = api.model('create', {
    'username': fields.String(required=True, description='Username of the user'),
    'email': fields.String(required=True, description='Email of the user'),
})

created = api.model('created', {
    'userID': fields.Integer(required=True, description='The unique identifier of the user'),
    'email': fields.String(required=True, description='Email of the user'),
    'accessToken': fields.String(required=True, description='Generated accessToken of the user'),
})

message = api.model('Response message', {
    'message': fields.String(required=True, description='Response message'),
})

token_auth = api.model('Response Authorization token', {
    'Authorization token': fields.String(required=True, description='Response Authorization token'),
})
 