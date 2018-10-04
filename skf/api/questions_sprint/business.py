from skf.database import db
from skf.database.projects import projects
from skf.database.checklists_kb import checklists_kb
from skf.database.questions_sprint import questions_sprint
from skf.database.checklists_results import checklists_results
from skf.database.question_sprint_results import question_sprint_results
from skf.api.security import log, val_num, val_alpha, val_alpha_num


def get_sprint_items(checklists_type):
    log("User requested list of question sprint items", "LOW", "PASS")
    val_num(checklists_type)
    result = questions_sprint.query.filter(questions_sprint.checklist_type == checklists_type).paginate(1, 500, False)
    return result


def delete_sprint_question(id_sprint_question):
    log("User deleted sprint item question", "MEDIUM", "PASS")
    val_num(id_sprint_question)
    sprint = questions_sprint.query.filter(questions_sprint.id == id_sprint_question).one()
    db.session.delete(sprint)
    db.session.commit()
    return {'message': 'Sprint item question successfully deleted'}


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
        projects_result = projects.query.filter(projects.projectID == question_project_id).one()
        checklist_type = projects_result.checklist_type
        status = 1
        pre_item = "False"
        questions_results = question_sprint_results.query.filter(question_sprint_results.sprintID == sprint_id).filter(question_sprint_results.projectID == question_project_id).filter(question_sprint_results.result == "True").all()
        for results in questions_results:
            projectID = results.projectID
            questionsprintID = results.question_sprint_ID
            checklists = checklists_kb.query.filter(checklists_kb.question_pre_ID == 0).filter(checklists_kb.question_sprint_ID == questionsprintID).filter(checklists_kb.checklist_type == checklist_type).group_by(checklists_kb.checklistID).group_by(checklists_kb.checklistID).order_by(checklists_kb.checklistID).all()
            for row in checklists:
                checkID = row.checklistID
                checklists_query = checklists_results(checkID, projectID, sprint_id, status, pre_item, row.kbID)
                db.session.add(checklists_query)
                db.session.commit()
        checklists_always = checklists_kb.query.filter(checklists_kb.include_always == "True").filter(checklists_kb.checklist_type == checklist_type).group_by(checklists_kb.checklistID).group_by(checklists_kb.checklistID).order_by(checklists_kb.checklistID).all()
        for row in checklists_always:
            checklists_query_always = checklists_results(row.checklistID, question_project_id, sprint_id, status, pre_item, row.kbID)
            db.session.add(checklists_query_always)
            db.session.commit()
    return {'message': 'Sprint questions successfully created'}


def update_sprint_question(id_sprint_question, data):
    log("User updated sprint question item", "MEDIUM", "PASS")
    val_num(id_sprint_question)
    val_alpha_num(data.get('question'))
    sprint_question = data.get('question')
    sprint_checklist_type = data.get('checklist_type')
    sprint = questions_sprint.query.filter(questions_sprint.id == id_sprint_question).one()
    sprint.question = sprint_question
    sprint.checklist_type = sprint_checklist_type
    db.session.add(sprint)
    db.session.commit()
    return {'message': 'Sprint question successfully updated'}


def new_sprint_question(data):
    log("User created new sprint question item", "MEDIUM", "PASS")
    val_alpha_num(data.get('question'))
    sprint_question = data.get('question')
    sprint_checklist_type = data.get('checklist_type')
    sprint = questions_sprint(sprint_question, sprint_checklist_type)
    db.session.add(sprint)
    db.session.commit()
    return {'message': 'New sprint question successfully created'}