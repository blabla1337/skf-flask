
from flask import request
from flask_restplus import Resource
from skf.api.security import security_headers, validate_privilege, select_userid_jwt
from skf.api.questions_sprint.business import delete_sprint_question
from skf.api.questions_sprint.serializers import question_sprint_item_update, message
from skf.api.questions_sprint.parsers import authorization
from skf.api.restplus import api

ns = api.namespace('questions_sprint', description='Operations related to question sprint items')


@ns.route('/item/delete/<int:id>')
@api.doc(params={'id': 'The unique question id'})
@api.response(404, 'Validation error', message)
class QuestionSprintDelete(Resource):

    @api.expect(authorization)
    @api.response(404, 'No results found', message)
    def delete(self, id):
        """
        Delete question sprint item.
        * Privileges required: **manage**
        """
        validate_privilege(self, 'manage')
        result = delete_sprint_question(id)
        return result, 200, security_headers()

