
from skf.database import db

class LabItem(db.Model):
	
    __tablename__ = 'lab_items'

    id = db.Column(db.Integer, primary_key=True)

    title = db.Column(db.Text, nullable=False)
    link = db.Column(db.Text, nullable=False)
    level = db.Column(db.Integer, nullable=False)

    def __init__(self, title, link, level):
    	self.title = title
    	self.link = link
    	self.level = level
    