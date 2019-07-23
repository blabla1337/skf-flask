from skf.database import db
from skf.database.kb_items import KBItem
from skf.api.security import log, val_num, val_alpha_num


def update_kb_item(kb_id, data):
    log("User requested update a specific kb item", "LOW", "PASS")
    val_num(kb_id)
    val_alpha_num(data.get('title'))

    try:
        kb_item = KBItem.query.get(kb_id)
        kb_item.title = data.get('title')
        kb_item.content = data.get('content')

        db.session.add(kb_item)
        db.session.commit()

    except:
        db.session.rollback()
        raise

    return {'message': 'KB item successfully updated'} 


def create_kb_item(data):
    log("User requested creating a new kb item", "LOW", "PASS")
    content = data.get('content')
    title = data.get('title')

    try:
        kb_item = KBItem(title,content)

        db.session.add(result)
        db.session.commit()

    except:
        db.session.rollback()
        raise

    return {'message': 'KB item successfully created'} 

def delete_kb_item(kbID, user_id):
    log("User deleted kb item", "MEDIUM", "PASS")
    val_num(kbID)
    val_num(user_id)

    try:
        kb_item = KBItem.query.get(kbID)

        db.session.delete(kbItem)
        db.session.commit()

    except:
        db.session.rollback()
        raise

    return {'message': 'KB item successfully deleted'}

def get_kb_item(kb_id):
    log("User requested specific kb item", "LOW", "PASS")
    val_num(kb_id)

    return KBItem.query.get(kb_id)


def get_kb_items():
    log("User requested list of kb items", "LOW", "PASS")
    return KBItem.query.paginate(1, 500, False)
