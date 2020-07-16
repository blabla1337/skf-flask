from flask_restplus import fields
from skf.api.restplus import api

sprint = api.model('sprint', {
    'sprint_id': fields.Integer(readOnly=True, description='The unique identifier of a sprint item'),
    'project_id': fields.Integer(required=True, description='The unique identifier of a sprint project'),
    'group_id': fields.Integer(required=True, description='The unique identifier of a sprint group'),
    'name': fields.String(required=True, description='Sprint name'),
    'description': fields.String(required=True, description='Sprint description'),
})

sprint_stats = api.model('sprint_stats', {
    'sprint_id': fields.Integer(readOnly=True, description='The unique identifier of a sprint item'),
    'title': fields.String(required=True, description='The name of a sprint'),
    'sprint_desc': fields.String(required=True, description='The description of a sprint'),
    'sprint_items_total': fields.Integer(readOnly=True, description='The count of total available items in a sprint'),
})

page_of_sprint_items = api.inherit('Page of sprint items', {
    'items': fields.List(fields.Nested(sprint))
})

sprint_update = api.model('Sprint update', {
    'sprint_id': fields.Integer(readOnly=True, description='The unique identifier of a sprint item'),
    'name': fields.String(required=True, description='Update sprint name'),
    'description': fields.String(required=True, description='Update sprint description'),
})

sprint_new = api.model('Sprint new', {
    'name': fields.String(required=True, description='New sprint name'),
    'description': fields.String(required=True, description='New sprint description'),
    'project_id': fields.Integer(required=True, description='The unique identifier of a sprint project'),
})

results = api.model('results', {
    'id': fields.Integer(required=True, description='Knowledge base content'),
    'checklist_type': fields.String(attribute='checklist_type.name', required=True, description='Knowledge base content'),
    'status': fields.Integer(readOnly=True, description='The status of a sprint item'),
    'sprint_id': fields.Integer(readOnly=True, description='The unique identifier of a sprint item'),
    'project_id': fields.Integer(required=True, description='The unique identifier of a sprint project'),
    'checklist_id': fields.Integer(required=True, description='id from checklist_ID'),
    'checklist_items_checklist_id': fields.String(attribute='checklist_item.checklist_id', required=True, description='The unique identifier of a checklist item'),
    'checklist_items_content': fields.String(attribute='checklist_item.content', required=True, description='Checklist content'),
    'add_resources': fields.Integer(attribute='checklist_item.add_resources', required=False, description='The additional resources'),
    'kb_item_id': fields.String(attribute='kb_items.kb_id', required=True, description='Knowledge base title'),
    'kb_item_title': fields.String(attribute='kb_items.title', required=True, description='Knowledge base title'),
    'kb_items_content': fields.String(attribute='kb_items.content', required=True, description='Knowledge base content'),
    'evidence': fields.String(required=False, description='Response message'),
    'resolved': fields.String(required=False, description='Response message'),
})

sprint_results = api.inherit('Page of sprint results', {
    'items': fields.List(fields.Nested(results))
})

message = api.model('Response message', {
    'message': fields.String(required=True, description='Response message'),
    'sprint_id': fields.Integer(readOnly=True, description='The unique identifier of a sprint item'),  
})

delete_checklist_results = api.model('Response message', {
    'checklist_type_id': fields.Integer(required=True, description='Response message'),
})

update_checklist_results = api.model('Response message', {
    'id': fields.Integer(required=True, description='Response message'),
    'evidence': fields.String(required=True, description='Response message'),
    'resolved': fields.String(required=True, description='Response message'),
})
