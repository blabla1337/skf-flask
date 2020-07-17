from flask_restplus import fields
from skf.api.restplus import api


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

checklist_update = api.model('checklist_update', {
    'kb_id': fields.Integer(attribute='kb_items.kb_id', required=True, description='The unique identifier of a Knowledge base item'),
    'kb_title': fields.String(attribute='kb_items.title', required=False, description='Knowledge base title'),
    'kb_content': fields.String(attribute='kb_items.content', required=False, description='Knowledge base content'),
    'id': fields.Integer(attribute='id', required=False, description='Checklist type'),
    'checklist_id': fields.String(attribute='checklist_id', required=False, description='The unique identifier of a checklist item'),
    'content': fields.String(attribute='content', required=True, description='Checklist content'),
    'checklist_type': fields.Integer(attribute='checklist_type', required=False, description='Checklist type'),
    'include_always': fields.String(attribute='include_always',required=True, description='Always include this checklist item'),
    'question_id': fields.Integer(attribute='question_id',required=True, description='The sprint question unique identifier this checklist belongs to'),
    'add_resources': fields.String(required=False, description='The additional resources'),
    'maturity': fields.Integer(required=False, description='The maturity level'),
    'questions': fields.String(attribute='questions.question', required=False, description='correlated question!'),
})

checklist_correlation = api.model('checklist_correlation', {
    'question_id': fields.Integer(attribute='question_id',required=True, description='correlate a new question id to the checklist item'),
})

checklist_questions = api.model('checklists_kb', {
    'kb_item_id': fields.String(attribute='kb_items.kb_id', required=True, description='The unique identifier of a Knowledge base item'),
    'kb_item_title': fields.String(attribute='kb_items.title', required=True, description='Knowledge base title'),
    'kb_items_content': fields.String(attribute='kb_items.content', required=True, description='Knowledge base content'),
    'checklist_items_id': fields.Integer(attribute='id', required=True, description='Checklist type'),
    'checklist_items_checklist_id': fields.String(attribute='checklist_id', required=True, description='The unique identifier of a checklist item'),
    'checklist_items_content': fields.String(attribute='content', required=True, description='Checklist content'),
    'checklist_items_type': fields.Integer(attribute='checklist_type', required=True, description='Checklist type'),
    'include_always': fields.String(attribute='include_always',required=True, description='Always include this checklist item'),
    'question_id': fields.Integer(attribute='question_id',required=True, description='The sprint question unique identifier this checklist belongs to'),
    'questions': fields.String(attribute='questions.question', required=True, description='correlated question!'),
})

checklist_items = api.inherit('List of checklist items', {
    'items': fields.List(fields.Nested(checklist))
})

checklist_items_questions = api.inherit('List of checklist items', {
    'items': fields.List(fields.Nested(checklist_questions))
})

checklist_type = api.model('checklist_type_create', {
    'name': fields.String(required=True, description='Name of the new checklist'),
    'description': fields.String(required=True, description='Description of the checklist type'),
})

checklist_types = api.model('checklist_types', {
    'id': fields.Integer(readOnly=True, description='The unique identifier of the checklist type'),
    'title': fields.String(attribute='name', required=True, description='Name of the checklist type'),
    'description': fields.String(required=True, description='Description of the checklist type'),
    'visibility': fields.String(required=True, description='visibility of the checklist type'),
})

checklist_type_items = api.inherit('List of checklist types', {
    'items': fields.List(fields.Nested(checklist_types))
})

checklist_create = api.model('checklist_create', {
    'content': fields.String(required=True, description='Checklist content'),
    'kb_id': fields.Integer(required=False, description='The unique identifier of a kb item for this checklist item'),
    'include_always': fields.String(required=True, description='Always include this checklist item'),
    'question_id': fields.Integer(required=False, description='The sprint question unique identifier this checklist belongs to'),
    'add_resources': fields.String(required=False, description='The additional resources'),
    'maturity': fields.Integer(required=False, description='The maturity level'),
})

message = api.model('Response message', {
    'message': fields.String(required=True, description='Response message'),
})
