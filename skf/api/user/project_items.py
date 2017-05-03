
from flask import request
from flask_restplus import Resource
from skf.api.security import log, security_headers, validate_privilege, select_userid_jwt, val_num
from skf.api.projects.business import new_project, update_project, delete_project
from skf.api.projects.serializers import page_of_project_items, project, project_update, project_new, message
from skf.api.projects.parsers import pagination_arguments, authorization
from skf.api.restplus import api
from skf.database.projects import projects
from skf.database.groupmembers import groupmembers


ns = api.namespace('project/items', description='Operations related to project items')


@ns.route('/')
class ProjectCollection(Resource):

    @api.expect(authorization, pagination_arguments)
    @api.marshal_with(page_of_project_items)
    @api.response(400, 'Validation Error', message)
    def get(self):
        """
        Returns list of project items.
        Privileges required: read
        """
        validate_privilege(self, 'read')
        args = pagination_arguments.parse_args(request)
        page = args.get('page', 1)
        per_page = args.get('per_page', 10)
        project_query = (projects.query.filter(projects.groupID == groupmembers.groupID))
        project_page = project_query.paginate(page, per_page, error_out=False)
        log("User requested list projects", "MEDIUM", "PASS", self)
        return project_page, 200, security_headers()


@ns.route('/<int:id>')
class ProjectItem(Resource):

    @api.expect(authorization)
    @api.marshal_with(project)
    @api.response(400, 'Validation Error', message)
    def get(self, id):
        """
        Returns a project item.
        Privileges required: read
        """
        validate_privilege(self, 'read')
        val_num(id)
        user_id = select_userid_jwt(self)
        try:
            log("User requested specific project", "MEDIUM", "PASS", self)
            return (projects.query.filter(projects.projectID == id).filter(projects.userID == user_id).one()), 200, security_headers()
        except:
            log("User triggered error requesting specific project", "MEDIUM", "FAIL", self)
            return {'message': 'Validation error'}, 400, security_headers()


@ns.route('/update/<int:id>')
class ProjectItemUpdate(Resource):

    @api.expect(authorization, project_update)
    @api.marshal_with(message, 'Success')
    @api.response(400, 'Validation Error', message)
    def put(self, id):
        """
        Update a project item.
        Privileges required: edit
        """
        validate_privilege(self, 'edit')
        val_num(id)
        user_id = select_userid_jwt(self)
        data = request.json
        try:
            log("User updated project", "MEDIUM", "PASS", self)
            update_project(id, user_id, data)
            return {'message': 'Project successfully updated'}, 200, security_headers()
        except:
            log("User triggered error updating project", "MEDIUM", "FAIL", self)
            return {'message': 'Project not updated'}, 400, security_headers()


@ns.route('/new')
class ProjectItemNew(Resource):

    @api.expect(authorization, project_new)
    @api.marshal_with(message, 'Success')
    @api.response(400, 'Validation Error', message)
    def post(self):
        """
        Create new project item.
        Privileges required: edit
        """
        validate_privilege(self, 'edit')
        user_id = select_userid_jwt(self)
        data = request.json
        try:
            new_project(user_id, data)
            log("User created new project", "MEDIUM", "PASS", self)
            return {'message': 'Project successfully created'}, 200, security_headers()
        except:
            log("User triggered error creating new project", "MEDIUM", "FAIL", self)
            return {'message': 'Project not created'}, 400, security_headers()


@ns.route('/delete/<int:id>')
class ProjectItemDelete(Resource):

    @api.expect(authorization)
    @api.marshal_with(message, 'Success')
    @api.response(400, 'Validation Error', message)
    def delete(self, id):
        """
        Deletes project item.
        Privileges required: delete
        """
        validate_privilege(self, 'delete')
        val_num(id)
        user_id = select_userid_jwt(self)
        try:
            delete_project(id, user_id)
            log("User deleted project", "MEDIUM", "PASS", self)
            return {'message': 'Project successfully deleted'}, 200, security_headers()
        except:
            log("User triggered error deleting project", "MEDIUM", "FAIL", self)
            return {'message': 'Project not deleted'}, 400, security_headers()
