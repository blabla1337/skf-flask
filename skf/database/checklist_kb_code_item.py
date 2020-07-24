from skf.database import db

class ChecklistKBCodeItem(db.Model):
    
    __tablename__ = 'checklist_kb_code_item'
    
    id = db.Column(db.Integer, primary_key=True)
    checklist_kb_id = db.Column(db.Integer, db.ForeignKey("checklists_kb.id"), nullable=False)
    checklists_kb_items = db.relationship("ChecklistKB", backref=db.backref('checklist_kb_code_item'))
    code_items_id = db.Column(db.Integer, db.ForeignKey("code_items.id"), nullable=False)
    code_items = db.relationship("CodeItem", backref=db.backref('checklist_kb_code_item'))

    def __init__(self, checklist_kb_id, code_items_id):
        self.checklist_kb_id = checklist_kb_id
        self.code_items_id = code_items_id
