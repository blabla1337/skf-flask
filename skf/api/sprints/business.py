from skf.database import db
from sqlalchemy import asc, desc
from skf.database.groupmembers import groupmembers
from skf.database.project_sprints import project_sprints 
from skf.database.checklists_results import checklists_results
from skf.database.checklists import checklists
from skf.database.kb_items import kb_items
from skf.database.comments import comments

from skf.api.security import log, val_num, val_alpha_num, val_alpha_num_special
import base64
import string
import random
from datetime import date

def get_sprint_item(sprint_id, user_id):
    log("User requested specific sprint item", "MEDIUM", "PASS")
    val_num(sprint_id)
    val_num(user_id)
    result = project_sprints.query.filter(project_sprints.sprintID == sprint_id).one()
    return result


def get_sprint_results(sprint_id, user_id):
    log("User requested specific sprint items", "MEDIUM", "PASS")
    val_num(sprint_id)
    val_num(user_id)
    result = checklists_results.query.filter(checklists_results.sprintID == sprint_id).group_by(checklists_results.checklistID).order_by(asc(checklists_results.status)).paginate(1, 500, False)
    return order_sprint_results(result)


def get_sprint_results_audit(sprint_id, user_id):
    log("User requested specific sprint audit items", "MEDIUM", "PASS")
    val_num(sprint_id)
    val_num(user_id)
    result = checklists_results.query.filter(checklists_results.sprintID == sprint_id).filter(checklists_results.status == 5).group_by(checklists_results.checklistID).paginate(1, 500, False)
    return order_sprint_results(result)


def get_sprint_results_audit_export(sprint_id, user_id):
    log("User requested specific sprint audit export", "MEDIUM", "PASS")
    val_num(sprint_id)
    val_num(user_id)
    result = checklists_results.query.filter(checklists_results.sprintID == sprint_id).filter(checklists_results.status == 5).group_by(checklists_results.checklistID).paginate(1, 500, False)
    return {'message': export_failed_results(result) }


def delete_sprint(sprint_id, user_id):
    log("User deleted sprint", "MEDIUM", "PASS")
    val_num(sprint_id)
    val_num(user_id)
    result = (project_sprints.query.filter(project_sprints.sprintID == sprint_id).one())
    db.session.delete(result)
    db.session.commit()
    return {'message': 'Sprint successfully deleted'}


def update_sprint(sprint_id, user_id, data):
    log("User updated sprint", "MEDIUM", "PASS")
    val_num(sprint_id)
    val_num(user_id)
    sprint = project_sprints.query.filter(project_sprints.sprintID == sprint_id).one()
    val_alpha_num_special(data.get('name'))
    val_alpha_num_special(data.get('description'))
    sprint.sprintName = data.get('name')
    sprint.sprintDesc = data.get('description')
    db.session.add(sprint) 
    db.session.commit()
    return {'message': 'Sprint successfully updated'}


def new_sprint(user_id, data):
    log("User created new sprint", "MEDIUM", "PASS")
    val_alpha_num_special(data.get('name'))
    val_alpha_num_special(data.get('description'))
    val_num(data.get('projectID'))
    sprintName = data.get('name')
    sprintDesc = data.get('description')
    projectID = data.get('projectID')
    groupmember = groupmembers.query.filter(groupmembers.userID == user_id).one()
    groupID = groupmember.groupID
    sprintAdd = project_sprints(sprintName, sprintDesc, groupID, projectID)
    db.session.add(sprintAdd)
    db.session.commit()
    result = project_sprints.query.filter(project_sprints.groupID == groupID).order_by(desc(project_sprints.sprintID)).first()
    return {'sprintID': result.sprintID, 'message': 'Sprint successfully created'}


