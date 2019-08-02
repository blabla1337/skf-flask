
from flask import request
from flask_restplus import Resource
from skf.api.security import security_headers, validate_privilege, select_userid_jwt
from skf.api.questions.business import new_question
from skf.api.questions.serializers import store_list_items, message
from skf.api.questions.parsers import authorization
from skf.api.restplus import api

ns = api.namespace('questions', description='Operations related to question sprint items')


@ns.route('/item/new')
@api.response(404, 'Validation error', message)
class QuestionSprintCollection(Resource):

    @api.expect(authorization, store_list_items)
    @api.response(400, 'No results found', message)
    def put(self):
        """
        Create new questions .
        * Privileges required: **manage**
        """
        validate_privilege(self, 'manage')
        data = request.json
        result = new_question(data)
        return result, 200, security_headers()

