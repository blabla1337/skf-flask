from flask import request
from flask_restplus import Resource
from skf.api.security import security_headers, validate_privilege
from skf.api.checklist_category.business import update_checklist_category
from skf.api.checklist_category.serializers import checklist, message
from skf.api.kb.parsers import authorization
from skf.api.restplus import api
from skf.api.security import log, val_num, val_alpha, val_alpha_num, val_alpha_num_special

ns = api.namespace('checklist_category', description='Operations related to checklist items')

@ns.route('/update/<int:id>')
@api.doc(params={'id': 'The checklist category id'})
@api.response(404, 'Validation error', message)
class ChecklistCategoryUpdate(Resource):

    @api.expect(authorization, checklist)
    @api.response(400, 'No results found', message)
    def put(self, id):
        """
        Update a checklist type.
        * Privileges required: **edit**
        """
        data = request.json
        val_num(id)
        val_alpha_num_special(data.get('name'))
        val_alpha_num_special(data.get('description'))
        validate_privilege(self, 'edit')
        result = update_checklist_category(id, data)
        return result, 200, security_headers()
