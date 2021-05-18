
from skf.database import db

class LabItemCodeFinishedByUser(db.Model):
	
    __tablename__ = 'lab_items_code_finished_by_user'
    __table_args__ = (db.UniqueConstraint('user_id', 'challenge_id', name='unique_component_commit'),)
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, nullable=False)
    challenge_id = db.Column(db.Integer, nullable=False)
    
    def __init__(self, user_id, challenge_id):
        self.user_id = user_id
        self.challenge_id = challenge_id

