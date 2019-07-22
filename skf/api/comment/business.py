import datetime

from sqlalchemy import desc
from skf.database import db
from skf.database.comments import Comment
from skf.database.checklists_results import ChecklistResult 
from skf.api.security import log, val_num, val_alpha_num, val_alpha_num_special


def get_comment_items(data):
    log("User requested specific comment item", "LOW", "PASS")
    val_alpha_num(data.get('checklistID'))
    val_num(data.get('sprintID'))
    sprint_id = data.get('sprintID')
    checklist_id = data.get('checklistID')
    result = Comment.query.filter(Comment.sprint_id == sprint_id).filter(Comment.checklist_id == checklist_id).order_by(desc(Comment.date)).paginate(1, 50, False)
    return result


def new_comment_item(user_id, data):
    log("User requested update a specific comment item", "LOW", "PASS")
    val_num(user_id)
    val_alpha_num(data.get('checklistID'))
    val_num(data.get('sprintID'))
    val_num(data.get('status'))
    sprint_id = data.get('sprintID')
    checklist_id = data.get('checklistID')
    status = data.get('status')
    comment = data.get('comment')
    now = datetime.datetime.now()
    dateLog = now.strftime("%Y-%m-%d %H:%M:%S")
    result = Comment(sprint_id, checklist_id, user_id, status, comment, dateLog)
    print("--------------------------------------------------")
    db.session.add(result)
    db.session.commit()
    result = ChecklistResult.query.filter(ChecklistResult.sprint_id == sprint_id).filter(ChecklistResult.checklist_id == checklist_id).all()
    for row in result:
        row.status = status
        db.session.add(row)
        db.session.commit()
    return {'message': 'Comment item successfully created'} 
