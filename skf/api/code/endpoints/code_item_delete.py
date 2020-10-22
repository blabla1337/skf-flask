<<<<<<< HEAD
=======

>>>>>>> origin/master
from flask import request
from flask_restplus import Resource
from skf.api.security import security_headers, validate_privilege, select_userid_jwt
from skf.api.code.business import delete_code_item
from skf.api.code.serializers import message
from skf.api.code.parsers import authorization
from skf.api.restplus import api
<<<<<<< HEAD

ns = api.namespace('code', description='Operations related to knowledge base')

=======
from skf.api.security import log, val_num, val_alpha, val_alpha_num, val_alpha_num_special

ns = api.namespace('code', description='Operations related to knowledge base')

 
>>>>>>> origin/master
@ns.route('/delete/<int:id>')
@api.doc(params={'id': 'The code id'})
@api.response(404, 'Validation error', message)
class KnowledgebaseItemDelete(Resource):

    @api.expect(authorization)
    @api.marshal_with(message, 'Success')
    @api.response(400, 'No results found', message)
    def delete(self, id):
        """
        Deletes code item.
        * Privileges required: **delete**
        """
<<<<<<< HEAD
        validate_privilege(self, 'delete')
        result = delete_code_item(id)
        return result, 200, security_headers()
=======
        val_num(id)
        validate_privilege(self, 'delete')
        result = delete_code_item(id)
        return result, 200, security_headers()


>>>>>>> origin/master
