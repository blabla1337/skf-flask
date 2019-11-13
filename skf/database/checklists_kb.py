
from skf.database import db

'''
--
-- Table structure for table `checklists_kb`
--
drop table if exists `checklists_kb`;
CREATE TABLE `checklists_kb` (
    `id` INTEGER PRIMARY KEY AUTOINCREMENT,
    `checklistID` varchar(255) NOT NULL,
    `content` varchar(255) NOT NULL,
    `cwe` int(11) NOT NULL,
    `question_ID` int(11) NOT NULL,
    `include_always` boolean,
    `kbID` int(11) NOT NULL,
    `checklist_type` int(11) NOT NULL
); 
'''

class ChecklistKB(db.Model):
    
    __tablename__ = 'checklists_kb'
    
    id = db.Column(db.Integer, primary_key=True)

    checklist_id = db.Column(db.String(255), nullable=False)
    content = db.Column(db.Text)
    cwe = db.Column(db.Integer)
    maturity = db.Column(db.Integer, nullable=True)
    question_id = db.Column(db.Integer, db.ForeignKey('questions.id'), nullable=True)
    questions = db.relationship("Question", backref=db.backref('checklist_kb'))
    include_always = db.Column(db.Boolean)
    kb_id = db.Column(db.Integer, db.ForeignKey("kb_items.kb_id"), nullable=True)
    kb_items = db.relationship("KBItem", backref=db.backref('checklist_kb'))
    checklist_type = db.Column(db.Integer, nullable=False)

    def __init__(self, checklist_id, content, checklist_type, include_always, cwe, maturity):
        self.include_always = include_always
        self.checklist_id = checklist_id
        self.checklist_type = checklist_type
        self.content = content
        self.cwe = cwe 
        self.maturity = maturity 
