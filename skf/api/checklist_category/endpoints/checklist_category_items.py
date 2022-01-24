
from flask_restplus import Resource
from skf.api.checklist_category.business import get_checklist_categories
from skf.api.checklist_category.serializers import checklist_items, message
from skf.api.restplus import api
from skf.api.security import *

ns = api.namespace('checklist_category', description='Operations related to checklist items')

@ns.route('/items')
@api.response(404, 'Validation error', message)
class ChecklistCategoryCollection(Resource):

    @api.marshal_with(checklist_items)
    @api.response(400, 'No results found', message)
    def get(self):
        result = get_checklist_categories()
        return result, 200, security_headers()
