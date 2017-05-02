import datetime

from skf.database import db
from skf.database.projects import projects
from skf.database.groupmembers import groupmembers
from skf.api.security import val_num, val_alpha, val_alpha_num

def update_project(project_id, user_id, data):
    project = projects.query.filter(projects.projectID == project_id).one()
    project.projectName = data.get('name')
    project.projectVersion = data.get('version')
    project.projectDesc = data.get('description')
    val_alpha_num(project.projectName)
    val_alpha_num(project.projectVersion)
    val_alpha_num(project.projectDesc)
    project.userID = user_id
    groupmember = groupmembers.query.filter(groupmembers.userID == userID).one()
    ownerID = groupmember.ownerID
    groupID = groupmember.groupID
    now = datetime.datetime.now()
    project.timestamp = now.strftime("%Y-%m-%d %H:%M")
    db.session.add(project)
    db.session.commit()


def new_project(user_id, data):
    projectName = data.get('name')
    projectVersion = data.get('version')
    projectDesc = data.get('description')
    val_alpha_num(projectName)
    val_alpha_num(projectVersion)
    val_alpha_num(projectDesc)
    userID = user_id
    groupmember = groupmembers.query.filter(groupmembers.userID == userID).one()
    ownerID = groupmember.ownerID
    groupID = groupmember.groupID
    now = datetime.datetime.now()
    timestamp = now.strftime("%Y-%m-%d %H:%M")
    project = projects(userID, groupID, projectName, projectVersion, projectDesc, ownerID, timestamp)
    db.session.add(project)
    db.session.commit()


def delete_project(project_id, user_id):
    project = (projects.query.filter(projects.projectID == project_id).filter(projects.userID == user_id).one())
    db.session.delete(project)
    db.session.commit()
