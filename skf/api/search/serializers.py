from flask_restplus import fields
from skf.api.restplus import api

kb = api.model('kb', {
    'kb_id': fields.Integer(readOnly=True, description='The unique identifier of a kb item'),
    'title': fields.String(required=True, description='KB title'),
    'content': fields.String(required=True, description='KB content'),
})

lab = api.model('lab', {
    'id': fields.Integer(readOnly=True, description='The unique identifier of a Lab'),
    'title': fields.String(required=True, description='lab Title'),
    'link': fields.String(required=True, description='Lab Link'),
    'level': fields.String(required=True, description='level of hardness of lab'),
    'label': fields.String(required=True, description='skf or other'),
    'has_tutorial': fields.String(required=True, description='Does this image has inline tutorial'),
})

code = api.model('code', {
    'id': fields.Integer(readOnly=True, description='The unique identifier of a code item'),
    'title': fields.String(required=True, description='Code title'),
    'content': fields.String(required=True, description='Code content'),
    'code_lang': fields.String(required=True, description='Code language'),
})

checklist = api.model('checklists_kb', {
    'kb_item_id': fields.String(attribute='kb_items.kb_id', required=True, description='The unique identifier of a Knowledge base item'),
    'kb_item_title': fields.String(attribute='kb_items.title', required=True, description='Knowledge base title'),
    'kb_items_content': fields.String(attribute='kb_items.content', required=True, description='Knowledge base content'),
    'checklist_items_id': fields.Integer(attribute='id', required=True, description='Checklist type'),
    'checklist_items_checklist_id': fields.String(attribute='checklist_id', required=True, description='The unique identifier of a checklist item'),
    'checklist_items_content': fields.String(attribute='content', required=True, description='Checklist content'),
    'checklist_items_type': fields.Integer(attribute='checklist_type', required=True, description='Checklist type'),
    'include_always': fields.String(attribute='include_always',required=True, description='Always include this checklist item'),
    'question_id': fields.Integer(attribute='question_id',required=True, description='The sprint question unique identifier this checklist belongs to'),
    'add_resources': fields.String(required=False, description='The additional resources'),
    'maturity': fields.Integer(required=False, description='The maturity level'),
})

project = api.model('project', {
    'id': fields.Integer(readOnly=True, description='The unique identifier of a project item'),
    'group_id': fields.Integer(required=True, description='The unique identifier of a project group'),
    'owner_id': fields.Integer(required=True, description='The unique identifier of the owner of a project'),
    'name': fields.String(required=True, description='Project name'),
    'version': fields.String(required=True, description='Project version'),
    'description': fields.String(required=True, description='Project description'),
    'timestamp': fields.String(required=True, description='Project timestamp'),
    'project_id': fields.Integer(required=True, description='The unique identifier of a sprint project'),
})

message = api.model('Response message', {
    'message': fields.String(required=True, description='Response message'),
})

