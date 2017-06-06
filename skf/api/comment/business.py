import datetime

from skf.database import db
from skf.database.comments import comments
from skf.database.checklists_results import checklists_results 
from skf.api.security import log, val_num, val_alpha_num


def get_comment_items(data):
    log("User requested specific comment item", "LOW", "PASS")
    val_alpha_num(data.get('checklistID'))
    val_num(data.get('sprintID'))
    sprint_id = data.get('sprintID')
    checklist_id = data.get('checklistID')
    result = comments.query.filter(comments.sprintID == sprint_id).filter(comments.checklistID == checklist_id).group_by(comments.comment).paginate(1, 50, False)
    return result


def new_comment_item(user_id, data):
    log("User requested update a specific comment item", "LOW", "PASS")
    val_num(user_id)
    val_alpha_num(data.get('checklistID'))
    val_num(data.get('sprintID'))
    val_num(data.get('status'))
    val_alpha_num(data.get('comment'))
    sprint_id = data.get('sprintID')
    checklist_id = data.get('checklistID')
    status = data.get('status')
    comment = data.get('comment')
    now = datetime.datetime.now()
    dateLog = now.strftime("%Y-%m-%d %H:%M")
    result = comments(sprint_id, checklist_id, user_id, status, comment, dateLog)
    db.session.add(result)
    db.session.commit()
    result = checklists_results.query.filter(checklists_results.sprintID == sprint_id).filter(checklists_results.checklistID == checklist_id).all()
    for row in result:
        row.status = status
        db.session.add(row)
        db.session.commit()
    return {'message': 'Comment item successfully created'} 
