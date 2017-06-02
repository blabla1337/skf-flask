from skf.database import db
from skf.database.code_items import code_items
from skf.api.security import log, val_num, val_alpha, val_alpha_num

def update_code_item(code_id, data):
    log("User requested updated specific code example item", "LOW", "PASS")
    result = code_items.query.filter(code_items.codeID == code_id).one()
    result.title = data.get('title')
    result.content = data.get('content')
    result.code_lang = data.get('code_lang')
    val_alpha_num(result.content)
    val_alpha_num(result.title)
    val_alpha(result.code_lang)
    db.session.add(result)
    db.session.commit()
    return {'message': 'Code example item successfully updated'}


def get_code_items():
    log("User requested list of code items", "LOW", "PASS")
    result = code_items.query.paginate()
    return result


def get_code_item(code_id):
    log("User requested code item", "LOW", "PASS")
    val_num(code_id)
    result = code_items.query.filter(code_items.codeID == code_id).one()
    return result


def get_code_items_lang(code_lang):
    log("User requested code lang items", "LOW", "PASS")
    val_alpha(code_lang)
    result = code_items.query.filter(code_items.code_lang == code_lang).paginate()
    return result