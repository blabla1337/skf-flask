from skf.database import db
from skf.database.lab_items import LabItem
from skf.api.security import log, val_num, val_alpha_num

def get_labs():
    log("User requested list of kb items", "LOW", "PASS")
    result = LabItem.query.order_by(LabItem.level.asc()).paginate(1, 500, False)
    return result
