from flask import request
from flask_restplus import Resource
from skf.api.kb.business import update_kb_item
from skf.api.kb.serializers import kb_update, message
from skf.api.restplus import api
from skf.api.security import *

ns = api.namespace('kb', description='Operations related to kb items')

@ns.route('/update/<int:kb_id>')
@api.doc(params={'id': 'The kb item id'})
@api.response(404, 'Validation error', message)
class KBItemUpdate(Resource):

    @api.expect(kb_update)
    @api.marshal_with(message, 'Success')
    @api.response(400, 'No results found', message)
    def put(self, kb_id):
        data = request.json
        val_num(kb_id)
        val_alpha_num_special(data.get('title'))
        result = update_kb_item(kb_id, data)
        return result, 200, security_headers()

