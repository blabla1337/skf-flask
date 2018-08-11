from skf.database import db
class chatbot_post(db.Model):
    id1 = db.Column(db.Integer, primary_key=True)
    question = db.Column(db.String)
    def __init__(self, id1, question):
        self.id1 = id1
        self.question = question
