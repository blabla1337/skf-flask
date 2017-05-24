
from flask import request
from flask_restplus import Resource
from skf.api.security import log, security_headers, validate_privilege, select_userid_jwt, val_num
from skf.api.sprints.business import new_sprint, update_sprint, delete_sprint
from skf.api.sprints.serializers import sprint, sprint_update, sprint_new, message
from skf.api.sprints.parsers import authorization
from skf.api.restplus import api
from skf.database.project_sprints import project_sprints
from skf.database.groupmembers import groupmembers


ns = api.namespace('sprint', description='Operations related to sprint items')


@ns.route('/<int:id>')
class ProjectSprintItem(Resource):

    @api.expect(authorization)
    @api.marshal_with(sprint)
    @api.response(400, 'Validation Error', message)
    def get(self, id):
        """
        Returns a sprint item.
        Privileges required: read
        """
        validate_privilege(self, 'read')
        val_num(id)
        user_id = select_userid_jwt(self)
        try:
            log("User requested specific sprint", "MEDIUM", "PASS")
            return (project_sprints.query.filter(project_sprints.projectID == id).all()), 200, security_headers()
        except:
            log("User triggered error requesting specific sprint", "MEDIUM", "FAIL")
            return {'message': 'Validation error'}, 400, security_headers()


@ns.route('/update/<int:id>')
class ProjectSprintItemUpdate(Resource):

    @api.expect(authorization, sprint_update)
    @api.marshal_with(message, 'Success')
    @api.response(400, 'Validation Error', message)
    def put(self, id):
        """
        Update a sprint item.
        Privileges required: edit
        """
        validate_privilege(self, 'edit')
        val_num(id)
        user_id = select_userid_jwt(self)
        data = request.json
        try:
            log("User updated sprint", "MEDIUM", "PASS")
            update_sprint(id, user_id, data)
            return {'message': 'Sprint successfully updated'}, 200, security_headers()
        except:
            log("User triggered error updating sprint", "MEDIUM", "FAIL")
            return {'message': 'Sprint not updated'}, 400, security_headers()


@ns.route('/new')
class ProjectSprintItemNew(Resource):

    @api.expect(authorization, sprint_new)
    @api.marshal_with(message, 'Success')
    @api.response(400, 'Validation Error', message)
    def put(self):
        """
        Create new sprint item.
        Privileges required: edit
        """
        validate_privilege(self, 'edit')
        user_id = select_userid_jwt(self)
        data = request.json
        try:
            sprintID = new_sprint(user_id, data)
            log("User created new sprint", "MEDIUM", "PASS")
            return {'sprintID': sprintID, 'message': 'Sprint successfully created'}, 200, security_headers()
        except:
            log("User triggered error creating new sprint", "MEDIUM", "FAIL")
            return {'message': 'Sprint not created'}, 400, security_headers()


@ns.route('/delete/<int:id>')
class ProjectSprintItemDelete(Resource):

    @api.expect(authorization)
    @api.marshal_with(message, 'Success')
    @api.response(400, 'Validation Error', message)
    def delete(self, id):
        """
        Deletes sprint item.
        Privileges required: delete
        """
        validate_privilege(self, 'delete')
        val_num(id)
        user_id = select_userid_jwt(self)
        try:
            delete_sprint(id, user_id)
            log("User deleted sprint", "MEDIUM", "PASS")
            return {'message': 'Sprint successfully deleted'}, 200, security_headers()
        except:
            log("User triggered error deleting sprint", "MEDIUM", "FAIL")
            return {'message': 'Sprint not deleted'}, 400, security_headers()
