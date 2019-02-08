
from flask import request
from flask_restplus import Resource
from skf.api.security import security_headers, validate_privilege, select_userid_jwt
from skf.api.questions_pre.business import new_pre_question
from skf.api.questions_pre.serializers import question_pre_item_update, message
from skf.api.questions_pre.parsers import authorization
from skf.api.restplus import api

ns = api.namespace('questions_pre', description='Operations related to question pre items')


@ns.route('/item/new')
@api.response(404, 'Validation error', message)
class QuestionPreCollection(Resource):

    @api.expect(authorization, question_pre_item_update)
    @api.response(400, 'No results found', message)
    def put(self):
        """
        Create new question pre item.
        * Privileges required: **manage**
        """
        validate_privilege(self, 'manage')
        data = request.json
        result = new_pre_question(data)
        return result, 200, security_headers()

