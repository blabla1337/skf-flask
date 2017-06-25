from flask_restplus import fields
from skf.api.restplus import api


comment = api.model('comment', {
    'sprintID': fields.Integer(readOnly=True, description='The unique identifier of a sprint item'),
    'checklistID': fields.String(readOnly=True, description='The unique identifier of a checklist item'),
    'userID': fields.Integer(readOnly=True, description='The unique identifier of a user'),
    'username': fields.String(attribute='user_items.userName', required=True, description='Username of comment'),
    'status': fields.Integer(readOnly=True, description='The status of a checklist item: 1, 2, 3'),
    'comment': fields.String(required=True, description='Comment content'),
    'date': fields.String(required=True, description='date of creation comment'),
})

comment_get = api.model('comment_get', {
    'sprintID': fields.Integer(readOnly=True, description='The unique identifier of a sprint item'),
    'checklistID': fields.String(readOnly=True, description='The unique identifier of a checklist item'),
})

comment_new = api.model('comment_new', {
    'sprintID': fields.Integer(readOnly=True, description='The unique identifier of a sprint item'),
    'checklistID': fields.String(readOnly=True, description='The unique identifier of a checklist item'),
    'status': fields.Integer(readOnly=True, description='The status of a checklist item: 1, 2, 3'),
    'comment': fields.String(required=True, description='Comment content'),
})

comment_items = api.inherit('List of comment items', {
    'items': fields.List(fields.Nested(comment))
})

message = api.model('Response message', {
    'message': fields.String(required=True, description='Response message'),
})
