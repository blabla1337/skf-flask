import base64, string, random
from skf import settings
from skf.database import db
from sqlalchemy import asc, desc
from skf.api.security import log, val_num, val_alpha_num, val_alpha_num_special
from skf.database.groupmembers import GroupMember
from skf.database.project_sprints import ProjectSprint
from skf.database.projects import Project
from skf.database.users import User
from skf.database.checklists_results import ChecklistResult
from skf.database.checklists_kb import ChecklistKB
from skf.database.checklist_types import ChecklistType
from skf.database.kb_items import KBItem
import requests
import sys

def get_sprint_item(sprint_id, user_id):
    log("User requested specific sprint item", "MEDIUM", "PASS")
    val_num(sprint_id)
    result = ProjectSprint.query.get(sprint_id)
    return result


def get_sprint_results(sprint_id, user_id):
    log("User requested specific sprint items", "MEDIUM", "PASS")
    val_num(sprint_id)
    result = ChecklistResult.query.filter(ChecklistResult.sprint_id == sprint_id).order_by(asc(ChecklistResult.checklist_id)).paginate(1, 500, False)
    return result

def update_sprint(sprint_id, user_id, data):
    log("User updated sprint", "MEDIUM", "PASS")
    val_num(sprint_id)
    val_alpha_num_special(data.get('name'))
    val_alpha_num_special(data.get('description'))
    name = data.get('name')
    description = data.get('description')

    try:
        sprint = ProjectSprint.query.get(sprint_id)
        sprint.name = name
        sprint.description = description
        db.session.add(sprint) 
        db.session.commit()

    except:
        db.session.rollback()
        raise

    return {'message': 'Sprint successfully updated'}


def new_sprint(user_id, data):
    log("User created new sprint", "MEDIUM", "PASS")
    
    val_alpha_num_special(data.get('name'))
    val_alpha_num_special(data.get('description'))
    val_num(data.get('project_id'))
    #val_num(data.get('checklist_type_id'))
    
    name = data.get('name')
    description = data.get('description')
    project_id = data.get('project_id')
    checklist_type_id = data.get('checklist_type_id')

    #groupmember = groupmembers.query.filter(groupmembers.userID == user_id).one()
    #groupID = groupmember.groupID

    try:
        user = User.query.get(user_id)
        #group = user.groups[0]
        sprint = ProjectSprint(name, description)
        sprint.group_id = 1
        sprint.project_id = project_id
        sprint.checklist_type_id = checklist_type_id
        db.session.add(sprint)
        db.session.commit()

    except:
         db.session.rollback()
         raise

    # somewhat funky query to obtain the id
    result = ProjectSprint.query.order_by(desc(ProjectSprint.id)).first()
    return {'sprint_id': result.id, 'message': 'Sprint successfully created'}

def stats_sprint(project_id):
    log("User requested specific project sprint stats", "MEDIUM", "PASS")
    val_num(project_id)
    sprint_info = ProjectSprint.query.filter(ProjectSprint.project_id == project_id).all()
    sprint = []
    for result in sprint_info:
        sprint_id = result.id
        sprint_desc = result.description
        sprint_name = result.name
        total = ChecklistResult.query.filter(ChecklistResult.sprint_id == sprint_id).count()
        sprint.append({'sprint_id': sprint_id, 'sprint_desc': sprint_desc, 'title': sprint_name, 'sprint_items_total': total })
    return sprint

def delete_sprint(sprint_id, user_id):
    log("User deleted sprint", "MEDIUM", "PASS")
    val_num(sprint_id)
    val_num(user_id)
    try:
        result = ProjectSprint.query.get(sprint_id)
        db.session.delete(result)
        db.session.commit()
    except:
        db.session.rollback()
        raise

    return {'message': 'Sprint successfully deleted'}

def delete_checklist_result(id, user_id):
    log("User deleted sprint", "MEDIUM", "PASS")
    val_num(id)
    val_num(user_id)
    try:
        result = ChecklistResult.query.get(id)
        db.session.delete(result)
        db.session.commit()
    except:
        db.session.rollback()
        raise
    return {'message': 'checklist result successfully deleted'}


def export_results(sprint_results):
    results = ChecklistResult.query.filter(ChecklistResult.sprint_id == sprint_results).order_by(ChecklistResult.checklist_type_id).all()
    file_path = "export.csv"
    with open(file_path, 'w+') as file:
        file.write('title,description,mitigation\n')
        for item in results:
            if item.kb_id != 1:
                if item.checklist_type_id != None:
                    name = ChecklistType.query.filter(ChecklistType.id == item.checklist_type_id).first()
                    checklistName = name.name
                else:
                    checklistName = "Removed"
                checklist = ChecklistKB.query.filter(ChecklistKB.id == item.checklist_id).first()
                kb_item = KBItem.query.filter(KBItem.kb_id == item.kb_id).first()
                title = checklist.content.replace(',','\\,').replace('\n',' ').lstrip(' ').rstrip(' ').replace('  ',' ')
                if kb_item != None:
                    try:
                        temp = kb_item.content.replace(',','\\,').split("Solution:")
                        temp1 = temp[0].split("Description:")
                        description = temp1[1].replace('\n',' ').lstrip(' ').rstrip(' ').replace('  ',' ')
                        mitigation = temp[1].replace('\n',' ').lstrip(' ').rstrip(' ').replace('  ',' ')
                    except:
                        description = "empty"
                        mitigation = "empty"
                else:
                    description = "empty"
                    mitigation = "empty"
                file.write('"' + checklistName + ' : ' + title + '","' + description + '","' + mitigation + '"\n')
    with open(file_path, 'rb') as file:
        return {'message': base64.b64encode(file.read())}
