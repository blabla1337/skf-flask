
from skf.database import db

class CodeItem(db.Model):

    __tablename__ = 'code_items'

    id = db.Column(db.Integer, primary_key=True)
<<<<<<< HEAD
    title = db.Column(db.Text, nullable=False)
    content = db.Column(db.Text, nullable=False)
    code_lang = db.Column(db.Text, nullable=False)
=======

    title = db.Column(db.Text, nullable=False)
    content = db.Column(db.Text, nullable=False)
    code_lang = db.Column(db.Text, nullable=False)

>>>>>>> origin/master
    checklist_category_id = db.Column(db.Integer, db.ForeignKey("checklist_category.id"), nullable=True)
    checklist_category = db.relationship("ChecklistCategory", backref=db.backref('code_items'))

    def __init__(self, content, title, lang):
    	self.content = content
    	self.title = title
    	self.code_lang = lang
