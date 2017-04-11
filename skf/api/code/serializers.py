from flask_restplus import fields
from skf.api.restplus import api

code = api.model('code', {
    'codeID': fields.Integer(readOnly=True, description='The unique identifier of a code item'),
    'title': fields.String(required=True, description='Code title'),
    'content': fields.String(required=True, description='Code content'),
    'code_lang': fields.String(required=True, description='Code language'),
})

pagination = api.model('A page of results', {
    'page': fields.Integer(description='Number of the page of results'),
    'pages': fields.Integer(description='Total number of pages of results'),
    'per_page': fields.Integer(description='Number of items per page of results'),
    'total': fields.Integer(description='Total number of results'),
})

code_lang = api.model('Code language', {
    'code_lang': fields.String(required=True, description='Code language', location='form'),
})


page_of_code_items = api.inherit('Page of code items', pagination, {
    'items': fields.List(fields.Nested(code))
})

message = api.model('Response message', {
    'message': fields.String(required=True, description='Response message'),
})
