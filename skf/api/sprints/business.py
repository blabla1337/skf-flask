import base64, string, random, requests, sys
from skf import settings
from flask import abort
from skf.database import db
from sqlalchemy import asc, desc
from skf.database.groupmembers import GroupMember
from skf.database.project_sprints import ProjectSprint
from skf.database.projects import Project
from skf.database.users import User
from skf.database.checklists_results import ChecklistResult
from skf.database.checklists_kb import ChecklistKB
from skf.database.checklist_types import ChecklistType
from skf.database.kb_items import KBItem
from skf.api.security import log


def get_sprint_item(sprint_id):
    log("User requested specific sprint item", "MEDIUM", "PASS")
    result = ProjectSprint.query.get(sprint_id)
    return result


def get_sprint_results(sprint_id):
    log("User requested specific sprint items", "MEDIUM", "PASS")
    result = ChecklistResult.query.filter(ChecklistResult.sprint_id == sprint_id).order_by(asc(ChecklistResult.checklist_id)).paginate(1, 500, False)
    return result

def update_sprint(sprint_id, data):
    log("User updated sprint", "MEDIUM", "PASS")
    try:
        sprint = ProjectSprint.query.get(sprint_id)
        sprint.name = data.get('name')
        sprint.description = data.get('description')
        db.session.add(sprint) 
        db.session.commit()
    except:
        db.session.rollback()
        return abort(400, 'Sprint not successfully updated')
    return {'message': 'Sprint successfully updated'}


def new_sprint(data):
    log("User created new sprint", "MEDIUM", "PASS")    
    try:
        sprint = ProjectSprint(data.get('name'), data.get('description'))
        sprint.group_id = 1
        sprint.project_id = data.get('project_id')
        sprint.checklist_type_id = data.get('checklist_type_id')
        db.session.add(sprint)
        db.session.commit()
    except:
        db.session.rollback()
        return abort(400, 'Sprint not successfully created')
    result = ProjectSprint.query.order_by(desc(ProjectSprint.sprint_id)).first()
    return {'sprint_id': result.sprint_id, 'message': 'Sprint successfully created'}
    

def stats_sprint(project_id):
    log("User requested specific project sprint stats", "MEDIUM", "PASS")
    sprint_info = ProjectSprint.query.filter(ProjectSprint.project_id == project_id).all()
    sprint = []
    for result in sprint_info:
        sprint_id = result.sprint_id
        sprint_desc = result.description
        sprint_name = result.name
        total = ChecklistResult.query.filter(ChecklistResult.sprint_id == sprint_id).count()
        sprint.append({'sprint_id': sprint_id, 'sprint_desc': sprint_desc, 'title': sprint_name, 'sprint_items_total': total })
    return sprint


def delete_sprint(sprint_id):
    log("User deleted sprint", "MEDIUM", "PASS")
    try:
        result = ProjectSprint.query.get(sprint_id)
        db.session.delete(result)
        db.session.commit()
    except:
        db.session.rollback()
        return abort(400, 'Sprint not successfully deleted')
    return {'message': 'Sprint successfully deleted'}

def delete_checklist_result(id):
    log("User deleted sprint", "MEDIUM", "PASS")
    try:
        result = ChecklistResult.query.get(id)
        db.session.delete(result)
        db.session.commit()
    except:
        db.session.rollback()
        return abort(400, 'checklist result successfully deleted')
    return {'message': 'checklist result successfully deleted'}


def update_checklist_result(id, data):
    log("User deleted sprint", "MEDIUM", "PASS")
    resolved = convert_boolean_type(data.get("resolved"))
    try:
        result = ChecklistResult.query.get(id)
        result.evidence = data.get("evidence")
        result.resolved = resolved
        db.session.add(result)
        db.session.commit()
    except:
        db.session.rollback()
        return abort(400, 'checklist result not successfully updated')
    return {'message': 'checklist result successfully updated'}


def convert_boolean_type(refine):
    if refine == "True":
        refine = True
    else:
        refine = False
    return refine

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
    with open("export.csv", 'rb') as file:
        return {'message': base64.b64encode(file.read())}
