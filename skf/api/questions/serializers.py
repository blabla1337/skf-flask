from flask_restplus import fields
from skf.api.restplus import api


question = api.model('question', {
    'id': fields.String(readOnly=True, description='The unique identifier of a question item'),
    'question': fields.String(readOnly=True, description='The question value'),
})

list_pre = api.model('list_pre', {
    'projectID': fields.String(readOnly=True, description='The unique identifier of the projectID'),
    'question_pre_ID': fields.String(readOnly=True, description='The unique identifier of a question pre item'),
    'result': fields.String(readOnly=True, description='The question result'),
})

list_pre_update = api.model('list_pre_update', {
    'question_pre_ID': fields.String(readOnly=True, description='The unique identifier of a question pre item'),
    'result': fields.String(readOnly=True, description='The question result'),
})

store_list_items_pre = api.inherit('List of questions pre for store', {
    'questions': fields.List(fields.Nested(list_pre))
})

update_list_items_pre = api.inherit('List of questions pre for update', {
    'questions': fields.List(fields.Nested(list_pre_update))
})

list_sprint = api.model('list_sprint', {
    'projectID': fields.String(readOnly=True, description='The unique identifier of the projectID'),
    'sprintID': fields.String(readOnly=True, description='The unique identifier of the sprintID'),
    'question_sprint_ID': fields.String(readOnly=True, description='The unique identifier of a question sprint item'),
    'result': fields.String(readOnly=True, description='The question result'),
})

store_list_items_sprint = api.inherit('List of questions sprint', {
    'questions': fields.List(fields.Nested(list_sprint))
})

message = api.model('Response message', {
    'message': fields.String(required=True, description='Response message'),
})
 