
from skf.database import db

class lab_items(db.Model):
    labID = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.Text)
    link = db.Column(db.Text)
    
    def __init__(self, title, content):
        self.title = title
        self.link = link