from flask import request
from flask_restplus import Resource
from skf.api.security import security_headers, validate_privilege
from skf.api.checklist.business import create_checklist_type
from skf.api.checklist.serializers import checklist_type, message
from skf.api.kb.parsers import authorization
from skf.api.restplus import api
from skf.api.security import log, val_num, val_float, val_alpha_num, val_alpha_num_special

ns = api.namespace('checklist_types', description='Operations related to checklist types')

@ns.route('/create/<int:category_id>')
@api.response(404, 'Validation error', message)
class ChecklistCreate(Resource):

    @api.expect(authorization, checklist_type)
    @api.response(400, 'No results found', message)
    def put(self, category_id):
        """
        Create a new checklist type.
        * Privileges required: **edit**
        """
        validate_privilege(self, 'edit')
        data = request.json
        val_num(category_id)
        val_alpha_num_special(data.get('name'))
        val_alpha_num_special(data.get('description'))
        val_alpha_num_special(data.get('visibility'))
        result = create_checklist_type(data, category_id)
        return result, 200, security_headers()
