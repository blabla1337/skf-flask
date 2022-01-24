from flask_restplus import Resource
from skf.api.sprints.business import export_results
from skf.api.sprints.serializers import sprint_results, message
from skf.api.restplus import api
from skf.api.security import *

ns = api.namespace('sprint', description='Operations related to sprint items')

@ns.route('/results/export_external/<int:id>')
@api.doc(params={'id': 'The external project id'})
@api.response(404, 'Validation error', message)
class ProjectSprintResultExportItemExternal(Resource):

    @api.marshal_with(message, 'Null')
    @api.response(400, 'No results found', message)
    def get(self, id):
        val_num(id)
        result = export_results(id)
        return result, 200, security_headers()
