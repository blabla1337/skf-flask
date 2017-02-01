from flask_restplus import fields
from skf.api.restplus import api

kb = api.model('kb', {
    'kbID': fields.Integer(readOnly=True, description='The unique identifier of a kb item'),
    'title': fields.String(required=True, description='KB title'),
    'content': fields.String(required=True, description='KB content'),
})

pagination = api.model('A page of results', {
    'page': fields.Integer(description='Number of this page of results'),
    'pages': fields.Integer(description='Total number of pages of results'),
    'per_page': fields.Integer(description='Number of items per page of results'),
    'total': fields.Integer(description='Total number of results'),
})

page_of_kb_items = api.inherit('Page of KB items', pagination, {
    'items': fields.List(fields.Nested(kb))
})

kb_update = api.model('kb_update', {
    'title': fields.String(required=True, description='New KB title'),
    'content': fields.String(required=True, description='New KB content'),
})
