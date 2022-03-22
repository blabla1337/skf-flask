from flask_restplus import Resource
from skf.api.training.business import set_progress
from skf.api.training.serializers import progress, message
from skf.api.restplus import api
from skf.api.security import *

ns = api.namespace('training', description='Operations related to training items')

@ns.route('/update')
@api.response(404, 'Validation error', message)
class TrainingCourseProgressUpdate(Resource):

    @api.expect(progress)
    @api.marshal_with(message, 'Success')
    def put(self):
        data = request.json
        val_alpha_num_special(data.get('courseId'))
        val_alpha_num_special(data.get('userId'))
        val_alpha_num_special(data.get('categoryId'))
        result = set_progress(data)
        return result, 200, security_headers()
