from flask_restplus import fields
from skf.api.restplus import api

project = api.model('project', {
    'projectID': fields.Integer(readOnly=True, description='The unique identifier of a project item'),
    'groupID': fields.Integer(required=True, description='The unique identifier of a project group'),
    'ownerID': fields.Integer(required=True, description='The unique identifier of the owner of a project'),
    'projectName': fields.String(required=True, description='Project name'),
    'projectVersion': fields.String(required=True, description='Project version'),
    'projectDesc': fields.String(required=True, description='Project description'),
    'timestamp': fields.String(required=True, description='Project timestamp'),
    'level': fields.String(required=True, description='Project checklist level'),
})

project_stats = api.model('project_stats', {
    'project_id': fields.Integer(readOnly=True, description='The unique identifier of a project item'),
    'project_name': fields.String(required=True, description='The name of a project'),
    'project_desc': fields.String(required=True, description='The description of a project'),
    'project_level': fields.Integer(readOnly=True, description='The selected ASVS level of a project item'),
    'project_open': fields.Integer(readOnly=True, description='The count of open items per project'),
    'project_closed': fields.Integer(readOnly=True, description='The count of closed items per project'),
    'project_accepted': fields.Integer(readOnly=True, description='The count of accpeted items per project'),
})

page_of_project_items = api.inherit('Page of project items', {
    'items': fields.List(fields.Nested(project))
})

project_update = api.model('Project update', {
    'name': fields.String(required=True, description='Update project name'),
    'description': fields.String(required=True, description='Update project description'),
    'level': fields.Integer(required=True, description='The selected ASVS level of a project'),
    'version': fields.String(required=True, description='Update project version'),

})

project_new = api.model('Project new', {
    'name': fields.String(required=True, description='New project name'),
    'description': fields.String(required=True, description='New project description'),
    'level': fields.Integer(required=True, description='The selected ASVS level of a project'),
    'version': fields.String(required=True, description='New project version'),

})

message = api.model('Response message', {
    'message': fields.String(required=True, description='Response message'),
    'projectID': fields.Integer(readOnly=True, description='The unique identifier of a project item'),  
})

