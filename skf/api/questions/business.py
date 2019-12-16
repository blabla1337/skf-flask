from sqlalchemy import or_
from skf.database import db
from flask import abort
from skf.database.checklists_kb import ChecklistKB
from skf.database.questions import Question
from skf.database.checklists_results import ChecklistResult
from skf.database.question_results import QuestionResult
from skf.api.security import log, val_num, val_alpha, val_alpha_num, val_alpha_num_special
import sys

def get_questions(checklists_type):
    log("User requested list of questions", "LOW", "PASS")
    val_num(checklists_type)
    result = Question.query.filter(Question.checklist_type == checklists_type).paginate(1, 500, False)
    return result

def store_questions(checklist_type, maturity, data):
    log("User stored new sprint question list", "MEDIUM", "PASS")
    #Store the result of the questionaire if answer was true in checklists_kb
    for result in data.get('questions'):
        project_id = result['project_id']
        sprint_id = result['sprint_id']
        question_id = result['question_id']
        if result['result'] == "True":
            checklists = select_checklist_items_by_maturity(maturity, question_id, checklist_type)
            store_question_results(checklists, project_id, sprint_id, checklist_type)
    #Also check for the include always marked items so they are taken in account
    checklists_always = select_checklist_items_by_maturity_include_always(maturity, checklist_type)
    store_question_results_include_always(checklists_always, project_id, sprint_id, checklist_type)
    return {'message': 'Sprint successfully created'}


def select_checklist_items_by_maturity(maturity, question_id, checklist_type):
    switcher = {
        1: ChecklistKB.query.filter(ChecklistKB.question_id == question_id).filter(ChecklistKB.checklist_type == checklist_type).filter(ChecklistKB.maturity == 1).filter(ChecklistKB.include_always == 0).all(),
        2: ChecklistKB.query.filter(ChecklistKB.question_id == question_id).filter(ChecklistKB.checklist_type == checklist_type).filter(or_(ChecklistKB.maturity == 1, ChecklistKB.maturity == 2)).filter(ChecklistKB.include_always == 0).all(),
        3: ChecklistKB.query.filter(ChecklistKB.question_id == question_id).filter(ChecklistKB.checklist_type == checklist_type).filter(or_(ChecklistKB.maturity == 1, ChecklistKB.maturity == 2, ChecklistKB.maturity == 3)).filter(ChecklistKB.include_always == 0).all(),
    }
    func = switcher.get(maturity, lambda: "Invalid search")
    return func


def select_checklist_items_by_maturity_include_always(maturity, checklist_type):
    switcher = {
        1: ChecklistKB.query.filter(ChecklistKB.include_always == 1).filter(ChecklistKB.checklist_type == checklist_type).filter(ChecklistKB.maturity == 1).all(),
        2: ChecklistKB.query.filter(ChecklistKB.include_always == 1).filter(ChecklistKB.checklist_type == checklist_type).filter(or_(ChecklistKB.maturity == 1, ChecklistKB.maturity == 2)).all(),
        3: ChecklistKB.query.filter(ChecklistKB.include_always == 1).filter(ChecklistKB.checklist_type == checklist_type).filter(or_(ChecklistKB.maturity == 1, ChecklistKB.maturity == 2, ChecklistKB.maturity == 3)).all(),
    }
    func = switcher.get(maturity, lambda: "Invalid search")
    return func


def store_question_results(checklists, project_id, sprint_id, checklist_type):
    try:
        for row in checklists:
            checklist = ChecklistResult(1, 0, 0)
            checklist.project_id = project_id
            checklist.sprint_id = sprint_id
            checklist.kb_id = row.kb_id
            checklist.checklist_id = row.id
            checklist.checklist_type_id = checklist_type
            db.session.add(checklist)
            db.session.commit()
    except:
        abort(400, "error storing checklist results")


def store_question_results_include_always(checklists, project_id, sprint_id, checklist_type):
    try:
        for row in checklists:
                    checklists = ChecklistResult(1, 0, 0)
                    checklists.project_id = project_id
                    checklists.sprint_id = sprint_id
                    checklists.kb_id = row.kb_id
                    checklists.checklist_id = row.id
                    checklists.checklist_type_id = checklist_type
                    db.session.add(checklists)
                    db.session.commit()
    except:
        abort(400, "error storing checklist results - include always")

def new_question(data):
    log("User created new sprint question item", "MEDIUM", "PASS")
    sprint = Question(data.get('question'), data.get('checklist_type'))
    db.session.add(sprint)
    db.session.commit()
    return {'message': 'New Question successfully created'}

def update_question(id_question, data):
    log("User updated sprint question item", "MEDIUM", "PASS")
    sprint = Question.query.filter(Question.id == id_question).one()
    sprint.question = data.get('question')
    sprint.checklist_type = data.get('checklist_type')
    db.session.add(sprint)
    db.session.commit()
    return {'message': 'Question successfully updated'}

def delete_question(id_question):
    log("User deleted question", "MEDIUM", "PASS")
    sprint = Question.query.filter(Question.id == id_question).one()
    db.session.delete(sprint)
    db.session.commit()
    return {'message': 'Question successfully deleted'}