import datetime
from skf.database import db
from sqlalchemy import desc
from skf.database.projects import projects 
from skf.database.groupmembers import groupmembers
from skf.database.project_sprints import project_sprints 
from skf.database.checklists_results import checklists_results
from skf.api.security import val_num, val_alpha, val_alpha_num


def update_project(project_id, user_id, data):
    project = projects.query.filter(projects.projectID == project_id).one()
    project.projectName = data.get('name')
    project.projectVersion = data.get('version')
    project.projectDesc = data.get('description')
    project.userID = user_id
    groupmember = groupmembers.query.filter(groupmembers.userID == user_id).one()
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
    project = (projects.query.filter(projects.userID == user_id).order_by(desc(projects.projectID)).first())
    return project.projectID


def delete_project(project_id, user_id):
    project = (projects.query.filter(projects.projectID == project_id).filter(projects.userID == user_id).one())
    db.session.delete(project)
    db.session.commit()


def stats_project(project_id):
    sprint_info = (project_sprints.query.filter(project_sprints.projectID == project_id).all())
    sprint_open = 0
    sprint_closed = 0
    sprint_accepted = 0
    for result in sprint_info:
        sprint_id = result.sprintID
        sprint_desc = result.sprintDesc
        sprint_name = result.sprintName
        sprint_open_add = (checklists_results.query.filter(checklists_results.sprintID == sprint_id).filter(checklists_results.status == 1).group_by(checklists_results.checklistID).count())
        sprint_open += sprint_open_add
        sprint_closed_add = (checklists_results.query.filter(checklists_results.sprintID == sprint_id).filter(checklists_results.status == 2).group_by(checklists_results.checklistID).count())
        sprint_closed += sprint_closed_add
        sprint_accepted_add = (checklists_results.query.filter(checklists_results.sprintID == sprint_id).filter(checklists_results.status == 3).group_by(checklists_results.checklistID).count())    
        sprint_accepted += sprint_accepted_add
    project_info = (projects.query.filter(projects.projectID == project_id).one())
    project_name = project_info.projectName
    project_desc = project_info.projectDesc
    project_open = sprint_open
    project_closed = (checklists_results.query.filter(checklists_results.projectID == project_id).filter(checklists_results.status == 2).count())
    project_accepted = (checklists_results.query.filter(checklists_results.projectID == project_id).filter(checklists_results.status == 3).count())
    project = {'project_id': project_id, 'project_name': project_name, 'project_desc': project_desc, 'project_open': project_open, 'project_closed': project_closed, 'project_accepted': project_accepted}
    return project