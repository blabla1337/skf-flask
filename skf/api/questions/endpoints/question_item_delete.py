
from flask import request
from flask_restplus import Resource
from skf.api.security import security_headers, validate_privilege, select_userid_jwt
from skf.api.questions.business import delete_question
from skf.api.questions.serializers import question_item_update, message
from skf.api.questions.parsers import authorization
from skf.api.restplus import api

ns = api.namespace('questions', description='Operations related to questions')


@ns.route('/item/delete/<int:id>')
@api.doc(params={'id': 'The unique question id'})
@api.response(404, 'Validation error', message)
class QuestionSprintDelete(Resource):

    @api.expect(authorization)
    @api.response(404, 'No results found', message)
    def delete(self, id):
        """
        Delete questions.
        * Privileges required: **manage**
        """
        validate_privilege(self, 'manage')
        result = delete_question(id)
        return result, 200, security_headers()

