from flask_restplus import fields
from skf.api.restplus import api


question = api.model('question', {
    'id': fields.String(readOnly=True, description='The unique identifier of a question item'),
    'question': fields.String(readOnly=True, description='The question value'),
})

message = api.model('Response message', {
    'message': fields.String(required=True, description='Response message'),
})
 