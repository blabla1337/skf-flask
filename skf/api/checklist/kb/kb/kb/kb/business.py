from skf.database import db
from skf.database.kb_items import kb_items
from skf.api.security import val_num, val_alpha, val_alpha_num

def update_kb_item(kb_id, data):
    kb = kb_items.query.filter(kb_items.kbID == kb_id).one()
    kb.title = data.get('title')
    kb.content = data.get('content')
    val_alpha_num(kb.title)
    val_alpha_num(kb.content)
    db.session.add(kb)
    db.session.commit()
