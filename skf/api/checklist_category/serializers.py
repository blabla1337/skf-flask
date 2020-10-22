from flask_restplus import fields
from skf.api.restplus import api

<<<<<<< HEAD
checklist_type_update = api.model('checklist_type_update', {
    'name': fields.String(required=False, description='The name of the checklist'),
    'description': fields.String(required=False, description='The maturity level'),
})

checklist_type = api.model('checklist_type', {
    'id': fields.Integer(readOnly=True, description='The unique identifier of the checklist type'),
    'name': fields.String(required=False, description='The name of the checklist'),
=======
checklist = api.model('checklists_kb', {
    'id': fields.Integer(readOnly=True, description='The unique identifier of a category item'),
    'name': fields.String(required=False, description='The CWE unique identifier'),
>>>>>>> origin/master
    'description': fields.String(required=False, description='The maturity level'),
})

checklist_items = api.inherit('List of checklist category items', {
<<<<<<< HEAD
    'items': fields.List(fields.Nested(checklist_type))
=======
    'items': fields.List(fields.Nested(checklist))
>>>>>>> origin/master
})

message = api.model('Response message', {
    'message': fields.String(required=True, description='Response message'),
})
