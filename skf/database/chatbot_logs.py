from skf.database import db


class chatbot_post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    question = db.Column(db.String)   

    def __init__(self, id, question):
        self.id = id
        self.question = question
