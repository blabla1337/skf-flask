import datetime

from skf.database import db
from sqlalchemy import desc
from skf.database.groupmembers import groupmembers
from skf.database.project_sprints import project_sprints 
from skf.database.checklists_results import checklists_results 
from skf.api.security import val_num, val_alpha, val_alpha_num

def update_sprint(sprint_id, user_id, data):
    sprint = project_sprints.query.filter(project_sprints.sprintID == sprint_id).one()
    sprint.sprintName = data.get('name')
    sprint.sprintDesc = data.get('description')
    db.session.add(sprint) 
    db.session.commit()


def new_sprint(user_id, data):
    sprintName = data.get('name')
    sprintDesc = data.get('description')
    projectID = data.get('projectID')
    val_alpha_num(sprintName)
    val_alpha_num(sprintDesc)
    groupmember = groupmembers.query.filter(groupmembers.userID == user_id).one()
    ownerID = groupmember.ownerID
    groupID = groupmember.groupID
    sprintAdd = project_sprints(sprintName, sprintDesc, groupID, projectID)
    db.session.add(sprintAdd)
    db.session.commit()
    sprint = (project_sprints.query.filter(project_sprints.groupID == groupID).order_by(desc(project_sprints.sprintID)).first())
    return sprint.sprintID


def stats_sprint(project_id):
    sprint_info = (project_sprints.query.filter(project_sprints.projectID == project_id).all())
    sprint = []
    for result in sprint_info:
        sprint_id = result.sprintID
        sprint_desc = result.sprintDesc
        sprint_name = result.sprintName
        sprint_open = (checklists_results.query.filter(checklists_results.sprintID == sprint_id).filter(checklists_results.status == 1).group_by(checklists_results.checklistID).count())
        sprint_closed = (checklists_results.query.filter(checklists_results.sprintID == sprint_id).filter(checklists_results.status == 2).group_by(checklists_results.checklistID).count())
        sprint_accepted = (checklists_results.query.filter(checklists_results.sprintID == sprint_id).filter(checklists_results.status == 3).group_by(checklists_results.checklistID).count())
        sprint.append({'sprint_id': sprint_id, 'sprint_desc': sprint_desc, 'sprint_name': sprint_name, 'sprint_open': sprint_open, 'sprint_closed': sprint_closed, 'sprint_accepted': sprint_accepted})
    return sprint


def delete_sprint(sprint_id, user_id):
    sprint = (project_sprints.query.filter(project_sprints.sprintID == sprint_id).one())
    db.session.delete(sprint)
    db.session.commit()
