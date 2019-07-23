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


def get_project_items():
    log("User requested list projects", "MEDIUM", "PASS")
    return Project.query.filter(Project.group_id == groupmembers.group_id).paginate(1, 500, False)


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
        project.projectName = data.get('name')
        project.projectVersion = data.get('version')
        project.projectDesc = data.get('description')
        project.userID = user_id

        #groupmember = groupmembers.query.filter(groupmembers.userID == user_id).one()
        #ownerID = groupmember.ownerID
        #groupID = groupmember.groupID
        now = datetime.datetime.now()
        project.timestamp = now.strftime("%Y-%m-%d %H:%M")

        db.session.add(project) 
        db.session.commit()

    except:
        db.session.rollback()
        raise

    return {'message': 'Project successfully updated'}


def new_project(user_id, data):
    log("User created new project", "MEDIUM", "PASS")
    val_num(user_id)
    val_alpha_num_special(data.get('name'))
    val_alpha_num(data.get('version'))
    val_alpha_num_special(data.get('description'))
    projectName = data.get('name')
    projectVersion = data.get('version')
    projectDesc = data.get('description')

    now = datetime.datetime.now()
    timestamp = now.strftime("%Y-%m-%d %H:%M")

    try:
        user = User.query.get(user_id)
        owner = User.query.get(user_id)
        group = user.groups[0]

        project = Project(projectName, projectVersion, projectDesc, timestamp)
        project.owner = owner
        project.user = user
        project.group = group

        db.session.add(project)
        db.session.commit()

    except:
        db.session.rollback()
        raise

    #result = Project.query.filter(Project.user_id == user_id).order_by(desc(Project.id)).first()
    # I assume we would like to return the new project ID?
    result = Project.query.filter(Project.projectName == projectName).first()
    return {'projectID': result.id, 'message': 'Project successfully created'}


def delete_project(project_id, user_id):
    log("User deleted project", "MEDIUM", "PASS")
    val_num(project_id)
    val_num(user_id)

    try:
        project = (Project.query.filter(Project.id == project_id).filter(Project.user_id == user_id).one())

        db.session.delete(project)
        db.session.commit()

    except:
        db.session.rollback()
        raise
    return {'message': 'Project successfully deleted'}


def stats_project(project_id):
    log("User requested specific project stats", "MEDIUM", "PASS")
    sprint_info = (ProjectSprint.query.filter(ProjectSprint.project_id == project_id).all())
    sprint_open = 0
    sprint_closed = 0
    sprint_accepted = 0

    for result in sprint_info:
        sprint_id = result.sprintID
        sprint_open_add = (ChecklistResult.query.filter(ChecklistResult.sprint_id == sprint_id).filter(ChecklistResult.status == 1).group_by(ChecklistResult.checklist_id).count())
        sprint_open += sprint_open_add
        sprint_closed_add = (ChecklistResult.query.filter(ChecklistResult.sprint_id == sprint_id).filter(ChecklistResult.status == 2).group_by(ChecklistResult.checklist_id).count())
        sprint_closed += sprint_closed_add
        sprint_accepted_add = (ChecklistResult.query.filter(ChecklistResult.sprint_id == sprint_id).filter(ChecklistResult.status == 3).group_by(ChecklistResult.checklist_id).count())    
        sprint_accepted += sprint_accepted_add

    project_info = (Project.query.filter(Project.id == project_id).one())
    project_name = project_info.projectName
    project_desc = project_info.projectDesc
    project_open = sprint_open
    project_closed = (ChecklistResult.query.filter(ChecklistResult.project_id == project_id).filter(ChecklistResult.status == 2).count())
    project_accepted = (ChecklistResult.query.filter(ChecklistResult.project_id == project_id).filter(ChecklistResult.status == 3).count())
    result = {'project_id': project_id, 'project_name': project_name, 'project_desc': project_desc, 'project_open': project_open, 'project_closed': project_closed, 'project_accepted': project_accepted}
    return result