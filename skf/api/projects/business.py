import datetime
from flask import abort
from skf.database import db
from sqlalchemy import desc
from skf.database.projects import Project 
from skf.database.groupmembers import GroupMember
from skf.database.users import User
from skf.database.project_sprints import ProjectSprint 
from skf.database.checklists_results import ChecklistResult
from skf.database.groups import Group
from skf.api.security import log, val_num, val_alpha_num, val_alpha_num_special
import sys

def get_project_items():
    log("User requested list projects", "MEDIUM", "PASS")
<<<<<<< HEAD
    return Project.query.paginate(1, 2500, False)
=======
    return Project.query.paginate(1, 500, False)
>>>>>>> origin/master


def new_project(user_id, data):
    log("User created new project", "MEDIUM", "PASS")
    now = datetime.datetime.now()
    timestamp = now.strftime("%Y-%m-%d %H:%M")
    try:
        project = Project(data.get('name'), data.get('version'), data.get('description'), timestamp)
        db.session.add(project)
        db.session.commit()
    except:
        db.session.rollback()
        return abort(400, 'Project not created')
    result = Project.query.filter(Project.name == data.get('name')).first()
    return {'project_id': result.id, 'message': 'Project successfully created'}


<<<<<<< HEAD
def update_project(id, data):
    log("User requested update a specific project", "LOW", "PASS")
    try:
        project = Project.query.filter(Project.id == id).first()
        project.name = data.get('name')
        project.version = data.get('version')
        project.description = data.get('description')
        db.session.add(project)
        db.session.commit()
    except:
        db.session.rollback()
        raise
    return {'message': 'project successfully updated'} 


=======
>>>>>>> origin/master
def delete_project(project_id):
    log("User deleted project", "MEDIUM", "PASS")
    try:
        project = (Project.query.filter(Project.id == project_id).one())
        db.session.delete(project)
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        return abort(400, 'Project not deleted')
    return {'message': 'Project successfully deleted'}


def get_project_item(project_id):
    log("User requested specific project stats", "MEDIUM", "PASS")
    return Project.query.filter(Project.id == project_id).first()


def stats_project(project_id):
    log("User requested specific project stats", "MEDIUM", "PASS")
    result = (ProjectSprint.query.filter(ProjectSprint.project_id == project_id).all())
    return result