def stats_sprint(project_id):
    log("User requested specific project sprint stats", "MEDIUM", "PASS")
    val_num(project_id)
    sprint_info = (project_sprints.query.filter(project_sprints.projectID == project_id).all())
    sprint = []
    for result in sprint_info:
        sprint_id = result.sprintID
        sprint_desc = result.sprintDesc
        sprint_name = result.sprintName
        sprint_open = (checklists_results.query.filter(checklists_results.sprintID == sprint_id).filter(checklists_results.status == 1).group_by(checklists_results.checklistID).group_by(checklists_results.checklistID).count())
        sprint_closed = (checklists_results.query.filter(checklists_results.sprintID == sprint_id).filter(checklists_results.status == 2).group_by(checklists_results.checklistID).group_by(checklists_results.checklistID).count())
        sprint_accepted = (checklists_results.query.filter(checklists_results.sprintID == sprint_id).filter(checklists_results.status == 3).group_by(checklists_results.checklistID).group_by(checklists_results.checklistID).count())
        sprint_sec_ack = (checklists_results.query.filter(checklists_results.sprintID == sprint_id).filter(checklists_results.status == 4).group_by(checklists_results.checklistID).group_by(checklists_results.checklistID).count())
        sprint_sec_fail = (checklists_results.query.filter(checklists_results.sprintID == sprint_id).filter(checklists_results.status == 5).group_by(checklists_results.checklistID).group_by(checklists_results.checklistID).count())
        total = sprint_open + sprint_closed + sprint_accepted + sprint_sec_ack + sprint_sec_fail
        sprint.append({'sprint_id': sprint_id, 'sprint_desc': sprint_desc, 'sprint_name': sprint_name, 'sprint_open': sprint_open, 'sprint_closed': sprint_closed, 'sprint_accepted': sprint_accepted, 'sprint_sec_ack': sprint_sec_ack, 'sprint_sec_fail': sprint_sec_fail, 'sprint_items_total': total})
    return sprint


def order_sprint_results(sprint_results):
    ordered_list = []
    ordered_closed = [] # 2
    ordered_accepted = [] # 3
    ordered_verified = [] # 4
    ordered_failed = [] # 5
    for item in sprint_results.items:
        numbers = item.checklistID.split('.')
        category = int(numbers[0])
        category_requirement = int(numbers[1])
        if (item.status == 1):
            ordered_list = insert_in_order(category, category_requirement, item, ordered_list)
        elif (item.status == 2):
            ordered_closed = insert_in_order(category, category_requirement, item, ordered_closed)
        elif (item.status == 3):
            ordered_accepted = insert_in_order(category, category_requirement, item, ordered_accepted)
        elif (item.status == 4):
            ordered_verified = insert_in_order(category, category_requirement, item, ordered_verified)
        else:
            ordered_failed = insert_in_order(category, category_requirement, item, ordered_failed)
    sprint_results.items = ordered_list + ordered_closed + ordered_accepted + ordered_verified + ordered_failed
    return sprint_results


def insert_in_order(category, category_requirement, item, status_list):
    if (len(status_list) == 0):
        status_list.append(item)
    else:
        y = 0
        while y < len(status_list):
            numbers_ordered = status_list[y].checklistID.split('.')
            category_ordered = int(numbers_ordered[0])
            category_requirement_ordered = int(numbers_ordered[1])
            if (category < category_ordered):
                status_list.insert(y, item)
                break
            else:
                if (category == category_ordered):
                    if (category_requirement < category_requirement_ordered):
                        status_list.insert(y, item)
                        break
            y = y + 1
        if (y == len(status_list)):
            status_list.insert(y, item)
    return status_list


def export_failed_results(sprint_results):
    file_path = "export_" + id_generator(16)
    with open(file_path, 'a') as file:
        file.write('date,title,description,mitigation,notes\n')

        for item in sprint_results.items:
            checklist = checklists.query.filter(checklists.checklistID == item.checklistID).first()
            kb_item = kb_items.query.filter(kb_items.kbID == item.kbID).first()
            comment = comments.query.filter(comments.sprintID == item.sprintID).filter(comments.checklistID == item.checklistID).filter(comments.status == item.status).order_by(desc(comments.id)).first()
            
            title = checklist.content.replace(',','\\,').replace('\n',' ').lstrip(' ').rstrip(' ').replace('  ',' ')
            temp = kb_item.content.replace(',','\\,').split(" Solution:")
            temp1 = temp[0].split(" Description:")
            
            description = temp1[1].replace('\n',' ').lstrip(' ').rstrip(' ').replace('  ',' ')
            mitigation = temp[1].replace('\n',' ').lstrip(' ').rstrip(' ').replace('  ',' ')
            file.write('"' + comment.date + '","' + title + '","' + description + '","' + mitigation + '","' + comment.comment.replace(',','\\,').replace('\n',' ').lstrip(' ').rstrip(' ').replace('  ',' ') + '"\n')

    with open(file_path, 'rb') as file:
        return base64.b64encode(file.read())


def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))