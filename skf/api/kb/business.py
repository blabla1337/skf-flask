from skf.database import db
from skf.database.kb_items import kb_items
from skf.api.security import log, val_num, val_alpha_num


def update_kb_item(kb_id, data):
    log("User requested update a specific kb item", "LOW", "PASS")
    val_num(kb_id)
    val_alpha_num(data.get('content'))
    val_alpha_num(data.get('title'))
    result = kb_items.query.filter(kb_items.kbID == kb_id).one()
    result.title = data.get('title')
    result.content = data.get('content')
    db.session.add(result)
    db.session.commit()
    return {'message': 'KB item successfully updated'} 


def create_kb_item(data):
    log("User requested creating a new kb item", "LOW", "PASS")
    content = data.get('content')
    title = data.get('title')
    val_alpha_num(content)
    val_alpha_num(title)
    result = kb_items(content, title)
    db.session.add(result)
    db.session.commit()
    return {'message': 'KB item successfully created'} 


def get_kb_item(kb_id):
    log("User requested specific kb item", "LOW", "PASS")
    val_num(kb_id)
    result = kb_items.query.filter(kb_items.kbID == kb_id).one()
    return result


def get_kb_items():
    log("User requested list of kb items", "LOW", "PASS")
    result = kb_items.query.paginate(1, 500, False)
    return result
