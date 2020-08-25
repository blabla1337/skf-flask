
from flask import request
from flask_restplus import Resource
from skf.api.security import security_headers, validate_privilege, select_userid_jwt
from skf.api.questions.business import new_question
from skf.api.questions.serializers import question_item, message
from skf.api.questions.parsers import authorization
from skf.api.restplus import api
from skf.api.security import log, val_num, val_alpha, val_alpha_num, val_alpha_num_special

ns = api.namespace('questions', description='Operations related to question sprint items')

@ns.route('/item/new')
@api.response(404, 'Validation error', message)
class QuestionSprintCollection(Resource):

    @api.expect(authorization, question_item)
    @api.response(400, 'No results found', message)
    def put(self):
        """
        Create new questions .
        * Privileges required: **edit**
        """
        data = request.json
        val_alpha_num(data.get('question'))
        validate_privilege(self, 'edit')
        result = new_question(data)
        return result, 200, security_headers()

