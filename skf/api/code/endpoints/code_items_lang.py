
from flask import request
from flask_restplus import Resource
from skf.api.security import security_headers
from skf.api.code.business import get_code_items_lang
from skf.api.code.serializers import code_items, message
from skf.api.restplus import api

ns = api.namespace('code', description='Operations related to code example items')


@ns.route('/lang/<string:code_lang>')
@api.doc(params={'code_lang': 'The code lang type'})
@api.response(404, 'Validation error')
class CodeLangItem(Resource):

    @api.marshal_with(code_items)
    @api.response(400, 'No results found', message)
    def get(self, code_lang):
        """
        Returns a code example item.
        * Privileges required: **none**
        """
        result = get_code_items_lang(code_lang)
        return result, 200, security_headers()

