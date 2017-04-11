from skf.database import db
from skf.database.code_items import code_items

def update_code_item(code_id, data):
    code = code_items.query.filter(code_items.codeID == code_id).one()
    code.title = data.get('title')
    code.content = data.get('content')
    code.code_lang = data.get('code_lang')
    db.session.add(code)
    db.session.commit()
