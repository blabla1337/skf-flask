
from skf.database import db

'''
--
-- Table structure for table `question_results`
--
drop table if exists `question_results`;
CREATE TABLE `question_results` (
`id` INTEGER PRIMARY KEY AUTOINCREMENT,
`project_id` int(11) NOT NULL,
`sprint_id` int(11) NOT NULL,
`question_id` int(11) NOT NULL,
`result` boolean,
`checklist_type` int(11) NOT NULL
);
'''

class QuestionResult(db.Model):
    
    __tablename__ = 'question_results'

    id = db.Column(db.Integer, primary_key=True)
    project_id = db.Column(db.Integer, db.ForeignKey("projects.id"))
    project = db.relationship("Project", backref=db.backref('question_results'))

    sprint_id = db.Column(db.Integer, db.ForeignKey("project_sprints.sprint_id"))
    sprint = db.relationship("ProjectSprint", backref=db.backref('question_results'))

    question_id = db.Column(db.Integer, db.ForeignKey('questions.id'))
    question = db.relationship("Question", backref=db.backref('question_result'), uselist=False)

    result = db.Column(db.Text)
    checklist_type = db.Column(db.Integer)


    def __init__(self, result, checklist_type):

        self.result = result
        self.checklist_type = checklist_type
