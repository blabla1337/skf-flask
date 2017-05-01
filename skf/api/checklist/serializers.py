from flask_restplus import fields
from skf.api.restplus import api

checklist = api.model('checklist', {
    'checklistID': fields.String(readOnly=True, description='The unique identifier of a checklist item'),
    'checklist_items.checklistID': fields.String(required=True, description='Checklist title'),
    'checklist_items.content': fields.String(required=True, description='Checklist title'),
    'checklist_items.level': fields.String(required=True, description='Checklist title'),
    'questionID': fields.String(readOnly=True, description='The unique identifier of a question item'),
    'codeID_php': fields.String(readOnly=True, description='The unique identifier of a php code item'),
    'codeID_asp': fields.String(readOnly=True, description='The unique identifier of a asp code item'),
    'codeID_java': fields.String(readOnly=True, description='The unique identifier of a java code item'),
    'codeID_python': fields.String(readOnly=True, description='The unique identifier of a python code item'),
    'kb_items.kbID': fields.String(required=True, description='Checklist title'),
    'kb_items.title': fields.String(required=True, description='Checklist content'),
    'kb_items.content': fields.String(required=True, description='Checklist title'),
})


message = api.model('Response message', {
    'message': fields.String(required=True, description='Response message'),
})
