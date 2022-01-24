from flask import request
from flask_restplus import Resource
from skf.api.checklist_category.business import update_checklist_category
from skf.api.checklist_category.serializers import checklist_type_update, message
from skf.api.restplus import api
from skf.api.security import *

ns = api.namespace('checklist_category', description='Operations related to checklist items')

@ns.route('/update/<int:id>')
@api.doc(params={'id': 'The checklist category id'})
@api.response(404, 'Validation error', message)
class ChecklistCategoryUpdate(Resource):

    @api.expect(checklist_type_update)
    @api.response(400, 'No results found', message)
    def put(self, id):
        data = request.json
        val_num(id)
        val_alpha_num_special(data.get('name'))
        val_alpha_num_special(data.get('description'))
        result = update_checklist_category(id, data)
        return result, 200, security_headers()
