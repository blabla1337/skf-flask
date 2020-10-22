from flask_restplus import fields
from skf.api.restplus import api

code = api.model('code', {
    'id': fields.Integer(readOnly=True, description='The unique identifier of a code item'),
    'title': fields.String(required=True, description='Code title'),
    'content': fields.String(required=True, description='Code content'),
    'code_lang': fields.String(required=True, description='Code language'),
})

<<<<<<< HEAD

checklist_kb_code_item = api.model('code_items_checklist_kb', {
    'title': fields.String(attribute='code_items.title', required=True, description='The unique identifier of a Knowledge base item'),
    'content': fields.String(attribute='code_items.content', required=True, description='Knowledge base title'),
    'code_lang': fields.String(attribute='code_items.code_lang', required=True, description='Knowledge base title'),
})

=======
>>>>>>> origin/master
code_properties = api.model('code_update', {
    'title': fields.String(required=True, description='Code title'),
    'content': fields.String(required=True, description='Code content'),
    'code_lang': fields.String(required=True, description='Code language'),
})


code_items = api.inherit('List of code example items', {
    'items': fields.List(fields.Nested(code))
})

message = api.model('Response message', {
    'message': fields.String(required=True, description='Response message'),
})


code_items_checklist_kb_all = api.inherit('List of code example items', {
    'items': fields.List(fields.Nested(checklist_kb_code_item))
})