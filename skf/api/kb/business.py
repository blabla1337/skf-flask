from skf.database import db
from skf.database.kb_items import kb_items
from skf.api.security import log, val_num, val_alpha_num


def update_kb_item(kb_id, data):
    log("User requested update a specific kb item", "LOW", "PASS")
    val_num(kb_id)
    result = kb_items.query.filter(kb_items.kbID == kb_id).one()
    result.title = data.get('title')
    result.content = data.get('content')
    val_alpha_num(result.title)
    val_alpha_num(result.content)
    db.session.add(result)
    db.session.commit()
    if not result:
        log("User triggered error updating specific kb item", "LOW", "FAIL")
        return {'message': 'KB item not updated'}
    else:
        return {'message': 'KB item successfully updated'}


def get_kb_item(kb_id):
    log("User requested specific kb item", "LOW", "PASS")
    val_num(kb_id)
    result = kb_items.query.filter(kb_items.kbID == kb_id).one()
    if not result:
        log("User triggered error requesting specific kb item", "LOW", "FAIL")
        return False
    else:
        return result


def get_kb_items():
    log("User requested list of kb items", "LOW", "PASS")
    result = kb_items.query.paginate()
    if not result:
        log("User triggered error requesting list of kb items", "LOW", "FAIL")
        return False
    else:
        return result