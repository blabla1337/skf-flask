from skf.database import db
#from skf.database.projects import Project
from skf.database.checklists_kb import ChecklistKB
from skf.database.questions import Question
from skf.database.checklists_results import ChecklistResult
from skf.database.question_results import QuestionResult
from skf.api.security import log, val_num, val_alpha, val_alpha_num
import sys

def get_questions(checklists_type):
    log("User requested list of questions", "LOW", "PASS")
    val_num(checklists_type)
    result = Question.query.filter(Question.checklist_type == checklists_type).paginate(1, 500, False)
    return result

def store_questions(checklist_type, data):
    log("User stored new sprint question list", "MEDIUM", "PASS")
    #Store the result of the questionaire if answer was true in checklists_kb
    for result in data.get('questions'):
         val_num(result['question_ID'])
         val_alpha(result['result'])
         val_num(result['projectID'])
         val_num(result['sprintID'])
         question_ID = result['question_ID']
         question_result = result['result']
         question_project_id = result['projectID']
         checklist_type = result['checklist_type']
         sprint_id = result['sprintID']
         status = 1
         if question_result == "True":
             checklists = ChecklistKB.query.filter(ChecklistKB.question_id == question_ID).filter(ChecklistKB.checklist_type == checklist_type).all()
             for row in checklists:
                 checklists_query = ChecklistResult(row.id, question_project_id, sprint_id, status, row.kbID)
                 db.session.add(checklists_query)
                 db.session.commit()
    #Also check for the include always marked items so they are taken in account
    checklists_always = ChecklistKB.query.filter(ChecklistKB.include_always == "True").filter(ChecklistKB.checklist_type == checklist_type).all()
    for row in checklists_always:
             checklists_query_always = ChecklistResult(row.id, question_project_id, sprint_id, status, row.kbID)
             db.session.add(checklists_query_always)
             db.session.commit()
    return {'message': 'Sprint successfully created'}

def new_question(data):
    log("User created new sprint question item", "MEDIUM", "PASS")
    val_alpha_num(data.get('question'))
    sprint_question = data.get('question')
    sprint_checklist_type = data.get('checklist_type')
    sprint = Question(sprint_question, sprint_checklist_type)
    db.session.add(sprint)
    db.session.commit()
    return {'message': 'New Question successfully created'}

def update_question(id_question, data):
    log("User updated sprint question item", "MEDIUM", "PASS")
    val_num(id_question)
    val_alpha_num(data.get('question'))
    sprint_question = data.get('question')
    sprint_checklist_type = data.get('checklist_type')
    sprint = Question.query.filter(Question.id == id_question).one()
    sprint.question = sprint_question
    sprint.checklist_type = sprint_checklist_type
    db.session.add(sprint)
    db.session.commit()
    return {'message': 'Question successfully updated'}

def delete_question(id_question):
    log("User deleted question", "MEDIUM", "PASS")
    val_num(id_question)
    sprint = Question.query.filter(Question.id == id_question).one()
    db.session.delete(sprint)
    db.session.commit()
    return {'message': 'Question successfully deleted'}