
from flask import request
from flask_restplus import Resource
from skf.api.security import log, security_headers, validate_privilege, val_num
from skf.api.code.business import update_code_item
from skf.api.code.serializers import page_of_code_items, code, code_update, message, code_lang
from skf.api.code.parsers import pagination_arguments, authorization, id_arguments
from skf.api.restplus import api
from skf.database.code_items import code_items

ns = api.namespace('code', description='Operations related to code example items')


@ns.route('/items')
class CodeCollection(Resource):

    @api.expect(pagination_arguments)
    @api.marshal_with(page_of_code_items)
    @api.response(400, 'Validation Error', message)
    def get(self):
        """
        Returns list of code example items.
        Privileges required: none
        """
        args = pagination_arguments.parse_args(request)
        page = args.get('page', 1)
        per_page = args.get('per_page', 10)
        code_query = code_items.query
        code_page = code_query.paginate(page, per_page, error_out=False)
        log("User requested list of code example items", "LOW", "PASS")
        return code_page, 200, security_headers()


@ns.route('/<int:id>')
class CodeItem(Resource):

    @api.expect(id_arguments)
    @api.marshal_with(code)
    @api.response(400, 'Validation Error', message)
    def get(self, id):
        """
        Returns a code example item.
        Privileges required: none
        """
        val_num(id)
        try:
            log("User requested specific code example item", "LOW", "PASS")
            return code_items.query.filter(code_items.codeID == id).one(), 200, security_headers()
        except:
            log("User triggered error requesting specific code example item", "LOW", "FAIL")
            return {'message': 'Validation error'}, 400, security_headers()


@ns.route('/lang/')
class CodeLangItem(Resource):

    @api.expect(code_lang)
    @api.marshal_with(page_of_code_items)
    @api.response(400, 'Validation Error', message)
    def post(self):
        """
        Returns a code example item.
        Privileges required: none
        """
        log("User requested specific code language items", "LOW", "PASS")
        data = request.json
        code_lang = data.get('code_lang')
        args = pagination_arguments.parse_args(request)
        page = args.get('page', 1)
        per_page = args.get('per_page', 10)
        code_query = (code_items.query.filter(code_items.code_lang == code_lang))
        code_page = code_query.paginate(page, per_page, error_out=False)
        return code_page, 200, security_headers()



@ns.route('/update/<int:id>')
class CodeItemUpdate(Resource):

    @api.expect(authorization, code_update)
    @api.marshal_with(message, 'Success')
    @api.response(400, 'Validation Error', message)
    def put(self, id):
        """
        Update a code example item.
        Privileges required: edit
        """
        validate_privilege(self, 'edit')
        val_num(id)
        data = request.json
        try:
            log("User requested updated specific code example item", "LOW", "PASS")
            update_code_item(id, data)
            return {'message': 'Code example item successfully updated'}, 200, security_headers()
        except:
            log("User triggered error updating specific code example item", "LOW", "FAIL")
            return {'message': 'Code example item not updated'}, 400, security_headers()
 