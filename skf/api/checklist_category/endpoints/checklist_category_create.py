from flask import request
from flask_restplus import Resource
from skf.api.checklist_category.business import create_checklist_category
from skf.api.checklist_category.serializers import checklist_type, message
from skf.api.restplus import api
from skf.api.security import *

ns = api.namespace('checklist_category', description='Operations related to checklist category')

@ns.route('/new')
@api.response(404, 'Validation error', message)
class ChecklistCategoryCreate(Resource):

    @api.expect(checklist_type)
    @api.response(400, 'No results found', message)
    def put(self):

        data = request.json
        val_alpha_num_special(data.get('name'))
        val_alpha_num_special(data.get('description'))
        result = create_checklist_category(data)
        return result, 200, security_headers()
