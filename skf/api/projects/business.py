import datetime
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
    return Project.query.paginate(1, 500, False)


def get_project_item(project_id, user_id):
    log("User requested specific project", "MEDIUM", "PASS")
    val_num(project_id)
    val_num(user_id)
    return Project.query.filter(Project.id == project_id).filter(Project.user_id == user_id).one()


def update_project(project_id, user_id, data):
    log("User updated project", "MEDIUM", "PASS")
    val_num(project_id)
    val_num(user_id)
    val_alpha_num_special(data.get('name'))
    val_alpha_num(data.get('version'))
    val_alpha_num_special(data.get('description'))
    try:
        project = Project.query.filter(Project.id == project_id).one()
        project.project_name = data.get('name')
        project.project_version = data.get('version')
        project.project_description = data.get('description')
        project.user_id = user_id
        #groupmember = groupmembers.query.filter(groupmembers.user_id == user_id).one()
        #owner_id = groupmember.owner_id
        #group_id = groupmember.group_id
        now = datetime.datetime.now()
        project.timestamp = now.strftime("%Y-%m-%d %H:%M")
        db.session.add(project) 
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        raise

    return {'message': 'Project successfully updated'}


def new_project(user_id, data):
    log("User created new project", "MEDIUM", "PASS")
    val_num(user_id)
    val_alpha_num_special(data.get('name'))
    val_alpha_num(data.get('version'))
    val_alpha_num_special(data.get('description'))
    name = data.get('name')
    version = data.get('version')
    description = data.get('description')
    now = datetime.datetime.now()
    timestamp = now.strftime("%Y-%m-%d %H:%M")
    try:
        project = Project(name, version, description, timestamp)
        db.session.add(project)
        db.session.commit()
    except:
        db.session.rollback()
        raise
    #result = Project.query.filter(Project.user_id == user_id).order_by(desc(Project.id)).first()
    # I assume we would like to return the new project ID?
    result = Project.query.filter(Project.name == name).first()
    return {'project_id': result.id, 'message': 'Project successfully created'}


def delete_project(project_id, user_id):
    log("User deleted project", "MEDIUM", "PASS")
    val_num(project_id)
    try:
        project = (Project.query.filter(Project.id == project_id).one())
        db.session.delete(project)
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        raise
    return {'message': 'Project successfully deleted'}


def stats_project(project_id):
    log("User requested specific project stats", "MEDIUM", "PASS")
    result = (ProjectSprint.query.filter(ProjectSprint.project_id == project_id).all())

    return result