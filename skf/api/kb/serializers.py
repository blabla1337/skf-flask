from flask_restplus import fields
from skf.api.restplus import api


kb = api.model('kb', {
    'kbID': fields.Integer(readOnly=True, description='The unique identifier of a kb item'),
    'title': fields.String(required=True, description='KB title'),
    'content': fields.String(required=True, description='KB content'),
})

kb_items = api.inherit('List of KB items', {
    'items': fields.List(fields.Nested(kb))
})

kb_update = api.model('KB update', {
    'title': fields.String(required=True, description='New KB title'),
    'content': fields.String(required=True, description='New KB content'),
})

message = api.model('Response message', {
    'message': fields.String(required=True, description='Response message'),
})

