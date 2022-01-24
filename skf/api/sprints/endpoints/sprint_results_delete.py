from flask import request
from flask_restplus import Resource
from skf.api.sprints.business import delete_checklist_result
from skf.api.sprints.serializers import delete_checklist_results, message
from skf.api.restplus import api
from skf.api.security import *

ns = api.namespace('sprint', description='Operations related to sprint items')

@ns.route('/results/delete/<int:checklist_result_id>')
@api.doc(params={'id': 'checklist_results_id'})
@api.response(404, 'Validation error', message)
class ProjectSprintResultItemDelete(Resource):

    @api.marshal_with(delete_checklist_results)
    @api.response(400, 'No results found', message)
    def delete(self, checklist_result_id):
        result = delete_checklist_result(checklist_result_id)
        return result, 200, security_headers()
