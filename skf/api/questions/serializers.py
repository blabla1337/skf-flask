from flask_restplus import fields
from skf.api.restplus import api


question = api.model('question', {
    'id': fields.Integer(readOnly=True, description='The unique identifier of a question item'),
    'question': fields.String(readOnly=True, description='The question value'),
    'checklist_type': fields.Integer(required=True, description='The question checklist type used for post process step'),
})

question_items = api.inherit('List of question sprint items', {
    'items': fields.List(fields.Nested(question))
})

list = api.model('list', {
    'project_id': fields.Integer(readOnly=True, description='The unique identifier of the project'),
    'sprint_id': fields.Integer(readOnly=True, description='The unique identifier of the sprint'),
    'question_id': fields.Integer(readOnly=True, description='The unique identifier of a question sprint item'),
    'result': fields.String(readOnly=True, description='The question result'),
    'checklist_type': fields.Integer(required=True, description='The question checklist type used for post process step'),
})

store_list_items = api.inherit('List of questions sprint', {
    'questions': fields.List(fields.Nested(list))
})

question_item = api.model('question_item', {
    'question': fields.String(readOnly=True, description='The question value'),
    'checklist_type': fields.Integer(required=True, description='The question checklist type used for sprint process step'),
})

message = api.model('Response message', {
    'message': fields.String(required=True, description='Response message'),
})
 