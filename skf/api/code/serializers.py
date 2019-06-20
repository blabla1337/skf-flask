from flask_restplus import fields
from skf.api.restplus import api

code = api.model('code', {
    'codeID': fields.Integer(readOnly=True, description='The unique identifier of a code item'),
    'title': fields.String(required=True, description='Code title'),
    'content': fields.String(required=True, description='Code content'),
    'code_lang': fields.String(required=True, description='Code language'),
})

code_properties = api.model('code_update', {
    'title': fields.String(required=True, description='Code title'),
    'content': fields.String(required=True, description='Code content'),
    'code_lang': fields.String(required=True, description='Code language'),
})


code_items = api.inherit('List of code example items', {
    'items': fields.List(fields.Nested(code))
})

message = api.model('Response message', {
    'message': fields.String(required=True, description='Response message'),
})
