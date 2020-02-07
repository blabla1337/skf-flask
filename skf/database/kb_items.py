from skf.database import db

class KBItem(db.Model):
	
    __tablename__ = 'kb_items'
    
    kb_id = db.Column(db.Integer, primary_key=True, autoincrement=False)
    title = db.Column(db.Text)
    content = db.Column(db.Text)
    checklist_category_id = db.Column(db.Integer, db.ForeignKey("checklist_category.id"), nullable=True)
    checklist_category = db.relationship("ChecklistCategory", backref=db.backref('kb_items'))

    def __init__(self, title, content, kb_id):
        self.kb_id = kb_id
        self.title = title
        self.content = content