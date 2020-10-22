from skf.database import db
from skf.database.code_items import CodeItem
<<<<<<< HEAD
from skf.database.checklist_kb_code_item import ChecklistKBCodeItem
from skf.api.security import log, val_num, val_alpha, val_alpha_num, val_alpha_num_special

=======
from skf.api.security import log, val_num, val_alpha, val_alpha_num, val_alpha_num_special

def create_code_item(data, category_id):
    log("User requested creating a new code item", "LOW", "PASS")
    result = CodeItem(data.get('content'), data.get('title'), data.get('code_lang'))
    result.checklist_category_id = category_id
    try:
        db.session.add(result)
        db.session.commit()
    except:
        db.session.rollback()
        raise
    return {'message': 'Code example item successfully created'} 

>>>>>>> origin/master

def update_code_item(code_id, data):
    log("User requested updated specific code example item", "LOW", "PASS")
    result = CodeItem.query.filter(CodeItem.id == code_id).one()
    result.title = data.get('title')
    result.content = data.get('content')
    result.code_lang = data.get('code_lang')
    try:
        db.session.add(result)
        db.session.commit()
    except:
        db.session.rollback()
        raise
    return {'message': 'Code example item successfully updated'}


<<<<<<< HEAD
def create_code_item(data, category_id):
    log("User requested creating a new kb item", "LOW", "PASS")
    val_alpha_num_special(data.get('title'))
    val_alpha_num(data.get('code_lang'))
    val_num(category_id)
    title = data.get('title')
    content = data.get('content')
    code_lang = data.get('code_lang')
    result = CodeItem(content, title, code_lang)
    result.checklist_category_id = category_id
    try:
        db.session.add(result)
        db.session.commit()
    except:
        db.session.rollback()
        raise
    return {'message': 'Code example item successfully created'} 


def delete_code_item(code_id):
    log("User deleted code item", "MEDIUM", "PASS")
    val_num(code_id)
    codeItem = (CodeItem.query.filter(CodeItem.id == code_id).one())
    try:
        db.session.delete(codeItem)
=======
def delete_code_item(code_id):
    log("User deleted code item", "MEDIUM", "PASS")
    code_item = (CodeItem.query.filter(CodeItem.id == code_id).one())
    try:
        db.session.delete(code_item)
>>>>>>> origin/master
        db.session.commit()
    except:
        db.session.rollback()
        raise
    return {'message': 'Code example item successfully deleted'}


def get_code_items(category_id):
    log("User requested list of code items", "LOW", "PASS")
<<<<<<< HEAD
    result = CodeItem.query.filter(CodeItem.checklist_category_id == category_id).paginate(1, 2500, False)
=======
    result = CodeItem.query.filter(CodeItem.checklist_category_id == category_id).paginate(1, 1500, False)
>>>>>>> origin/master
    return result
    


def get_code_item(code_id):
    log("User requested code item", "LOW", "PASS")
<<<<<<< HEAD
    val_num(code_id)
    result = CodeItem.query.filter(CodeItem.id == code_id).one()
    return result

def get_code_items_checklist_kb(checklist_kb_id):
    log("User requested list of code items", "LOW", "PASS")
    result = ChecklistKBCodeItem.query.filter(ChecklistKBCodeItem.checklist_kb_id == checklist_kb_id).paginate(1, 2500, False)
    return result
    
    
def delete_code_item_checklist_kb(checklist_kb_id, code_items_id):
    log("User deleted code item", "MEDIUM", "PASS")
    val_num(code_items_id)
    val_num(checklist_kb_id)
    codeItem = (ChecklistKBCodeItem.query \
    .filter(ChecklistKBCodeItem.checklist_kb_id == checklist_kb_id) \
    .filter(ChecklistKBCodeItem.code_items_id == code_items_id) \
    .one())
    try:
        db.session.delete(codeItem)
        db.session.commit()
    except:
        db.session.rollback()
        raise
    return {'message': 'Code example item successfully deleted'} 


def create_code_item_checklist_kb(checklist_kb_id, code_items_id):
    log("User requested creating a new kb item", "LOW", "PASS")
    val_num(checklist_kb_id)
    val_num(code_items_id)
    result = ChecklistKBCodeItem(checklist_kb_id,code_items_id)
    try:
        db.session.add(result)
        db.session.commit()
    except:
        db.session.rollback()
        raise
    return {'message': 'Code example item successfully created'} 
=======
    result = CodeItem.query.filter(CodeItem.id == code_id).one()
    return result
>>>>>>> origin/master
