from flask_restplus import fields
from skf.api.restplus import api


question = api.model('question', {
    'id': fields.String(readOnly=True, description='The unique identifier of a question item'),
    'question': fields.String(readOnly=True, description='The question value'),
})

question_items = api.inherit('List of question sprint items', {
    'items': fields.List(fields.Nested(question))
})

list_sprint = api.model('list_sprint', {
    'projectID': fields.Integer(readOnly=True, description='The unique identifier of the projectID'),
    'sprintID': fields.Integer(readOnly=True, description='The unique identifier of the sprintID'),
    'question_sprint_ID': fields.Integer(readOnly=True, description='The unique identifier of a question sprint item'),
    'result': fields.String(readOnly=True, description='The question result'),
})

store_list_items_sprint = api.inherit('List of questions sprint', {
    'questions': fields.List(fields.Nested(list_sprint))
})

message = api.model('Response message', {
    'message': fields.String(required=True, description='Response message'),
})
 