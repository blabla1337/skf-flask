from flask_restplus import fields
from skf.api.restplus import api


question = api.model('question', {
    'id': fields.String(readOnly=True, description='The unique identifier of a question item'),
    'question': fields.String(readOnly=True, description='The question value'),
})

list_pre = api.model('store_list_pre', {
    'question_pre_ID': fields.String(readOnly=True, description='The unique identifier of a question pre item'),
    'result': fields.String(readOnly=True, description='The question result'),
})

store_list_items_pre = api.inherit('List of questions pre', {
    'projectID': fields.String(readOnly=True, description='The unique identifier of the projectID'),
    'questions': fields.List(fields.Nested(list_pre))
})

update_list_items_pre = api.inherit('List of questions pre', {
    'questions': fields.List(fields.Nested(list_pre))
})

list_sprint = api.model('store_list_sprint', {
    'question_sprint_ID': fields.String(readOnly=True, description='The unique identifier of a question sprint item'),
    'result': fields.String(readOnly=True, description='The question result'),
})

store_list_items_sprint = api.inherit('List of questions sprint', {
    'sprintID': fields.String(readOnly=True, description='The unique identifier of the sprintID'),
    'projectID': fields.String(readOnly=True, description='The unique identifier of the projectID'),
    'questions': fields.List(fields.Nested(list_sprint))
})

message = api.model('Response message', {
    'message': fields.String(required=True, description='Response message'),
})
 