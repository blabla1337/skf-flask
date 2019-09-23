from skf.database import db
#from skf.database.projects import Project
from skf.database.checklists_kb import ChecklistKB
from skf.database.questions import Question
from skf.database.checklists_results import ChecklistResult
from skf.database.question_results import QuestionResult
from skf.api.security import log, val_num, val_alpha, val_alpha_num, val_alpha_num_special

def get_questions(checklists_type):
    log("User requested list of questions", "LOW", "PASS")
    val_num(checklists_type)
    result = Question.query.filter(Question.checklist_type == checklists_type).paginate(1, 500, False)
    return result

def store_questions(checklist_type, maturity, data):
    log("User stored new sprint question list", "MEDIUM", "PASS")
    #Store the result of the questionaire if answer was true in checklists_kb
    for result in data.get('questions'):

         val_num(result['question_id'])
         val_num(result['project_id'])
         val_num(result['checklist_type'])
         val_num(result['sprint_id'])
         val_alpha_num(result['result'])

         question_id = result['question_id']
         question_result = result['result']
         question_project_id = result['project_id']
         checklist_type = result['checklist_type']
         sprint_id = result['sprint_id']
         status = 1
         if question_result == "True":
             checklists = ChecklistKB.query.filter(ChecklistKB.question_id == question_id).filter(ChecklistKB.checklist_type == checklist_type).filter(ChecklistKB.maturity == maturity).all()
             for row in checklists:
                 checklists_query = ChecklistResult(status)
                 checklists_query.project_id = question_project_id
                 checklists_query.sprint_id = sprint_id
                 checklists_query.kb_id = row.kb_id
                 checklists_query.checklist_id = row.id
                 checklists_query.checklist_type_id = checklist_type
                 db.session.add(checklists_query)
                 db.session.commit()
         #Also check for the include always marked items so they are taken in account
         checklists_always = ChecklistKB.query.filter(ChecklistKB.include_always == 1).filter(ChecklistKB.checklist_type == checklist_type).filter(ChecklistKB.maturity == maturity).all()
         for row in checklists_always:
            checklists_always = ChecklistResult(status)
            checklists_always.project_id = question_project_id
            checklists_always.sprint_id = sprint_id
            checklists_always.kb_id = row.kb_id
            checklists_always.checklist_id = row.id
            checklists_always.checklist_type_id = checklist_type
            db.session.add(checklists_always)
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
    val_num(data.get('checklist_type'))
    val_alpha_num_special(data.get('question'))
    
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