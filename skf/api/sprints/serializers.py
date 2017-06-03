from flask_restplus import fields
from skf.api.restplus import api

sprint = api.model('sprint', {
    'sprintID': fields.Integer(readOnly=True, description='The unique identifier of a sprint item'),
    'projectID': fields.Integer(required=True, description='The unique identifier of a sprint project'),
    'groupID': fields.Integer(required=True, description='The unique identifier of a sprint group'),
    'sprintName': fields.String(required=True, description='Sprint name'),
    'sprintDesc': fields.String(required=True, description='Sprint description'),
})

sprint_stats = api.model('sprint_stats', {
    'sprint_id': fields.Integer(readOnly=True, description='The unique identifier of a sprint item'),
    'sprint_name': fields.String(required=True, description='The name of a sprint'),
    'sprint_desc': fields.String(required=True, description='The description of a sprint'),
    'sprint_open': fields.Integer(readOnly=True, description='The count of open items per sprint'),
    'sprint_closed': fields.Integer(readOnly=True, description='The count of closed items per sprint'),
    'sprint_accepted': fields.Integer(readOnly=True, description='The count of accepted items per sprint'),
    'sprint_items_total': fields.Integer(readOnly=True, description='The count of total available items in a sprint'),
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
    'projectID': fields.Integer(required=True, description='The unique identifier of a sprint project'),
})

message = api.model('Response message', {
    'message': fields.String(required=True, description='Response message'),
    'sprintID': fields.Integer(readOnly=True, description='The unique identifier of a sprint item'),  
})
