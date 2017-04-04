
from flask import request
from flask_restplus import Resource
from skf.api.security import log, security_headers, validate_privilege, val_num
from skf.api.kb.business import update_kb_item
from skf.api.kb.serializers import page_of_kb_items, kb, kb_update, message
from skf.api.kb.parsers import pagination_arguments, authorization
from skf.api.restplus import api
from skf.database.kb_items import kb_items

ns = api.namespace('kb/items', description='Operations related to kb items')


@ns.route('/')
class KBCollection(Resource):

    @api.expect(pagination_arguments)
    @api.marshal_with(page_of_kb_items)
    @api.response(400, 'Validation Error', message)
    def get(self):
        """
        Returns list of kb items.
        Privileges required: none
        """
        args = pagination_arguments.parse_args(request)

        page = args.get('page', 1)
        per_page = args.get('per_page', 10)

        kb_query = kb_items.query
        kb_page = kb_query.paginate(page, per_page, error_out=False)

        log("User requested list of kb items", "LOW", "PASS")
        return kb_page, 200, security_headers()


@ns.route('/<int:id>')
class KBItem(Resource):

    @api.expect(pagination_arguments)
    @api.marshal_with(kb)
    @api.response(400, 'Validation Error', message)
    def get(self, id):
        """
        Returns a kb item.
        Privileges required: none
        """
        try:
            log("User requested specific kb item", "LOW", "PASS")
            return kb_items.query.filter(kb_items.kbID == id).one(), 200, security_headers()
        except:
            log("User triggered error requesting specific kb item", "LOW", "FAIL")
            return {'message': 'Validation error'}, 400, security_headers()

@ns.route('/update/<int:id>')
class KBItemUpdate(Resource):

    @api.expect(authorization, kb_update)
    @api.marshal_with(message, 'Success')
    @api.response(400, 'Validation Error', message)
    def put(self, id):
        """
        Update a kb item.
        Privileges required: edit
        """
        validate_privilege(self, 'edit')
        data = request.json
        try:
            log("User requested updated specific kb item", "LOW", "PASS")
            update_kb_item(id, data)
            return {'message': 'KB item successfully updated'}, 200, security_headers()
        except:
            log("User triggered error updating specific kb item", "LOW", "FAIL")
            return {'message': 'KB item not updated'}, 400, security_headers()
