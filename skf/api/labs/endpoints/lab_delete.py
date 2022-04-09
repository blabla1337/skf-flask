from flask import request
from flask_restplus import Resource
from skf.api.labs.business import delete_labs
from skf.api.labs.serializers import lab_user_id, message
from skf.api.restplus import api
from skf.api.security import *

import json

ns = api.namespace('interactive_labs', description='Operations related to the labs')

@ns.route('/delete-deployments/<int:instance_id>')
@api.response(404, 'Validation error', message)
class LabDelete(Resource):

    @api.expect(lab_user_id)
    @api.response(400, 'No results found', message)
    def post(self, instance_id):
        data = request.json
        user_id = data.get('user_id')
        val_num(instance_id)
        val_alpha_num_special(user_id)
        result = delete_labs(instance_id, user_id)
        return result, 200, security_headers()
 