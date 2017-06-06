
from flask import request
from flask_restplus import Resource
from skf.api.security import security_headers, validate_privilege, select_userid_jwt
from skf.api.comment.business import new_comment_item
from skf.api.comment.serializers import comment, comment_new, message
from skf.api.comment.parsers import authorization
from skf.api.restplus import api

ns = api.namespace('comment', description='Operations related to comment items')


@ns.route('/new')
@api.response(404, 'Validation error', message)
class CommentItemNew(Resource):

    @api.expect(authorization, comment_new)
    @api.marshal_with(message, 'Success')
    @api.response(400, 'No results found', message)
    def put(self):
        """
        Create a comment item.
        * Privileges required: **edit**
        """
        validate_privilege(self, 'edit')
        user_id = select_userid_jwt(self)
        data = request.json
        result = update_comment_item(user_id, data)
        return result, 200, security_headers()

