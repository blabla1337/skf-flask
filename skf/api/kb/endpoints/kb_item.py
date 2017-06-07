
from flask import request
from flask_restplus import Resource
from skf.api.security import security_headers
from skf.api.kb.business import get_kb_item
from skf.api.kb.serializers import kb, message
from skf.api.restplus import api

ns = api.namespace('kb', description='Operations related to kb items')


@ns.route('/<int:id>')
@api.doc(params={'id': 'The kb item id'})
@api.response(404, 'Validation error', message)
class KBItem(Resource):

    @api.marshal_with(kb)
    @api.response(400, 'No results found', message)
    def get(self, id):
        """
        Returns a kb item.
        * Privileges required: **none**
        """
        result = get_kb_item(id)
        return result, 200, security_headers()

