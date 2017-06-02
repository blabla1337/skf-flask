from skf.database import db
from skf.api.security import log, val_num, val_float
from skf.database.checklists import checklists
from skf.database.checklists_kb import checklists_kb


def get_checklist_item(checklist_id):
    log("User requested specific checklist item", "LOW", "PASS")
    val_float(checklist_id)
    result = checklists_kb.query.filter(checklists_kb.checklistID == checklist_id).one()
    if not result:
        log("User triggered error requesting specific checklist item", "LOW", "FAIL")
    else:
        return result
    

def get_checklist_items():
    log("User requested list of checklist items", "LOW", "PASS")
    result = checklists_kb.query.paginate()
    if not result:
        log("User triggered error requesting list of checklist items", "LOW", "FAIL")
    else:
        return result


def get_checklist_items_lvl(lvl):
    log("User requested list of checklist items based on level", "LOW", "PASS")
    val_num(lvl)
    result = checklists_kb.query.filter(checklists_kb.checklist_items.has(level = 0) | checklists_kb.checklist_items.has(level = lvl)).group_by(checklists_kb.checklistID).all()
    if not result:
        log("User triggered error requesting specific checklist items based on level", "LOW", "FAIL")
    else:
        return result

