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


def update_checklist_result(id, user_id, data):
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
    with open("export.md", 'rb') as file:
        return {'message': base64.b64encode(file.read())}
