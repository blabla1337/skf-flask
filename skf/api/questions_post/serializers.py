from flask_restplus import fields
from skf.api.restplus import api


results = api.model('results', {
    'sprintID': fields.Integer(readOnly=True, description='The unique identifier of a sprint item'),
    'projectID': fields.Integer(required=True, description='The unique identifier of a sprint project'),
    'kb_item_title': fields.String(attribute='kb_items.title', required=True, description='Knowledge base title'),
    'kb_items_content': fields.String(attribute='kb_items.content', required=True, description='Knowledge base content'),
    'checklist_items_checklistID': fields.String(attribute='checklist_items.checklistID', required=True, description='The unique identifier of a checklist item'),
    'checklist_items_content': fields.String(attribute='checklist_items.content', required=True, description='Checklist content'),
})

post_items = api.inherit('List of question post items', {
    'items': fields.List(fields.Nested(results))
})

list_post = api.model('list_post', {
    'projectID': fields.Integer(readOnly=True, description='The unique identifier of the project'),
    'sprintID': fields.Integer(readOnly=True, description='The unique identifier of the sprint'),
    'kbID': fields.Integer(readOnly=True, description='The unique identifier of the kb item'),
    'checklistID': fields.String(readOnly=True, description='The unique identifier of the checklist item'),
    'status': fields.Integer(readOnly=True, description='The checklistID result'),
})

store_list_items_post = api.inherit('List of questions post', {
    'questions': fields.List(fields.Nested(list_post))
})

message = api.model('Response message', {
    'message': fields.String(required=True, description='Response message'),
})
 