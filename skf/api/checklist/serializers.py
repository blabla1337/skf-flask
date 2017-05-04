from flask_restplus import fields
from skf.api.restplus import api


checklist = api.model('checklist', {
    'questionID': fields.String(readOnly=True, description='The unique identifier of a question item'),
    'codeID_php': fields.String(readOnly=True, description='The unique identifier of a php code item'),
    'codeID_asp': fields.String(readOnly=True, description='The unique identifier of a asp code item'),
    'codeID_java': fields.String(readOnly=True, description='The unique identifier of a java code item'),
    'codeID_python': fields.String(readOnly=True, description='The unique identifier of a python code item'),
    'kb_item_title': fields.String(attribute='kb_items.title', required=True, description='Knowledge base title'),
    'kb_items_content': fields.String(attribute='kb_items.content', required=True, description='Knowledge base content'),
    'checklist_items_checklistID': fields.String(attribute='checklist_items.checklistID', required=True, description='The unique identifier of a checklist item'),
    'checklist_items_content': fields.String(attribute='checklist_items.content', required=True, description='Checklist content'),
    'checklist_items_level': fields.String(attribute='checklist_items.level', required=True, description='Checklist level'),
})


message = api.model('Response message', {
    'message': fields.String(required=True, description='Response message'),
})
 