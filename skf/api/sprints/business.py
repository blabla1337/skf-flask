from skf.database import db
from sqlalchemy import asc, desc
from skf.database.groupmembers import groupmembers
from skf.database.project_sprints import project_sprints 
from skf.database.checklists_results import checklists_results 
from skf.api.security import log, val_num, val_alpha_num, val_alpha_num_special


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
    i = 0
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
            ordered_list = insertInOrder(category, category_requirement, item, ordered_list)
        elif (item.status == 2):
            ordered_closed = insertInOrder(category, category_requirement, item, ordered_closed)
        elif (item.status == 3):
            ordered_accepted = insertInOrder(category, category_requirement, item, ordered_accepted)
        elif (item.status == 4):
            ordered_verified = insertInOrder(category, category_requirement, item, ordered_verified)
        else:
            ordered_failed = insertInOrder(category, category_requirement, item, ordered_failed)
    sprint_results.items = ordered_list + ordered_closed + ordered_accepted + ordered_verified + ordered_failed
    return sprint_results


def insertInOrder(category, category_requirement, item, list):
    if (len(list) == 0):
        list.append(item)
    else:
        y = 0
        while y < len(list):
            numbers_ordered = list[y].checklistID.split('.')
            category_ordered = int(numbers_ordered[0])
            category_requirement_ordered = int(numbers_ordered[1])
            if (category < category_ordered):
                list.insert(y, item)
                break
            else:
                if (category == category_ordered):
                    if (category_requirement < category_requirement_ordered):
                        list.insert(y, item)
                        break
            y = y + 1
        if (y == len(list)):
            list.insert(y, item)
    return list

