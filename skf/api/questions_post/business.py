import datetime

from skf.database import db
from skf.database.projects import projects
from skf.database.checklists_kb import checklists_kb
from skf.database.checklists_post import checklists_post
from skf.api.security import log, val_num, val_alpha, val_alpha_num


def get_post_items(sprint_id):
    log("User requested list of question post items", "LOW", "PASS")
    result = checklists_post.query.filter(checklists_post.sprintID == sprint_id).filter(checklists_post.status == 1).paginate(1, 500, False)
    return result


def store_post_questions(user_id, data):
    log("User stored new post question list", "MEDIUM", "PASS")
    val_num(user_id)
    for result in data.get('questions'):
        val_alpha_num(result['checklistID'])
        val_num(result['status'])
        val_num(result['projectID'])
        val_num(result['sprintID'])
        val_num(result['kbID'])
        post_checklist_id = result['checklistID']
        post_result = result['status']
        post_project_id = result['projectID']
        post_sprint_id = result['sprintID']
        post_kb_id = result['kbID']
        post = checklists_post(post_checklist_id, post_project_id, post_sprint_id, post_result, post_kb_id)
        db.session.add(post)
        db.session.commit()
    return {'message': 'Post questions successfully stored'}
