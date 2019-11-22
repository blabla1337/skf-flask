
from flask_restplus import Resource
from skf.api.security import security_headers
from skf.api.checklist_category.business import get_checklist_category_item
from skf.api.checklist_category.serializers import checklist, message
from skf.api.restplus import api

ns = api.namespace('checklist_category', description='Operations related to checklist items')

@ns.route('/<int:id>')
@api.doc(params={'id': 'The category'})
@api.response(404, 'Validation error', message)
class ChecklistCategoryCollection(Resource):

    @api.marshal_with(checklist)
    @api.response(400, 'No results found', message)
    def get(self, id):
        """
        Returns a single checklist category.
        * Privileges required: **none**
        """
        result = get_checklist_category_item(id)
        return result, 200, security_headers()
