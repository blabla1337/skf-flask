from skf.database import db
from skf.api.security import log, val_num, val_float, val_alpha_num, val_alpha_num_special
from skf.database.checklists_kb import ChecklistKB
from skf.database.checklists_results import ChecklistResult
from skf.database.checklist_types import ChecklistType
from skf.database.question_results import QuestionResult
from skf.database.questions import Question
from sqlalchemy import desc, asc
import sys

def get_checklist_item(checklist_id, checklist_type):
    log("User requested specific checklist item", "LOW", "PASS")
    result = ChecklistKB.query.filter((ChecklistKB.checklist_type == checklist_type) & (ChecklistKB.checklist_id == checklist_id)).one()
    return result


def get_checklist_item_questions_git(checklist_type):
    log("User requested specific checklist items and correlated questions", "LOW", "PASS")
    result = ChecklistKB.query.filter(ChecklistKB.checklist_type == checklist_type).paginate(1, 2500, False)
    return result


def get_checklist_item_question_sprint(question_id):
    log("User requested specific checklist item using sprint questionID", "LOW", "PASS")
    result = ChecklistKB.query.filter(ChecklistKB.question_id == question_id).paginate(1, 2500, False)
    return result


def get_checklist_item_types(category_id):
    log("User requested list checklist types", "LOW", "PASS")
    result = ChecklistType.query.filter(ChecklistType.checklist_category_id == category_id).order_by(desc(ChecklistType.visibility)).paginate(1, 2500, False)
    return result

def get_checklist_type_by_id(checklist_type_id):
    log("User requested single checklist type content", "LOW", "PASS")
    result = ChecklistType.query.filter(ChecklistType.id ==  checklist_type_id).one()
    return result


def get_checklist_item_types_with_filter(maturity):
    log("User requested list checklist types", "LOW", "PASS")
    result = ChecklistType.query.filter(ChecklistType.maturity == maturity).filter(ChecklistType.visibility == 1).paginate(1, 2500, False)
    return result

def get_checklist_item_types_with_filter(maturity):
    log("User requested list checklist types", "LOW", "PASS")
    result = ChecklistType.query.filter(ChecklistType.maturity == maturity).filter(ChecklistType.visibility == 1).paginate(1, 2500, False)
    return result

def get_checklist_item_types_with_filter(maturity):
    log("User requested list checklist types", "LOW", "PASS")
    result = ChecklistType.query.filter(ChecklistType.maturity == maturity).filter(ChecklistType.visibility == 1).paginate(1, 2500, False)
    return result

def get_checklist_items(checklist_type):
    log("User requested list of checklist items", "LOW", "PASS")
    result = ChecklistKB.query.filter(ChecklistKB.checklist_type == checklist_type).order_by(ChecklistKB.checklist_id.asc()).paginate(1, 2500, False)
    return result
    

def get_checklist_items(checklist_type):
    log("User requested list of checklist items", "LOW", "PASS")
    result = ChecklistKB.query.filter(ChecklistKB.checklist_type == checklist_type).order_by(ChecklistKB.checklist_id.asc()).paginate(1, 2500, False)
    return result
    

def create_checklist_type(data, category_id):
    log("User requested create a new checklist type", "LOW", "PASS")
    checklist_type = ChecklistType(data.get('name'), data.get('description'), data.get('visibility'))
    checklist_type.checklist_category_id = category_id
    try:
        db.session.add(checklist_type)
        db.session.commit()
    except:
        db.rollback()
        raise
    return {'message': 'Checklist type successfully created'} 


def create_checklist_item(checklist_id, checklist_type, data):
    log("User requested create a new checklist item", "LOW", "PASS")
    include_always = convert_boolean_type(data.get('include_always'))
    question_id = convert_question_id_to_none(data.get('question_id'))
    if validate_duplicate_checklist_item(checklist_id, checklist_type) == True:
        try:
            checklist_item = ChecklistKB(checklist_id, data.get('content'), checklist_type, include_always, data.get('add_resources'), data.get('maturity'))
            checklist_item.question_id = question_id
            checklist_item.kb_id = data.get('kb_id')
            db.session.add(checklist_item)
            db.session.commit()
        except:
            db.session.rollback()
            raise
        return {'message': 'Checklist item successfully created'} 
    else:
        return {'message': 'Checklist item was duplicate!'} 


def convert_boolean_type(refine):
    if refine == "True":
        refine = True
    else:
        refine = False
    return refine


def convert_question_id_to_none(question_id):
    if question_id == 0:
        question_id = None
    return question_id


def update_checklist_type(id, data):
    log("User requested update checklist type", "LOW", "PASS")
    checklist_type = ChecklistType.query.get(id)
    checklist_type.name = data.get('name')
    checklist_type.description = data.get('description')
    checklist_type.visibility = data.get('visibility')
    try:
        db.session.add(checklist_type)
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        raise
    return {'message': 'Checklist item successfully updated'} 


def update_checklist_item(checklist_id, checklist_type, data):
    log("User requested update a specific checklist item", "LOW", "PASS")
    include_always = convert_boolean_type(data.get('include_always'))
    question_id = data.get('question_id')
    if question_id == 0:
        question_id = None
    result_checklist_kb = ChecklistKB.query.filter((ChecklistKB.checklist_id == checklist_id) & (ChecklistKB.checklist_type == checklist_type)).one()
    result_checklist_kb.content = data.get('content')
    result_checklist_kb.include_always = include_always
    result_checklist_kb.question_id = question_id
    result_checklist_kb.add_resources = data.get('add_resources')
    result_checklist_kb.kb_id = data.get('kb_id')
    result_checklist_kb.checklist_id = checklist_id
    result_checklist_kb.maturity = data.get('maturity')
    result_checklist_kb.checklist_type = checklist_type
    try:
        db.session.add(result_checklist_kb)
        db.session.commit()
    except Exception as e:
        db.session.rollback
        raise
    return {'message': 'Checklist item successfully updated'} 


def update_checklist_question_correlation(checklist_id, checklist_type, data):
    log("User requested update a specific checklist question correlation", "LOW", "PASS")
    question_id = convert_question_id_to_none(data.get('question_id'))
    result_checklist_kb = ChecklistKB.query.filter((ChecklistKB.checklist_id == checklist_id) & (ChecklistKB.checklist_type == checklist_type)).one()
    result_checklist_kb.question_id = question_id
    try:
        db.session.add(result_checklist_kb)
        db.session.commit()
    except Exception as e:
        db.session.rollback
        raise
    return {'message': 'Checklist item successfully updated'} 


def delete_checklist_type(checklist_type_id):
    log("User deleted checklist type", "MEDIUM", "PASS")
    checklist_types = ChecklistType.query.get(checklist_type_id)
    try:
        db.session.delete(checklist_types)
        db.session.commit()
    except:
        db.session.rollback()
        raise
    return {'message': 'Checklist type successfully deleted'}


def delete_checklist_item(checklist_id, checklist_type):
    log("User deleted checklist item", "MEDIUM", "PASS")    
    try:
        checklist = ChecklistKB.query.filter((ChecklistKB.checklist_id == checklist_id) & (ChecklistKB.checklist_type == checklist_type)).one()
        db.session.delete(checklist)
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        raise
    return {'message': 'Checklist item successfully deleted'}


def validate_duplicate_checklist_item(checklist_id, checklist_type):
        checklists = ChecklistKB.query.filter(ChecklistKB.checklist_id == checklist_id).filter(ChecklistKB.checklist_type == checklist_type).all()
        check = True
        for item in checklists:            
            if item.checklist_id == checklist_id:
                check = False
        return check
