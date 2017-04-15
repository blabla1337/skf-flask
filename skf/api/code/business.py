from skf.database import db
from skf.database.code_items import code_items
from skf.api.security import val_num, val_alpha, val_alpha_num

def update_code_item(code_id, data):
    code = code_items.query.filter(code_items.codeID == code_id).one()
    code.title = data.get('title')
    code.content = data.get('content')
    code.code_lang = data.get('code_lang')
    val_alpha_num(code.title)
    val_alpha(code.code_lang)
    db.session.add(code)
    db.session.commit()
