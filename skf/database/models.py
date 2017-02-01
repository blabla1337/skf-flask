# The examples in this file come from the Flask-SQLAlchemy documentation
# For more information take a look at:
# http://flask-sqlalchemy.pocoo.org/2.1/quickstart/#simple-relationships


from skf.database import db

class kb_items(db.Model):
    kbID = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.Text)
    content = db.Column(db.Text)

    def __init__(self, kbID, content, title):
        self.kbID = kbID
        self.title = title
        self.content = content

    def __repr__(self):
        return '<kb_items %r>' % self.title


class users(db.Model):
    userID = db.Column(db.Integer, primary_key=True)
    privilegeID = db.Column(db.Integer)
    accessToken = db.Column(db.Text)
    userName = db.Column(db.Text)
    password = db.Column(db.Text)
    access = db.Column(db.Text)
    activated = db.Column(db.Text)
    email = db.Column(db.Text)

    def __init__(self, userID, privilegeID, accessToken, userName, password, access, activated, email):
        self.userID = userID
        self.privilegeID = privilegeID
        self.accessToken = accessToken
        self.userName = userName
        self.password = password
        self.access = access
        self.activated = activated
        self.email = email

    def __repr__(self):
        return '<users %r>' % self.userName
