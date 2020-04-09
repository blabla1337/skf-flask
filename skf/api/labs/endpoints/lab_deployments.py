from flask import request
from flask_restplus import Resource
from skf.api.security import security_headers, select_userid_jwt, validate_privilege
from skf.api.labs.business import deploy_labs
from skf.api.labs.serializers import lab_items, message
from skf.api.restplus import api
from skf.api.kb.parsers import authorization

ns = api.namespace('interactive_labs', description='Operations related to the labs')

@api.expect(authorization)
@ns.route('/deployments/<string:instance_name>')
@api.response(404, 'Validation error', message)
class LabDeploy(Resource):

    #@api.marshal_with(lab_items)
    @api.response(400, 'No results found', message)
    def get(self, instance_name):
        """
        Returns list of labs.
        * Privileges required: **none**
        """
        userid = select_userid_jwt(self)
        validate_privilege(self, 'read')
        result = deploy_labs(instance_name, userid)
        return result, 200, security_headers()
 