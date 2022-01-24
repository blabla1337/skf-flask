from flask import request
from flask_restplus import Resource
from skf.api.code.business import delete_code_item
from skf.api.code.serializers import message
from skf.api.restplus import api
from skf.api.security import *

ns = api.namespace('code', description='Operations related to knowledge base')

@ns.route('/delete/<int:id>')
@api.doc(params={'id': 'The code id'})
@api.response(404, 'Validation error', message)
class KnowledgebaseItemDelete(Resource):

    @api.marshal_with(message, 'Success')
    @api.response(400, 'No results found', message)
    def delete(self, id):
        result = delete_code_item(id)
        return result, 200, security_headers()