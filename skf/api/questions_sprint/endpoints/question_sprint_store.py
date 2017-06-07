
from flask import request
from flask_restplus import Resource
from skf.api.security import security_headers, validate_privilege, select_userid_jwt
from skf.api.questions_sprint.business import store_sprint_questions
from skf.api.questions_sprint.serializers import store_list_items_sprint, message
from skf.api.questions_sprint.parsers import authorization
from skf.api.restplus import api

ns = api.namespace('questions_sprint', description='Operations related to question items')


@ns.route('/store')
@api.response(404, 'Validation error', message)
class QuestionSprintStoreCollection(Resource):

    @api.expect(authorization, store_list_items_sprint)
    @api.marshal_with(message, 'Success')
    @api.response(400, 'No results found', message)
    def put(self):
        """
        Store list of question sprint items.
        * Privileges required: **edit**
        """
        validate_privilege(self, 'edit')
        user_id = select_userid_jwt(self)
        data = request.json
        result = store_sprint_questions(user_id, data)
        return result, 200, security_headers()

