from skf.database import db
from skf.database.code_items import CodeItem
from skf.api.security import log, val_num, val_alpha, val_alpha_num

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

def create_code_item(data):
    log("User requested creating a new kb item", "LOW", "PASS")
    content = data.get('content')
    title = data.get('title')
    code_lang = data.get('code_lang')
    result = CodeItem(title, content, code_lang)

    try:
        db.session.add(result)
        db.session.commit()
    except:
        db.session.rollback()
        raise

    return {'message': 'KB item successfully created'} 

def delete_code_item(codeId, user_id):
    log("User deleted code item", "MEDIUM", "PASS")
    val_num(codeId)
    val_num(user_id)
    codeItem = (CodeItem.query.filter(CodeItem.ide == codeId).one())

    try:
        db.session.delete(codeItem)
        db.session.commit()
    except:
        db.session.rollback()
        raise
        
    return {'message': 'code item successfully deleted'}

def get_code_items():
    log("User requested list of code items", "LOW", "PASS")
    result = CodeItem.query.paginate(1, 500, False)
    return result


def get_code_item(code_id):
    log("User requested code item", "LOW", "PASS")
    val_num(code_id)
    result = CodeItem.query.filter(CodeItem.id == code_id).one()
    return result


def get_code_items_lang(code_lang):
    log("User requested code lang items", "LOW", "PASS")
    val_alpha(code_lang)
    result = CodeItem.query.filter(CodeItem.code_lang == code_lang).paginate(1, 500, False)
    return result