
from flask import request
from flask_restplus import Resource
from skf.api.security import security_headers, validate_privilege, select_userid_jwt
from skf.api.questions_sprint.business import update_sprint_question
from skf.api.questions_sprint.serializers import question_sprint_item_update, message
from skf.api.questions_sprint.parsers import authorization
from skf.api.restplus import api

ns = api.namespace('questions_sprint', description='Operations related to question sprint items')


@ns.route('/item/update/<int:id>')
@api.doc(params={'id': 'The unique question id'})
@api.response(404, 'Validation error', message)
class QuestionSprintCollection(Resource):

    @api.expect(authorization, question_sprint_item_update)
    @api.response(404, 'No results found', message)
    def put(self, id):
        """
        Update question sprint item.
        * Privileges required: **manage**
        """
        validate_privilege(self, 'manage')
        data = request.json
        result = update_sprint_question(id, data)
        return result, 200, security_headers()

