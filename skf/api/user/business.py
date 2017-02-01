from skf.database import db
from skf.database.models import users

def activate_user(user_id, data):
    user = users.query.filter(users.userID == user_id).one()
    user.userName = 'lala'
#    if users.query.filter(users.activated == "false").one():
#        if users.query.filter(users.accessToken == data.get('accessToken')).one():
#            if data.get('password') == data.get('repassword'):
#                pw_hash = bcrypt.generate_password_hash(data.get('password')).decode('utf-8')
#                user.password = pw_hash
#                user.access = "true"
#                user.activated = "true"
#                db.session.add(user)
#                db.session.commit()
