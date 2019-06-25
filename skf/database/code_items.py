from skf.database import db

class code_items(db.Model):
    codeID = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.Text)
    content = db.Column(db.Text)
    code_lang = db.Column(db.Text)
