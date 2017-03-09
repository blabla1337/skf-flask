from flask_restplus import fields
from skf.api.restplus import api

project = api.model('project', {
    'projectID': fields.Integer(readOnly=True, description='The unique identifier of a project item'),
    'groupID': fields.String(required=True, description='The unique identifier of a project group'),
    'ownerID': fields.Integer(required=True, description='The unique identifier of the owner of a project'),
    'projectName': fields.String(required=True, description='Project name'),
    'projectVersion': fields.String(required=True, description='Project version'),
    'projectDesc': fields.String(required=True, description='Project description'),
    'timestamp': fields.String(required=True, description='Project timestamp'),
})

pagination = api.model('A page of results', {
    'page': fields.Integer(description='Number of this page of results'),
    'pages': fields.Integer(description='Total number of pages of results'),
    'per_page': fields.Integer(description='Number of items per page of results'),
    'total': fields.Integer(description='Total number of results'),
})

page_of_project_items = api.inherit('Page of project items', pagination, {
    'items': fields.List(fields.Nested(project))
})

project_update = api.model('Project update', {
    'name': fields.String(required=True, description='Update project name'),
    'description': fields.String(required=True, description='Update project description'),
    'version': fields.String(required=True, description='Update project version'),

})

project_new = api.model('Project new', {
    'name': fields.String(required=True, description='New project name'),
    'description': fields.String(required=True, description='New project description'),
    'version': fields.String(required=True, description='New project version'),

})

message = api.model('Response message', {
    'message': fields.String(required=True, description='Response message'),
})
