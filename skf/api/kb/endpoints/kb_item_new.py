from flask import request
from flask_restplus import Resource
from skf.api.kb.business import create_kb_item
from skf.api.kb.serializers import kb_update, message
from skf.api.restplus import api
from skf.api.security import *

ns = api.namespace('kb', description='Operations related to kb items')

@ns.route('/new/<int:category_id>')
@api.response(404, 'Validation error', message)
class KBItemCreate(Resource):

    @api.expect(kb_update)
    @api.marshal_with(message, 'Success')
    @api.response(400, 'No results found', message)
    def put(self, category_id):
        data = request.json
        val_alpha_num_special(data.get('title'))
        result = create_kb_item(data, category_id)
        return result, 200, security_headers()

