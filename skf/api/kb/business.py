from skf.database import db
from skf.database.kb_items import KBItem
from skf.api.security import log, val_num, val_alpha_num, val_alpha_num_special
from sqlalchemy import desc

import sys

def update_kb_item(kbID, data):
    log("User requested update a specific kb item", "LOW", "PASS")
    val_num(kbID)
    val_alpha_num_special(data.get('title'))

    try:
        kb_item = KBItem.query.filter(KBItem.kbID == kbID).first()
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
    val_alpha_num_special(data.get('title'))

    content = data.get('content')
    title = data.get('title')
    
    #grab highest kbID value and +1 it for unique number as kbID
    item = KBItem.query.order_by(desc(KBItem.kbID)).first()
    try:
        kb_item = KBItem(title, content, item.kbID+1)

        db.session.add(kb_item)
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
        kb_item = KBItem.query.filter(KBItem.kbID == kbID).first()

        db.session.delete(kb_item)
        db.session.commit()

    except:
        db.session.rollback()
        raise

    return {'message': 'KB item successfully deleted'}

def get_kb_item(kbID):
    log("User requested specific kb item", "LOW", "PASS")
    val_num(kbID)

    return KBItem.query.filter(KBItem.kbID == kbID).first()


def get_kb_items():
    log("User requested list of kb items", "LOW", "PASS")
    return KBItem.query.paginate(1, 500, False)
