from flask_restplus import fields
from skf.api.restplus import api


comment = api.model('comment', {
    'sprintID': fields.Integer(readOnly=True, description='The unique identifier of a sprint item'),
    'checklistID': fields.String(readOnly=True, description='The unique identifier of a checklist item'),
    'userID': fields.Integer(readOnly=True, description='The unique identifier of a user'),
    'status': fields.Integer(readOnly=True, description='The status of a checklist item: 1, 2, 3'),
    'comment': fields.String(required=True, description='Comment content'),
})

comment_get = api.model('comment_get', {
    'sprintID': fields.Integer(readOnly=True, description='The unique identifier of a sprint item'),
    'checklistID': fields.String(readOnly=True, description='The unique identifier of a checklist item'),
})

comment_update = api.model('comment_update', {
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
