
from skf.database import db

class ChecklistType(db.Model):
	
    __tablename__ = 'checklist_types'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text, nullable=False)
    description = db.Column(db.Text, nullable=False)
    visibility = db.Column(db.Boolean, nullable=False)
    
    checklist_category_id = db.Column(db.Integer, db.ForeignKey("checklist_category.id"), nullable=True)
    checklist_category = db.relationship("ChecklistCategory", backref=db.backref('checklist_types'))

    def __init__(self, name, description, visibility):
        self.name = name
        self.description = description
        self.visibility = visibility

