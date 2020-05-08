
from flask import request
from flask_restplus import Resource
from skf.api.security import security_headers, validate_privilege, select_userid_jwt
from skf.api.sprints.business import update_checklist_result
from skf.api.sprints.serializers import update_checklist_results, message
from skf.api.sprints.parsers import authorization
from skf.api.restplus import api
from skf.api.security import log, val_num, val_alpha_num, val_alpha_num_special

ns = api.namespace('sprint', description='Operations related to sprint items')

@ns.route('/results/update/<int:checklist_result_id>')
@api.doc(params={'id': 'checklist_results_id'})
@api.response(404, 'Validation error', message)
class ProjectSprintResultItemUpdate(Resource):

    @api.expect(authorization)
    @api.marshal_with(update_checklist_results)
    @api.response(400, 'No results found', message)
    def put(self, checklist_result_id):
        """
        Deletes a checklist_result item from your sprint/feature.
        * Privileges required: **read**
        """
        validate_privilege(self, 'read')
        data = request.json
        val_alpha_num_special(data.get('evidence'))
        val_alpha_num(data.get('resolved'))
        val_num(checklist_result_id)
        result = update_checklist_result(checklist_result_id, data)
        return result, 200, security_headers()
