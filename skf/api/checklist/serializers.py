from flask_restplus import fields
from skf.api.restplus import api


checklist = api.model('checklist', {
    'kb_item_title': fields.String(attribute='kb_items.title', required=True, description='Knowledge base title'),
    'kb_items_content': fields.String(attribute='kb_items.content', required=True, description='Knowledge base content'),
    'checklist_items_checklistID': fields.String(attribute='checklist_items.checklistID', required=True, description='The unique identifier of a checklist item'),
    'checklist_items_content': fields.String(attribute='checklist_items.content', required=True, description='Checklist content'),
    'checklist_items_level': fields.Integer(attribute='checklist_items.level', required=True, description='Checklist level'),
})

checklist_items = api.inherit('List of checklist items', {
    'items': fields.List(fields.Nested(checklist))
})

message = api.model('Response message', {
    'message': fields.String(required=True, description='Response message'),
})
