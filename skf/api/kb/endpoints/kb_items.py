import logging

from flask import request
from flask_restplus import Resource
from skf.api.security import security_headers
from skf.api.kb.business import update_kb_item
from skf.api.kb.serializers import page_of_kb_items, kb, kb_update
from skf.api.kb.parsers import pagination_arguments
from skf.api.restplus import api
from skf.database.models import kb_items

log = logging.getLogger(__name__)

ns = api.namespace('kb/items', description='Operations related to kb items')


@ns.route('/')
class KBCollection(Resource):

    @api.expect(pagination_arguments)
    @api.marshal_with(page_of_kb_items)
    def get(self):
        """
        Returns list of kb items.
        """
        args = pagination_arguments.parse_args(request)
        page = args.get('page', 1)
        per_page = args.get('per_page', 10)

        kb_query = kb_items.query
        kb_page = kb_query.paginate(page, per_page, error_out=False)

        return kb_page, 200, security_headers()


@ns.route('/<int:id>')
class KBItem(Resource):

    @api.expect(pagination_arguments)
    @api.marshal_with(kb)
    def get(self, id):
        """
        Returns a kb item.
        """
        return kb_items.query.filter(kb_items.kbID == id).one()

    @api.expect(kb_update)
    #@api.response(200, 'KB successfully updated.')
    def put(self, id):
        """
        Updates a kb item.
        """
        data = request.json
        update_kb_item(id, data)
        return None, 204, security_headers()
