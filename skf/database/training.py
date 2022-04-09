from skf.database import db

class Training(db.Model):
    
    __tablename__ = 'training'
    __table_args__ = (
        db.PrimaryKeyConstraint('user_id', 'course_id', 'category_id'),
        db.Index('training_index', 'user_id', 'course_id'),
    )

    user_id = db.Column(db.String(255), nullable=False)
    course_id = db.Column(db.String(255), nullable=False)
    category_id = db.Column(db.String(255), nullable=False)

    def __init__(self, user_id, course_id, category_id):
        self.user_id = user_id
        self.course_id = course_id
        self.category_id = category_id
