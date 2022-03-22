from flask_restplus import Resource
from skf.api.training.business import get_progress
from skf.api.restplus import api
from skf.api.security import *

ns = api.namespace('training', description='Operations related to training items')

@ns.route('/course/<string:course_id>/progress/<string:user_id>')
@ns.doc(params={'course_id': 'The course id'})
@ns.doc(params={'user_id': 'The user id'})
class TrainingCourseProgress(Resource):

    @api.response(400, 'No results found')
    def get(self, course_id, user_id):
        val_alpha_num_special(course_id)
        val_alpha_num_special(user_id)
        result = get_progress(course_id, user_id)
        return result, 200, security_headers()
