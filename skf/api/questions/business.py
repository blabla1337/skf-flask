import datetime

from sqlalchemy import distinct
from skf.database import db
from skf.database.projects import projects
from skf.database.groupmembers import groupmembers
from skf.database.checklists_kb import checklists_kb
from skf.database.checklists_results import checklists_results
from skf.database.question_pre_results import question_pre_results
from skf.database.question_sprint_results import question_sprint_results
from skf.api.security import val_num, val_alpha, val_alpha_num

def store_pre_questions(user_id, data):
    question = data.get('questions')
    project_id = question[0]['projectID']
    project = projects.query.filter(projects.projectID == project_id).one()
    userID = user_id
    groupmember = groupmembers.query.filter(groupmembers.userID == userID).one()
    if groupmember.ownerID == project.ownerID & groupmember.groupID == project.groupID:
        for result in data.get('questions'):
            question_pre_ID = result['question_pre_ID']
            question_result = result['result']
            question_project_id = result['projectID']
            questions = question_pre_results(question_project_id, question_pre_ID, question_result)
            db.session.add(questions)
            db.session.commit()
            questions_results = question_pre_results.query.filter(question_pre_results.result == "False").group_by(question_pre_results.question_pre_ID).all()
        for results in questions_results:
            projectID = results.projectID
            questionpreID = results.question_pre_ID
            status = 1
            checklists = checklists_kb.query.filter(checklists_kb.question_pre_ID == questionpreID).group_by(checklists_kb.checklistID).order_by(checklists_kb.checklistID).all()
            for row in checklists:
                sprint_id = 0
                comment = ""
                checklists_query = checklists_results(row.checklistID, projectID, sprint_id, status, comment)
                db.session.add(checklists_query)
                db.session.commit()
        checklists_first = checklists_kb.query.filter(checklists_kb.include_first == "True").group_by(checklists_kb.checklistID).order_by(checklists_kb.checklistID).all()
        for row in checklists_first:
            sprint_id = 0
            comment = ""
            status = 1
            checklists_query_first = checklists_results(row.checklistID, question_project_id, sprint_id, status, comment)
            db.session.add(checklists_query_first)
            db.session.commit()


def update_pre_questions(project_id, user_id, data):
    clear_question_pre_rows = db.session.query(question_pre_results).filter(question_pre_results.projectID == project_id)
    clear_question_pre_rows.delete(synchronize_session=False)
    clear_checklists_results_rows = db.session.query(checklists_results).filter(checklists_results.sprintID == '0').filter(checklists_results.projectID == project_id)
    clear_checklists_results_rows.delete(synchronize_session=False)
    db.session.commit()
    project = projects.query.filter(projects.projectID == project_id).one()
    groupmember = groupmembers.query.filter(groupmembers.userID == user_id).one()
    if groupmember.ownerID == project.ownerID & groupmember.groupID == project.groupID:
        for result in data.get('questions'):
            question_pre_ID = result['question_pre_ID']
            question_result = result['result']
            questions = question_pre_results(project_id, question_pre_ID, question_result)
            db.session.add(questions)
            db.session.commit()
            questions_results = question_pre_results.query.filter(question_pre_results.result == "False").group_by(question_pre_results.question_pre_ID).all()
        for results in questions_results:
            projectID = results.projectID
            questionpreID = results.question_pre_ID
            status = 1
            checklists = checklists_kb.query.filter(checklists_kb.question_pre_ID == questionpreID).group_by(checklists_kb.checklistID).order_by(checklists_kb.checklistID).all()
            for row in checklists:
                sprint_id = 0
                comment = ""
                checklists_query = checklists_results(row.checklistID, projectID, sprint_id, status, comment)
                db.session.add(checklists_query)
                db.session.commit()
        checklists_first = checklists_kb.query.filter(checklists_kb.include_first == "True").group_by(checklists_kb.checklistID).order_by(checklists_kb.checklistID).all()
        for row in checklists_first:
            sprint_id = 0
            comment = ""
            checklists_query_first = checklists_results(row.checklistID, projectID, sprint_id, status, comment)
            db.session.add(checklists_query_first)
            db.session.commit()


def store_sprint_questions(user_id, data):
    for result in data.get('questions'):
        question_sprint_ID = result['question_sprint_ID']
        question_result = result['result']
        question_project_id = result['projectID']
        question_sprint_id = result['sprintID']
        questions = question_sprint_results(question_project_id, question_sprint_id, question_sprint_ID, question_result)
        db.session.add(questions)
        db.session.commit()
        questions_results = question_sprint_results.query.filter(question_sprint_results.result == "True").group_by(question_sprint_results.question_sprint_ID).all()
    for results in questions_results:
        projectID = results.projectID
        questionsprintID = results.question_sprint_ID
        status = 1
        checklists = checklists_kb.query.filter(checklists_kb.question_sprint_ID == questionsprintID).group_by(checklists_kb.checklistID).order_by(checklists_kb.checklistID).all()
        for row in checklists:
            comment = ""
            checklists_query = checklists_results(row.checklistID, projectID, question_sprint_id, status, comment)
            db.session.add(checklists_query)
            db.session.commit()
    checklists_always = checklists_kb.query.filter(checklists_kb.include_always == "True").group_by(checklists_kb.checklistID).order_by(checklists_kb.checklistID).all()
    for row in checklists_always:
        comment = ""
        checklists_query_always = checklists_results(row.checklistID, projectID, question_sprint_id, status, comment)
        db.session.add(checklists_query_always)
        db.session.commit()
