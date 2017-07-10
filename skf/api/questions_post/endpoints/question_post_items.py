
from flask import request
from flask_restplus import Resource
from skf.api.security import security_headers, validate_privilege, select_userid_jwt
from skf.api.questions_post.business import get_post_items
from skf.api.questions_post.serializers import post_items, message
from skf.api.questions_post.parsers import authorization
from skf.api.restplus import api

ns = api.namespace('questions_post', description='Operations related to question post items')


@ns.route('/<int:id>')
@api.doc(params={'id': 'The sprint id'})
@api.response(404, 'Validation error', message)
class QuestionPostCollection(Resource):

    @api.expect(authorization)
    @api.marshal_with(post_items)
    @api.response(400, 'No results found', message)
    def get(self, id):
        """
        Returns list of question post items.
        * Privileges required: **none**
        """
        result = get_post_items(id)
        return result, 200, security_headers()

