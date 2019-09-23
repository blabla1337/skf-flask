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
    val_alpha_num_special(checklist_id)
    val_num(checklist_type)
    result = ChecklistKB.query.filter((ChecklistKB.checklist_type == checklist_type) & (ChecklistKB.checklist_id == checklist_id)).one()
    return result

def get_checklist_item_questions_git(checklist_type):
    log("User requested specific checklist items and correlated questions", "LOW", "PASS")
    val_num(checklist_type)
    result = ChecklistKB.query.filter(ChecklistKB.checklist_type == checklist_type).paginate(1, 1500, False)
    return result


def get_checklist_item_question_pre(question_id):
    log("User requested specific checklist item using pre questionID", "LOW", "PASS")
    val_num(question_id)
    result = ChecklistKB.query.filter(ChecklistKB.question_id == question_id).paginate(1, 1500, False)
    return result


def get_checklist_item_question_sprint(question_id):
    log("User requested specific checklist item using sprint questionID", "LOW", "PASS")
    val_num(question_id)
    result = ChecklistKB.query.filter(ChecklistKB.question_id == question_id).paginate(1, 1500, False)
    return result


def get_checklist_item_types():
    log("User requested list checklist types", "LOW", "PASS")
    result = ChecklistType.query.order_by(desc(ChecklistType.visibility)).paginate(1, 500, False)
    return result

def get_checklist_item_types_with_filter(maturity):
    log("User requested list checklist types", "LOW", "PASS")
    result = ChecklistType.query.filter(ChecklistType.maturity == maturity).filter(ChecklistType.visibility == 1).paginate(1, 500, False)
    return result

def get_checklist_items(checklist_type):
    log("User requested list of checklist items", "LOW", "PASS")
    val_num(checklist_type)
    result = ChecklistKB.query.filter(ChecklistKB.checklist_type == checklist_type).paginate(1, 1500, False)
    ordered = order_checklist_items(result)
    return ordered
    

def create_checklist_type(data):
    log("User requested create a new checklist type", "LOW", "PASS")
    val_alpha_num_special(data.get('name'))
    val_alpha_num_special(data.get('description'))
    
    checklist_name = data.get('name')
    checklist_description = data.get('description')
    visibility = data.get('visibility')
    checklist_type = ChecklistType(checklist_name, checklist_description, visibility)

    try:
        db.session.add(checklist_type)
        db.session.commit()
    except:
        db.rollback()
        raise
    return {'message': 'Checklist type successfully created'} 

def create_checklist_item(checklist_id, checklist_type, data):
    log("User requested create a new checklist item", "LOW", "PASS")
    
    val_alpha_num_special(data.get('content'))
    val_alpha_num(data.get('include_always'))
    val_num(data.get('question_id'))
    val_num(data.get('kb_id'))
    val_num(data.get('maturity'))

    content = data.get('content')
    include_always = data.get('include_always')
    question_id = data.get('question_id')
    kb_id = data.get('kb_id')
    cwe = data.get('cwe')
    maturity = data.get('maturity')

    if include_always == "True":
        include_always = True
    else:
        include_always = False

    if question_id == 0:
        question_id = None

    if validate_duplicate_checklist_item(checklist_id, checklist_type) == True:
        try:
            checklist_item = ChecklistKB(checklist_id, content, checklist_type, include_always, cwe, maturity)
            checklist_item.question_id = question_id
            checklist_item.kb_id = kb_id
            db.session.add(checklist_item)

            db.session.commit()
        except:
            db.session.rollback()
            raise

        return {'message': 'Checklist item successfully created'} 
    else:
        return {'message': 'Checklist item was duplicate!'} 


def update_checklist_type(id, data):
    log("User requested update checklist type", "LOW", "PASS")
    
    val_num(id)
    val_alpha_num_special(data.get('name'))
    val_alpha_num_special(data.get('description'))
    
    checklist_name = data.get('name')
    checklist_description = data.get('description')
    visibility = data.get('visibility')

    checklist_type = ChecklistType.query.get(id)
    checklist_type.name = checklist_name
    checklist_type.description = checklist_description
    checklist_type.visibility = visibility

    try:
        db.session.add(checklist_type)
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        raise
    
    return {'message': 'Checklist item successfully updated'} 


def update_checklist_item(checklist_id, checklist_type, data):
    log("User requested update a specific checklist item", "LOW", "PASS")
    
    val_num(checklist_type)
    val_alpha_num_special(checklist_id)
    val_num(data.get('maturity'))
    val_num(data.get('question_id'))
    val_num(data.get('cwe'))
    val_num(data.get('kb_id'))
    val_alpha_num(data.get('include_always'))
    val_alpha_num_special(data.get('content'))
    
    include_always = data.get('include_always')
    question_id = data.get('question_id')
    maturity = data.get('maturity')
    content = data.get('content')
    cwe = data.get('cwe')
    kb_id = data.get('kb_id')
    if include_always == "True":
        include_always = True
    else:
        include_always = False
    if question_id == 0:
        question_id = None
    result_checklist_kb = ChecklistKB.query.filter((ChecklistKB.checklist_id == checklist_id) & (ChecklistKB.checklist_type == checklist_type)).one()
    result_checklist_kb.content = content
    result_checklist_kb.include_always = include_always
    result_checklist_kb.question_id = question_id
    result_checklist_kb.cwe = cwe
    result_checklist_kb.kb_id = kb_id
    result_checklist_kb.checklist_id = checklist_id
    result_checklist_kb.maturity = maturity
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

    val_num(checklist_type)
    val_alpha_num_special(checklist_id)
    val_num(data.get('question_id'))

    question_id = data.get('question_id')
    if question_id == 0:
        question_id = None
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
    val_num(checklist_type_id)

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
    val_num(checklist_type)
    val_alpha_num_special(checklist_id)
    
    try:
        checklist = ChecklistKB.query.filter((ChecklistKB.checklist_id == checklist_id) & (ChecklistKB.checklist_type == checklist_type)).one()
        db.session.delete(checklist)
        db.session.commit()

    except Exception as e:
        db.session.rollback()
        raise

    return {'message': 'Checklist item successfully deleted'}

def order_checklist_items(checklist_items):
    ordered_checklist_items = []
    for item in checklist_items.items:
        numbers = item.checklist_id.split('.')
        category = int(numbers[0])
        category_requirement = int(numbers[1])
        if (len(ordered_checklist_items) == 0):
            ordered_checklist_items.append(item)
        else:
            y = 0
            while y < len(ordered_checklist_items):
                numbers_ordered = ordered_checklist_items[y].checklist_id.split('.')
                category_ordered = int(numbers_ordered[0])
                category_requirement_ordered = int(numbers_ordered[1])
                if (category < category_ordered):
                    ordered_checklist_items.insert(y, item)
                    break
                else:
                    if (category == category_ordered):
                        if (category_requirement < category_requirement_ordered):
                            ordered_checklist_items.insert(y, item)
                            break
                y = y + 1
            if (y == len(ordered_checklist_items)):
                ordered_checklist_items.insert(y, item)
            checklist_items.items = ordered_checklist_items
    return checklist_items


def validate_duplicate_checklist_item(checklist_id, checklist_type):
        checklists = ChecklistKB.query.filter(ChecklistKB.checklist_id == checklist_id).filter(ChecklistKB.checklist_type == checklist_type).all()
        check = True
        for item in checklists:            
            if item.checklist_id == checklist_id:
                check = False
        return check

    