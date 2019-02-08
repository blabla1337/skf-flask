
from skf.database import db


class kb_items(db.Model):
    kbID = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.Text)
    content = db.Column(db.Text)
    
    def __init__(self, title, content):
        self.title = title
        self.content = content