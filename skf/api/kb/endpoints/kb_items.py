
from flask import request
from flask_restplus import Resource
from skf.api.security import security_headers
from skf.api.kb.business import get_kb_items
from skf.api.kb.serializers import kb_items, message
from skf.api.restplus import api
from skf.api.security import log, val_num, val_alpha, val_alpha_num, val_alpha_num_special

ns = api.namespace('kb', description='Operations related to kb items')


@ns.route('/items/<int:category_id>')
@api.response(404, 'Validation error', message)
class KBCollection(Resource):

    @api.marshal_with(kb_items)
    @api.response(400, 'No results found', message)
    def get(self, category_id):
        """
        Returns list of kb items.
        * Privileges required: **none**
        """
        val_num(category_id)
        result = get_kb_items(category_id)
        return result, 200, security_headers()
 