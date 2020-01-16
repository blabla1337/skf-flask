from skf.database import db
from skf.database.code_items import CodeItem
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


def delete_code_item(code_id):
    log("User deleted code item", "MEDIUM", "PASS")
    code_item = (CodeItem.query.filter(CodeItem.id == code_id).one())
    try:
        db.session.delete(code_item)
        db.session.commit()
    except:
        db.session.rollback()
        raise
    return {'message': 'Code example item successfully deleted'}


def get_code_items(category_id):
    log("User requested list of code items", "LOW", "PASS")
    result = CodeItem.query.filter(CodeItem.checklist_category_id == category_id).paginate(1, 500, False)
    return result


def get_code_item(code_id):
    log("User requested code item", "LOW", "PASS")
    result = CodeItem.query.filter(CodeItem.id == code_id).one()
    return result