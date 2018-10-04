from flask_restplus import fields
from skf.api.restplus import api


question = api.model('question', {
    'id': fields.Integer(readOnly=True, description='The unique identifier of a question item'),
    'question': fields.String(readOnly=True, description='The question value'),
    'checklist_level': fields.String(required=True, description='The question checklist level for pre process step'),
    'checklist_type': fields.String(required=True, description='The question checklist type used for pre process step'),
})

question_items = api.inherit('List of question pre items', {
    'items': fields.List(fields.Nested(question))
})

list_pre = api.model('list_pre', {
    'projectID': fields.Integer(readOnly=True, description='The unique identifier of the project'),
    'question_pre_ID': fields.Integer(readOnly=True, description='The unique identifier of a question pre item'),
    'result': fields.String(readOnly=True, description='The question result'),
})

list_pre_update = api.model('list_pre_update', {
    'question_pre_ID': fields.Integer(readOnly=True, description='The unique identifier of a question pre item'),
    'result': fields.String(readOnly=True, description='The question result'),
})

store_list_items_pre = api.inherit('List of questions pre for store', {
    'questions': fields.List(fields.Nested(list_pre))
})

update_list_items_pre = api.inherit('List of questions pre for update', {
    'questions': fields.List(fields.Nested(list_pre_update))
})

question_pre_item = api.model('question_pre_item', {
    'checklist_type': fields.String(required=True, description='The question checklist type used for pre process step'),
})

question_pre_item_update = api.model('question_pre_item_update', {
    'question': fields.String(readOnly=True, description='The question value'),
    'checklist_type': fields.String(required=True, description='The question checklist type used for pre process step'),
})

message = api.model('Response message', {
    'message': fields.String(required=True, description='Response message'),
})
 