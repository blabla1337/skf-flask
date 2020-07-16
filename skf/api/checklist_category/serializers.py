from flask_restplus import fields
from skf.api.restplus import api

checklist = api.model('checklists_kb', {
    'id': fields.Integer(readOnly=True, description='The unique identifier of a category item'),
    'name': fields.String(required=False, description='The name of the checklist'),
    'description': fields.String(required=False, description='The maturity level'),
})

checklist_items = api.inherit('List of checklist category items', {
    'items': fields.List(fields.Nested(checklist))
})

message = api.model('Response message', {
    'message': fields.String(required=True, description='Response message'),
})
