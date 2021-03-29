from flask_restplus import fields
from skf.api.restplus import api



email = api.model('email', {
    'email': fields.email(readOnly=True, description='Email'),
    
})

password = api.model('passwod', {
    'password': fields.email(attribute='code_items.title', required=True, description='Password'),
})