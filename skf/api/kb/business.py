from skf.database import db
from skf.database.models import kb_items


def update_kb_item(kb_id, data):
    kb = kb_items.query.filter(kb_items.kbID == kb_id).one()
    kb.title = data.get('title')
    kb.body = data.get('content')
    db.session.add(kb)
    db.session.commit()
