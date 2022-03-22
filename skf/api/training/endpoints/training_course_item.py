from flask_restplus import Resource
from skf.api.training.business import get_training_course_item
from skf.api.restplus import api
from skf.api.security import *

ns = api.namespace('training', description='Operations related to training items')

@ns.route('/course/<string:course_id>')
@ns.doc(params={'course_id': 'The course id'})
class TrainingCourse(Resource):

    @api.response(400, 'No results found')
    def get(self, course_id):
        val_alpha_num_special(course_id)
        result = get_training_course_item(course_id)
        return result, 200, security_headers()
