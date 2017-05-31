from skf.database import db
from skf.api.security import log, val_float
from skf.database.checklists import checklists
from skf.database.checklists_kb import checklists_kb

def get_checklist_item(checklist_id):
    log("User requested specific checklist item", "LOW", "PASS")
    val_float(checklist_id)
    result = checklists_kb.query.filter(checklists_kb.checklistID == checklist_id).one()
    if not result:
        return False
    else:
        return result