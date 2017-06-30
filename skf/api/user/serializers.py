from flask_restplus import fields
from skf.api.restplus import api

activate = api.model('activate', {
    'accessToken': fields.Integer(required=True, description='Authentication token that was generated'),
    'username': fields.String(required=True, description='Username of the new user'),
    'email': fields.String(required=True, description='Email of the user'),
    'password': fields.String(required=True, description='Password of the user'),
    'repassword': fields.String(required=True, description='Retyped password'),
})

message = api.model('Response message', {
    'message': fields.String(required=True, description='Response message'),
})

login = api.model('login', {
    'username': fields.String(required=True, description='The username of the user'),
    'password': fields.String(required=True, description='The password of the user'),
})

create = api.model('create', {
    'email': fields.String(required=True, description='Email of the user'),
    'privilege': fields.Integer(required=True, description='Role of the user privilege: 2, 3, 4'),
})

manage = api.model('manage', {
    'active': fields.String(required=True, default="True", description='Status of the user account'),
})

created = api.model('created', {
    'userID': fields.Integer(required=True, description='The unique identifier of the user'),
    'email': fields.String(required=True, description='Email of the user'),
    'accessToken': fields.String(required=True, description='Generated accessToken of the user'),
})

token_auth = api.model('Response Authorization token', {
    'Authorization token': fields.String(required=True, description='Response Authorization token'),
    'username': fields.String(required=True, description='Response Authorization token'),
})
 
user_list = api.model('user_list', {
    'userName': fields.String(required=True, description='Username of the user'),
    'email': fields.String(required=True, description='Email of the user'),
    'access': fields.String(required=True, description='User has access to application'),
    'activated': fields.String(required=True, description='User is activated'),
    'userID': fields.Integer(required=True, description='The unique identifier of the user'),
})

user_items = api.inherit('List of user items', {
    'items': fields.List(fields.Nested(user_list))
})