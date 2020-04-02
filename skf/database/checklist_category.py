from skf.database import db

class ChecklistCategory(db.Model):
    
    __tablename__ = 'checklist_category'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False, unique=True)
    description = db.Column(db.Text)
   
    def __init__(self, name, description):
        self.name = name
        self.description = description
