from flask_restplus import fields
from skf.api.restplus import api

project = api.model('project', {
    'id': fields.Integer(readOnly=True, description='The unique identifier of a project item'),
    'group_id': fields.Integer(required=True, description='The unique identifier of a project group'),
    'owner_id': fields.Integer(required=True, description='The unique identifier of the owner of a project'),
    'name': fields.String(required=True, description='Project name'),
    'version': fields.String(required=True, description='Project version'),
    'description': fields.String(required=True, description='Project description'),
    'timestamp': fields.String(required=True, description='Project timestamp'),
})

project_stats = api.model('project_stats', {
    'id': fields.Integer(readOnly=True, description='The unique identifier of a project item'),
    'name': fields.String(required=True, description='The name of a project'),
    'description': fields.String(required=True, description='The description of a project'),
    'type': fields.Integer(readOnly=True, description='The selected type of checklist of a project item'),
 })

page_of_project_items = api.inherit('Page of project items', {
    'items': fields.List(fields.Nested(project))
})

project_new = api.model('Project new', {
    'name': fields.String(required=True, description='New project name'),
    'description': fields.String(required=True, description='New project description'),
    'version': fields.String(required=True, description='New project version'),
})


project_update = api.model('Project new', {
    'name': fields.String(required=True, description='New project name'),
    'description': fields.String(required=True, description='New project description'),
    'version': fields.String(required=True, description='New project version'),
})

message = api.model('Response message', {
    'message': fields.String(required=True, description='Response message'),
    'id': fields.Integer(readOnly=True, description='The unique identifier of a project item'),  
})

