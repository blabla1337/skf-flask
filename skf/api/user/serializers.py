from flask_restplus import fields
from skf.api.restplus import api

activate = api.model('activate', {
    'accessToken': fields.Integer(required=True, description='Authentication token that was generated'),
    'email': fields.String(required=True, description='Email of the user'),
    'password': fields.String(required=True, description='Password of the user'),
    'repassword': fields.String(required=True, description='Retyped password'),
})
