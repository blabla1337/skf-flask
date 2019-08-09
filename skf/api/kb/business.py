from skf.database import db
from skf.database.kb_items import KBItem
from skf.api.security import log, val_num, val_alpha_num
from sqlalchemy import desc

import sys

def update_kb_item(kb_id, data):
    log("User requested update a specific kb item", "LOW", "PASS")
    val_num(kb_id)
    val_alpha_num(data.get('title'))

    try:
        kb_item = KBItem.query.filter(KBItem.kb_id == kb_id).first()
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
    #grab highest kb_id value and +1 it for unique number as kb_id
    item = KBItem.query.order_by(desc(KBItem.kb_id)).first()
    try:
        kb_item = KBItem(title, content, item.kb_id+1)

        db.session.add(kb_item)
        db.session.commit()

    except:
        db.session.rollback()
        raise

    return {'message': 'KB item successfully created'} 

def delete_kb_item(kb_id, user_id):
    log("User deleted kb item", "MEDIUM", "PASS")
    val_num(kb_id)
    val_num(user_id)

    try:
        kb_item = KBItem.query.filter(KBItem.kb_id == kb_id).first()

        db.session.delete(kb_item)
        db.session.commit()

    except:
        db.session.rollback()
        raise

    return {'message': 'KB item successfully deleted'}

def get_kb_item(kb_id):
    log("User requested specific kb item", "LOW", "PASS")
    val_num(kb_id)

    return KBItem.query.filter(KBItem.kb_id == kb_id).first()


def get_kb_items():
    log("User requested list of kb items", "LOW", "PASS")
    return KBItem.query.paginate(1, 500, False)
