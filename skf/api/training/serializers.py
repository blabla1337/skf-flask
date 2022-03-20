from flask_restplus import fields
from skf.api.restplus import api

profile = api.model('Profile', {
    'id': fields.String(readonly=True, description='The unique identifier of a profile item'),
    'name': fields.String(readonly=True, description='Profile name'),
    'text': fields.String(readonly=True, description='Profile description'),
    'iconClass': fields.String(readonly=True, description='Profile icon class to display')
})

course = api.model('Course', {
    'id': fields.String(readonly=True, description='The unique identifier of a course item')
})

progress = api.model('Progress', {
    'courseId': fields.String(required=True, description='The unique identifier of a course item'),
    'userId': fields.String(required=True, description='The unique identifier of a user item'),
    'categoryId': fields.String(required=True, description='The unique identifier of a category item')
})

message = api.model('Message', {
    'message': fields.String(required=True, description='Response message'),
})

