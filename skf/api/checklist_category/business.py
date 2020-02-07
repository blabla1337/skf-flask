from skf.database import db
from skf.api.security import log, val_num, val_float, val_alpha_num, val_alpha_num_special
from skf.database.checklist_category import ChecklistCategory
from skf.database.checklists_results import ChecklistResult
from skf.database.question_results import QuestionResult
from skf.database.questions import Question
from sqlalchemy import desc, asc
import sys

def get_checklist_category_item(checklist_category_id):
    log("User requested specific checklist category item", "LOW", "PASS")
    result = ChecklistCategory.query.filter((ChecklistCategory.id == checklist_category_id)).one()
    return result

def get_checklist_categories():
    log("User requested list checklist categories", "LOW", "PASS")
    result = ChecklistCategory.query.order_by(desc(ChecklistCategory.name)).paginate(1, 500, False)
    return result
    
def create_checklist_category(data):
    log("User requested create a new checklist category", "LOW", "PASS")
    checklist_category = ChecklistCategory(data.get('name'), data.get('description'))
    try:
        db.session.add(checklist_category)
        db.session.commit()
    except:
        db.rollback()
        raise
    return {'message': 'Checklist category successfully created'} 

def update_checklist_category(id, data):
    log("User requested update checklist category", "LOW", "PASS")
    checklist_category = ChecklistCategory.query.get(id)
    checklist_category.name = data.get('name')
    checklist_category.description = data.get('description')
    try:
        db.session.add(checklist_category)
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        raise
    return {'message': 'Checklist category successfully updated'} 

def delete_checklist_category(checklist_category_id):
    log("User deleted checklist item", "MEDIUM", "PASS")
    try:
        checklist = ChecklistCategory.query.filter(ChecklistCategory.id == checklist_category_id).one()
        db.session.delete(checklist)
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        raise
    return {'message': 'Checklist category successfully deleted'}