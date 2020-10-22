from skf.database import db
from skf.database.kb_items import KBItem
from skf.api.security import log, val_num, val_alpha_num, val_alpha_num_special
from sqlalchemy import desc

import sys

def update_kb_item(kb_id, data):
    log("User requested update a specific kb item", "LOW", "PASS")
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


def create_kb_item(data, category_id):
    log("User requested creating a new kb item", "LOW", "PASS")    
    #grab highest kb_id value and +1 it for unique number as kb_id
    item = KBItem.query.order_by(desc(KBItem.kb_id)).first()
    try:
        kb_item = KBItem(data.get('title'), data.get('content'), item.kb_id+1)
        kb_item.checklist_category_id = category_id
        db.session.add(kb_item)
        db.session.commit()
    except:
        db.session.rollback()
        raise
    return {'message': 'KB item successfully created'} 


def delete_kb_item(kb_id):
    log("User deleted kb item", "MEDIUM", "PASS")
    val_num(kb_id)
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
    return KBItem.query.filter(KBItem.kb_id == kb_id).first()


def get_kb_items(category_id):
    log("User requested list of kb items", "LOW", "PASS")
    return KBItem.query.filter((KBItem.checklist_category_id == category_id) | (KBItem.checklist_category_id == 0)).paginate(1, 2500, False)
