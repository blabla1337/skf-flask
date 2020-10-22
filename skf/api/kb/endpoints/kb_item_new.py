
from flask import request
from flask_restplus import Resource
from skf.api.security import security_headers, validate_privilege
from skf.api.kb.business import create_kb_item
from skf.api.kb.serializers import kb_update, message
from skf.api.kb.parsers import authorization
from skf.api.restplus import api
from skf.api.security import log, val_num, val_alpha, val_alpha_num, val_alpha_num_special

ns = api.namespace('kb', description='Operations related to kb items')

<<<<<<< HEAD
=======

>>>>>>> origin/master
@ns.route('/new/<int:category_id>')
@api.response(404, 'Validation error', message)
class KBItemCreate(Resource):

    @api.expect(authorization, kb_update)
    @api.marshal_with(message, 'Success')
    @api.response(400, 'No results found', message)
    def put(self, category_id):
        """
        Create new kb item.
        * Privileges required: **edit**
        """
        validate_privilege(self, 'edit')
        data = request.json
        val_alpha_num_special(data.get('title'))
        result = create_kb_item(data, category_id)
        return result, 200, security_headers()

