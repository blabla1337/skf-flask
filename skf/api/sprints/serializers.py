from flask_restplus import fields
from skf.api.restplus import api

sprint = api.model('sprint', {
    'sprintID': fields.Integer(readOnly=True, description='The unique identifier of a sprint item'),
    'projectID': fields.String(required=True, description='The unique identifier of a sprint project'),
    'groupID': fields.String(required=True, description='The unique identifier of a sprint group'),
    'sprintName': fields.String(required=True, description='Sprint name'),
    'sprintDesc': fields.String(required=True, description='Sprint description'),
})

page_of_sprint_items = api.inherit('Page of sprint items', {
    'items': fields.List(fields.Nested(sprint))
})

sprint_update = api.model('Sprint update', {
    'sprintID': fields.Integer(readOnly=True, description='The unique identifier of a sprint item'),
    'name': fields.String(required=True, description='Update sprint name'),
    'description': fields.String(required=True, description='Update sprint description'),
})

sprint_new = api.model('Sprint new', {
    'name': fields.String(required=True, description='New sprint name'),
    'description': fields.String(required=True, description='New sprint description'),
    'projectID': fields.String(required=True, description='The unique identifier of a sprint project'),
})

message = api.model('Response message', {
    'message': fields.String(required=True, description='Response message'),
})
