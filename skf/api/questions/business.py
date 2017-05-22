import datetime

from skf.database import db
from skf.database.projects import projects
from skf.database.groupmembers import groupmembers
from skf.database.question_pre_results import question_pre_results
from skf.api.security import val_num, val_alpha, val_alpha_num

def store_pre_questions(user_id, data):
    project_id = data.get('projectID')
    project = projects.query.filter(projects.projectID == project_id).one()
    userID = user_id
    groupmember = groupmembers.query.filter(groupmembers.userID == userID).one()
    if groupmember.ownerID == project.ownerID & groupmember.groupID == project.groupID:
        for result in data.get('questions'):
            question_pre_ID = result['question_pre_ID']
            question_result = result['result']
            questions = question_pre_results(project_id, question_pre_ID, question_result)
            db.session.add(questions)
            db.session.commit()


def store_sprint_questions(user_id, data):
    project_id = data.get('projectID')
    project = projects.query.filter(projects.projectID == project_id).one()
    userID = user_id
    groupmember = groupmembers.query.filter(groupmembers.userID == userID).one()
    if groupmember.ownerID == project.ownerID & groupmember.groupID == project.groupID:
        for result in data.get('questions'):
            question_sprint_ID = result['question_sprint_ID']
            question_result = result['result']
            questions = question_pre_results(project_id, question_sprint_ID, question_result)
            db.session.add(questions)
            db.session.commit()

