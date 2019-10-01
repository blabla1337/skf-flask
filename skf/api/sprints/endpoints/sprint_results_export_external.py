
from flask_restplus import Resource
from skf.api.security import security_headers, validate_privilege, select_userid_jwt
from skf.api.sprints.business import export_results
from skf.api.sprints.serializers import sprint_results, message
from skf.api.sprints.parsers import authorization
from skf.api.restplus import api

ns = api.namespace('sprint', description='Operations related to sprint items')

@ns.route('/results/export_external/<int:id>')
@api.doc(params={'id': 'The external project id'})
@api.response(404, 'Validation error', message)
class ProjectSprintResultExportItemExternal(Resource):

    @api.expect(authorization)
    @api.marshal_with(message, 'Null')
    @api.response(400, 'No results found', message)
    def get(self, id):
        """
        Returns sprint export.
        * Privileges required: **read**
        """
        validate_privilege(self, 'read')
        result = export_results(id)
        return result, 200, security_headers()
