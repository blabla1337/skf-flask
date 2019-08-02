import base64, string, random
from skf.database import db
from sqlalchemy import asc, desc
from skf.api.security import log, val_num, val_alpha_num, val_alpha_num_special
from skf.database.groupmembers import GroupMember
from skf.database.project_sprints import ProjectSprint
from skf.database.projects import Project
from skf.database.users import User
from skf.database.checklists_results import ChecklistResult
from skf.database.checklists_kb import ChecklistKB
from skf.database.checklists_results import ChecklistResult
from skf.database.kb_items import KBItem
from skf.database.comments import Comment
import sys

def get_sprint_item(sprint_id, user_id):
    log("User requested specific sprint item", "MEDIUM", "PASS")
    val_num(sprint_id)
    val_num(user_id)
    result = ProjectSprint.query.get(sprint_id)
    return result


def get_sprint_results(sprint_id, user_id):
    log("User requested specific sprint items", "MEDIUM", "PASS")
    val_num(sprint_id)
    val_num(user_id)
    result = ChecklistResult.query.filter(ChecklistResult.sprint_id == sprint_id).filter(ChecklistResult.kb_id != 0).paginate(1, 500, False)
    return result


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


def update_sprint(sprint_id, user_id, data):
    log("User updated sprint", "MEDIUM", "PASS")
    val_num(sprint_id)
    val_num(user_id)
    val_alpha_num_special(data.get('name'))
    val_alpha_num_special(data.get('description'))

    try:
        sprint = ProjectSprint.query.get(sprint_id)
        sprint.name = data.get('name')
        sprint.description = data.get('description')

        db.session.add(sprint) 
        db.session.commit()

    except:
        db.session.rollback()
        raise

    return {'message': 'Sprint successfully updated'}


def new_sprint(user_id, data):
    log("User created new sprint", "MEDIUM", "PASS")
    name = data.get('name')
    description = data.get('description')
    project_id = data.get('project_id')

    #groupmember = groupmembers.query.filter(groupmembers.userID == user_id).one()
    #groupID = groupmember.groupID

    try:
        user = User.query.get(user_id)
        group = user.groups[0]

        sprint = ProjectSprint(name, description)
        sprint.group_id = group.id
        sprint.project_id = project_id

        db.session.add(sprint)
        db.session.commit()

    except:
         db.session.rollback()
         raise

    # somewhat funky query to obtain the id
    result = ProjectSprint.query.filter(ProjectSprint.group_id == group.id).order_by(desc(ProjectSprint.id)).first()
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
        sprint.append({'sprint_id': sprint_id, 'sprint_desc': sprint_desc, 'sprint_name': sprint_name})
    return sprint


def export_failed_results(sprint_results):
    file_path = "export_" + id_generator(16)
    with open(file_path, 'a') as file:
        file.write('date,title,description,mitigation,notes\n')

        for item in sprint_results.items:
            checklist = checklists_kb.query.filter(checklists_kb.checklist_id == item.checklist_id).first()
            kb_item = kb_items.query.filter(kb_items.kbID == item.kbID).first()
            comment = comments.query.filter(comments.sprint_id == item.sprint_id).filter(comments.checklist_id == item.checklist_id).filter(comments.status == item.status).order_by(desc(comments.id)).first()

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