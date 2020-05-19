
from flask import request
from flask_restplus import Resource
from skf.api.security import security_headers, validate_privilege, select_userid_jwt
from skf.api.questions.business import store_questions
from skf.api.questions.serializers import store_list_items, message
from skf.api.questions.parsers import authorization
from skf.api.restplus import api
from skf.api.security import log, val_num, val_alpha, val_alpha_num, val_alpha_num_special

ns = api.namespace('questions', description='Operations related to question items')

@ns.route('/store/<int:checklist_type>/<int:maturity>')
@api.response(404, 'Validation error', message)
class QuestionSprintStoreCollection(Resource):

    @api.expect(authorization, store_list_items)
    @api.marshal_with(message, 'Success')
    @api.response(400, 'No results found', message)
    def put(self, checklist_type, maturity):
        """
        Store list of question sprint items.
        * Privileges required: **edit**
        """
        validate_privilege(self, 'edit')
        data = request.json
        result = store_questions(checklist_type, maturity, data)
        return result, 200, security_headers()
