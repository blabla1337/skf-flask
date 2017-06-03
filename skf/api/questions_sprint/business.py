import datetime

from skf.database import db
from skf.database.checklists_kb import checklists_kb
from skf.database.project_sprints import project_sprints
from skf.database.questions_sprint import questions_sprint
from skf.database.checklists_results import checklists_results
from skf.database.question_sprint_results import question_sprint_results
from skf.api.security import log, val_num, val_alpha, val_alpha_num


def get_sprint_items():
    log("User requested list of question sprint items", "LOW", "PASS")
    result = questions_sprint.query.paginate()
    return result


def store_sprint_questions(user_id, data):
    log("User stored new sprint question list", "MEDIUM", "PASS")
    val_num(user_id)
    for result in data.get('questions'):
        val_num(result['question_sprint_ID'])
        val_alpha(result['result'])
        val_num(result['projectID'])
        val_num(result['sprintID'])
        question_sprint_ID = result['question_sprint_ID']
        question_result = result['result']
        question_project_id = result['projectID']
        sprint_id = result['sprintID']
        questions = question_sprint_results(question_project_id, sprint_id, question_sprint_ID, question_result)
        db.session.add(questions)
        db.session.commit()
        status = 1
        pre_item = "False"
        comment = ""
        questions_results = question_sprint_results.query.filter(question_sprint_results.result == "True").group_by(question_sprint_results.question_sprint_ID).all()
    for results in questions_results:
        projectID = results.projectID
        questionsprintID = results.question_sprint_ID
        checklists = checklists_kb.query.filter(checklists_kb.question_sprint_ID == questionsprintID).group_by(checklists_kb.checklistID).order_by(checklists_kb.checklistID).all()
        for row in checklists:
            checklists_query = checklists_results(row.checklistID, projectID, sprint_id, status, comment, pre_item)
            db.session.add(checklists_query)
            db.session.commit()
    checklists_always = checklists_kb.query.filter(checklists_kb.include_always == "True").group_by(checklists_kb.checklistID).order_by(checklists_kb.checklistID).all()
    for row in checklists_always:
        checklists_query_always = checklists_results(row.checklistID, projectID, sprint_id, status, comment, pre_item)
        db.session.add(checklists_query_always)
        db.session.commit()
    return {'message': 'Sprint questions successfully created'}