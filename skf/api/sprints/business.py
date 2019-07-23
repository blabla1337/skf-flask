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
from skf.database.kb_items import KBItem
from skf.database.comments import Comment


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
    result = ChecklistResult.query.filter(ChecklistResult.sprint_id == sprint_id).filter(ChecklistResult.kb_id != 0).order_by(asc(checklists_results.status)).group_by(ChecklistResult.checklist_id).paginate(1, 500, False)
    return result


def get_sprint_results_audit(sprint_id, user_id):
    log("User requested specific sprint audit items", "MEDIUM", "PASS")
    val_num(sprint_id)
    val_num(user_id)
    result = ChecklistResult.query.filter(ChecklistResult.sprint_id == sprint_id).filter(ChecklistResult.status == 5).group_by(ChecklistResult.checklist_id).group_by(ChecklistResult.checklist_id).paginate(1, 500, False)
    return result


def get_sprint_results_audit_export(sprint_id, user_id):
    log("User requested specific sprint audit export", "MEDIUM", "PASS")
    val_num(sprint_id)
    val_num(user_id)
    result = ChecklistResult.query.filter(checklists_results.sprintID == sprint_id).filter(checklists_results.status == 5).group_by(checklists_results.checklistID).group_by(checklists_results.checklistID).paginate(1, 500, False)
    return {'message': export_failed_results(result) }


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
        sprint.sprintName = data.get('name')
        sprint.sprintDesc = data.get('description')

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
    val_num(data.get('projectID'))
    sprintName = data.get('name')
    sprintDesc = data.get('description')
    projectID = data.get('projectID')

    #groupmember = groupmembers.query.filter(groupmembers.userID == user_id).one()
    #groupID = groupmember.groupID

    try:
        user = User.query.get(user_id)
        group = user.groups[0]

        sprint = ProjectSprint(sprintName, sprintDesc)
        sprint.group_id = group.id
        sprint.project_id = projectID

        db.session.add(sprint)
        db.session.commit()

    except:
         db.session.rollback()
         raise

    # somewhat funky query to obtain the id
    result = ProjectSprint.query.filter(ProjectSprint.group_id == group.id).order_by(desc(ProjectSprint.id)).first()
    return {'sprintID': result.id, 'message': 'Sprint successfully created'}


def stats_sprint(project_id):
    log("User requested specific project sprint stats", "MEDIUM", "PASS")
    val_num(project_id)
    sprint_info = (project_sprints.query.filter(project_sprints.projectID == project_id).all())
    sprint = []
    for result in sprint_info:
        sprint_id = result.sprintID
        sprint_desc = result.sprintDesc
        sprint_name = result.sprintName
        sprint_open = (checklists_results.query.filter(checklists_results.sprintID == sprint_id).filter(checklists_results.kbID > 0 ).filter(checklists_results.status == 1).group_by(checklists_results.checklistID).group_by(checklists_results.checklistID).count())
        sprint_closed = (checklists_results.query.filter(checklists_results.sprintID == sprint_id).filter(checklists_results.kbID > 0 ).filter(checklists_results.status == 2).group_by(checklists_results.checklistID).group_by(checklists_results.checklistID).count())
        sprint_accepted = (checklists_results.query.filter(checklists_results.sprintID == sprint_id).filter(checklists_results.kbID > 0 ).filter(checklists_results.status == 3).group_by(checklists_results.checklistID).group_by(checklists_results.checklistID).count())
        sprint_sec_ack = (checklists_results.query.filter(checklists_results.sprintID == sprint_id).filter(checklists_results.kbID > 0 ).filter(checklists_results.status == 4).group_by(checklists_results.checklistID).group_by(checklists_results.checklistID).count())
        sprint_sec_fail = (projects.query.filter(checklists_results.sprintID == sprint_id).filter(checklists_results.kbID > 0 ).filter(checklists_results.status == 5).group_by(checklists_results.checklistID).group_by(checklists_results.checklistID).count())
        checklist_type = projects.query.filter(projects.projectID == project_id).one()
        total = sprint_open + sprint_closed + sprint_accepted + sprint_sec_ack + sprint_sec_fail
        sprint.append({'sprint_id': sprint_id, 'sprint_desc': sprint_desc, 'sprint_name': sprint_name, 'sprint_open': sprint_open, 'sprint_closed': sprint_closed, 'sprint_accepted': sprint_accepted, 'sprint_sec_ack': sprint_sec_ack, 'sprint_sec_fail': sprint_sec_fail, 'sprint_items_total': total})
    return sprint


def export_failed_results(sprint_results):
    file_path = "export_" + id_generator(16)
    with open(file_path, 'a') as file:
        file.write('date,title,description,mitigation,notes\n')

        for item in sprint_results.items:
            checklist = checklists_kb.query.filter(checklists_kb.checklistID == item.checklistID).first()
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