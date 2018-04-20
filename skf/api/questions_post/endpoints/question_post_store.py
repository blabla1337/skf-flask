
from flask import request
from flask_restplus import Resource
from skf.api.security import security_headers, validate_privilege, select_userid_jwt
from skf.api.questions_post.business import store_post_questions
from skf.api.questions_post.serializers import store_list_items_post, message
from skf.api.questions_post.parsers import authorization
from skf.api.restplus import api

ns = api.namespace('questions_post', description='Operations related to question post items')


@ns.route('/store')
@api.response(404, 'Validation error', message)
class QuestionPostStoreCollection(Resource):

    @api.expect(authorization, store_list_items_post)
    @api.marshal_with(message, 'Success')
    @api.response(400, 'No results found', message)
    def put(self):
        """
        Store list of question post items.
        * Privileges required: **edit**
        """
        validate_privilege(self, 'edit')
        user_id = select_userid_jwt(self)
        data = request.json
        result = store_post_questions(user_id, data)
        return result, 200, security_headers()

