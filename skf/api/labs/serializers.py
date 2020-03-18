from flask_restplus import fields
from skf.api.restplus import api

labs = api.model('labs', {
    'labID': fields.Integer(readOnly=True, description='The unique identifier of a Lab'),
    'title': fields.String(required=True, description='lab Title'),
    'link': fields.String(required=True, description='Lab Link'),
    'level': fields.String(required=True, description='level of hardness of lab'),
    'image_tag': fields.String(required=True, description='the image tag of the lab'),
})

lab_items = api.inherit('List of lab items', {
    'items': fields.List(fields.Nested(labs))
})

message = api.model('Response message', {
    'message': fields.String(required=True, description='Response message'),
})

