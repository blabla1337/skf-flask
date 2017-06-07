
from flask import request
from flask_restplus import Resource
from skf.api.security import security_headers, validate_privilege
from skf.api.comment.business import get_comment_items
from skf.api.comment.serializers import comment_items, comment_get, message
from skf.api.comment.parsers import authorization
from skf.api.restplus import api

ns = api.namespace('comment', description='Operations related to comment items')


@ns.route('/items')
@api.response(404, 'Validation error', message)
class CommentItem(Resource):

    @api.expect(authorization, comment_get)
    @api.marshal_with(comment_items)
    @api.response(400, 'No results found', message)
    def post(self):
        """
        Returns a comment item.
        * Privileges required: **read**
        """
        validate_privilege(self, 'read')
        data = request.json
        result = get_comment_items(data)
        return result, 200, security_headers()

