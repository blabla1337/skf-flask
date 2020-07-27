from flask import request
from flask_restplus import Resource
from skf.api.security import security_headers, validate_privilege
from skf.api.code.business import get_code_items_checklist_kb
from skf.api.code.serializers import code_items_checklist_kb_all, message
from skf.api.restplus import api
from skf.api.code.parsers import authorization
from skf.api.security import log, val_num, val_alpha, val_alpha_num, val_alpha_num_special

ns = api.namespace('code', description='Operations related to code example items')

@ns.route('/items/requirements/<int:checklist_kb_id>')
@api.response(404, 'Validation error', message)
class CodeCollection(Resource):

    @api.expect(authorization)
    @api.marshal_with(code_items_checklist_kb_all)
    @api.response(400, 'No results found', message)
    def get(self, checklist_kb_id):
        """
        Returns list of code example items that have correlation with requirements.
        * Privileges required: **edit**
        """
        val_alpha_num_special(checklist_kb_id)
        validate_privilege(self, 'edit')
        result = get_code_items_checklist_kb(checklist_kb_id)
        return result, 200, security_headers()
