from skf.database import db

class ProjectSprint(db.Model):
    
    __tablename__ = "project_sprints"

    sprint_id = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.Text)
    description = db.Column(db.Text)

    group_id = db.Column(db.Integer, db.ForeignKey("groups.id"))
    group = db.relationship('Group', backref=db.backref("sprints"))

    project_id = db.Column(db.Integer, db.ForeignKey("projects.id"))
    project = db.relationship('Project', backref=db.backref("sprints"))

    checklist_type_id = db.Column(db.Integer, db.ForeignKey("checklist_types.id"))
    checklist_type = db.relationship('ChecklistType', backref=db.backref("sprints"))

    def __init__(self, name, description):
        self.name = name
        self.description = description
 