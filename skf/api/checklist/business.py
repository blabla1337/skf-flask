from skf.database import db
from skf.api.security import log, val_num, val_float
from skf.database.checklists import checklists
from skf.database.checklists_kb import checklists_kb


def get_checklist_item(checklist_id):
    log("User requested specific checklist item", "LOW", "PASS")
    val_float(checklist_id)
   
    result = checklists_kb.query.filter(checklists_kb.checklistID == checklist_id).one()
    return result
    

def get_checklist_items():
    log("User requested list of checklist items", "LOW", "PASS")
    result = checklists_kb.query.group_by(checklists_kb.checklistID).paginate(1, 1500, False)
    return result


def get_checklist_items_lvl(lvl):
    log("User requested list of checklist items based on level", "LOW", "PASS")
    val_num(lvl)
    if lvl == 1:
        result = checklists_kb.query.filter(checklists_kb.checklist_items.has(level = 0) | checklists_kb.checklist_items.has(level = 1)).group_by(checklists_kb.checklistID).paginate(1, 1500, False)
    elif lvl == 2:
        result = checklists_kb.query.filter(checklists_kb.checklist_items.has(level = 0) | checklists_kb.checklist_items.has(level = 1) | checklists_kb.checklist_items.has(level = 2)).group_by(checklists_kb.checklistID).paginate(1, 1500, False)
    elif lvl == 3:
        result = checklists_kb.query.filter(checklists_kb.checklist_items.has(level = 0) | checklists_kb.checklist_items.has(level = 1) | checklists_kb.checklist_items.has(level = 2) | checklists_kb.checklist_items.has(level = 3)).group_by(checklists_kb.checklistID).paginate(1, 1500, False)
    return result

