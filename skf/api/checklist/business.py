from skf.database import db
from skf.api.security import log, val_num, val_float, val_alpha_num
from skf.database.checklists_kb import ChecklistKB
from skf.database.checklists_results import ChecklistResult
from skf.database.checklist_types import ChecklistType
import sys

def get_checklist_item(checklist_id, checklist_type):
    log("User requested specific checklist item", "LOW", "PASS")
    val_float(checklist_id)
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
    result = ChecklistKB.query.paginate(1, 500, False)
    return result


def create_checklist_type(data):
    log("User requested create a new checklist type", "LOW", "PASS")
    checklist_name = data.get('checklist_name')
    checklist_description = data.get('checklist_description')
    checklist_type = ChecklistType(checklist_name, checklist_description)

    try:
        db.session.add(checklist_type)
        db.session.commit()
    except:
        db.rollback()
        raise
    return {'message': 'Checklist type successfully created'} 


def update_checklist_type(id, data):
    log("User requested update checklist type", "LOW", "PASS")
    checklist_name = data.get('checklist_name')
    checklist_description = data.get('checklist_description')

    checklist_type = ChecklistType.query.get(id)
    checklist_type.checklist_name = checklist_name
    checklist_type.checklist_description = checklist_description

    try:
        db.session.commit()
    except:
        db.session.rollback()
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


def create_checklist_item(checklistID, checklist_type, data):
    log("User requested create a new checklist item", "LOW", "PASS")
    checklist_content = data.get('content')
    include_always = data.get('include_always')
    questionID = data.get('question_ID')
    checklistkbID = data.get('kbID')
    cwe = data.get('cwe')
    val_num(checklistID)
    val_num(checklist_kbID)
    val_num(checklist_type)

    checklist = Checklist.query.get(checklistID)

    if validate_duplicate_checklist_item(checklistID, checklist_type) == True:

        try:
            checklist_item = ChecklistKB(checklist_content, checklist_type, include_always, cwe)
            checklist_item.question_id = questionID
            checklist_item.kb_id = checklistkbID
            checklist.checklist_items.append(checklist_item)

            db.session.add(checklist_item)
            db.session.commit()

        except:
            db.session.rollback()
            raise

        return {'message': 'Checklist item successfully created'} 
    else:
        return {'message': 'Checklist item was duplicate!'} 


def update_checklist_item(checklist_id, checklist_type, data):
    log("User requested update a specific checklist item", "LOW", "PASS")
    val_num(checklist_type)

    if data.get('kbID') == "":
        kbID = 0
    else:
        kbID = data.get('kbID')
    val_num(kbID)

    result_checklist_kb = ChecklistKB.query.filter((ChecklistKB.id == checklist_id) & (ChecklistKB.checklist_type == checklist_type)).one()
    result_checklist_kb.title = data.get('title')
    result_checklist_kb.content = data.get('content')
    result_checklist_kb.include_always = data.get('include_always')
    result_checklist_kb.question_ID = data.get('question_ID')
    result_checklist_kb.cwe = data.get('cwe')
    result_checklist_kb.kbID = kbID
    result_checklist_kb.checklistID = checklist_id
    result_checklist_kb.checklist_type = checklist_type
    val_num(result_checklist_kb.question_ID)

    try:
        db.session.add(result_checklist_kb)
        db.session.commit()
    except:
        db.session.rollback
        raise
    return {'message': 'Checklist item successfully updated'} 


def delete_checklist_item(checklist_id, checklist_type):
    log("User deleted checklist item", "MEDIUM", "PASS")

    try:
        checklist = ChecklistKB.query.filter((ChecklistKB.id == checklist_id) & (ChecklistKB.checklist_type == checklist_type)).one()
        db.session.delete(checklist)
        db.session.commit()

    except:
        db.session.rollback()
        raise

    return {'message': 'Checklist item successfully deleted'}


def get_checklist_items(checklist_type):
    log("User requested list of checklist items", "LOW", "PASS")
    val_num(checklist_type)
    result = ChecklistKB.query.filter(ChecklistKB.id == checklist_type).paginate(1, 1500, False)
    ordered = order_checklist_items(result)
    return ordered
    

def order_checklist_items(checklist_items):
    ordered_checklist_items = []
    for item in checklist_items.items:
        numbers = item.checklistID.split('.')
        category = int(numbers[0])
        category_requirement = int(numbers[1])
        if (len(ordered_checklist_items) == 0):
            ordered_checklist_items.append(item)
        else:
            y = 0
            while y < len(ordered_checklist_items):
                numbers_ordered = ordered_checklist_items[y].checklistID.split('.')
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


def validate_duplicate_checklist_item(checklistID, checklist_type):
        checklists = ChecklistKB.query.filter(ChecklistKB.id == checklistID).filter(ChecklistKB.checklist_type == checklist_type).all()
        check = True
        for item in checklists:            
            if item.checklistID == checklistID:
                check = False
        return check

    