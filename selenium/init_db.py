import os
from flask import Flask
from shutil import copyfile
from sqlite3 import dbapi2 as sqlite3

app = Flask(__name__)

def connect_db():
    """Connects to the specific database."""
    rv = sqlite3.connect("../skf/db/db.sqlite")
    rv.row_factory = sqlite3.Row
    return rv


def update_db():
    """Update the database."""
    db = connect_db()
    with app.open_resource(os.path.join(app.root_path, 'clean.sql'), mode='r') as f:
        db.cursor().executescript(f.read())
    db.commit()

if __name__ == "__main__":
    update_db()
