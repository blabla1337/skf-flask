# -*- coding: utf-8 -*-
"""
Foobar
"""

import os, re 
from sqlite3 import dbapi2 as sqlite3
import markdown

from flask import Flask, request, session, g, redirect, url_for, abort, \
     render_template, flash, Markup

# create our little application :)
app = Flask(__name__)

# Load default config and override config from an environment variable
app.config.update(dict(
    DATABASE=os.path.join(app.root_path, 'flaskr.db'),
    DEBUG=True,
    SECRET_KEY='development key',
    USERNAME='admin',
    PASSWORD='default'
))
app.config.from_envvar('FLASKR_SETTINGS', silent=True)


def connect_db():
    """Connects to the specific database."""
    rv = sqlite3.connect(app.config['DATABASE'])
    rv.row_factory = sqlite3.Row
    return rv


def init_db():
    """Initializes the database."""
    db = get_db()
    with app.open_resource('schema.sql', mode='r') as f:
        db.cursor().executescript(f.read())
    db.commit()


@app.cli.command('initdb')
def initdb_command():
    """Creates the database tables."""
    init_db()
    print('Initialized the database.')


def get_db():
    """Opens a new database connection if there is none yet for the
    current application context.
    """
    if not hasattr(g, 'sqlite_db'):
        g.sqlite_db = connect_db()
    return g.sqlite_db

def get_filepaths(directory):
    """
    This function will generate the file names in a directory 
    tree by walking the tree either top-down or bottom-up. For each 
    directory in the tree rooted at directory top (including top itself), 
    it yields a 3-tuple (dirpath, dirnames, filenames).
    """
    file_paths = []  # List which will store all of the full filepaths.

    # Walk the tree.
    for root, directories, files in os.walk(directory):
        for filename in files:
            # Join the two strings in order to form the full filepath.
            filepath = os.path.join(root, filename)
            file_paths.append(filepath)  # Add it to the list.

    return file_paths  # Self-explanatory.

def get_num(x):
    return int(''.join(ele for ele in x if ele.isdigit()))

@app.teardown_appcontext
def close_db(error):
    """Closes the database again at the end of the request."""
    if hasattr(g, 'sqlite_db'):
        g.sqlite_db.close()

@app.route('/')
def show_entries():
    return render_template('login.html')

@app.route('/dashboard', methods=['GET'])
def dashboard():
    if not session.get('logged_in'):
        abort(401)
    return render_template('dashboard.html')

@app.route('/kb-search', methods=['POST'])
def show_kb_search():
    if not session.get('logged_in'):
        abort(401)

    search = request.form['search']
    full_file_paths = []
    full_file_paths = get_filepaths(os.path.join(app.root_path, "markdown"))
    for path in full_file_paths:
	found = re.match('^[A-Za-z]', search)
        if found != None:
            filemd = open(path, 'r').read()
            content = Markup(markdown.markdown(filemd))
            path = path.split("-")
            y = len(path)-3
            kb_name_uri = path[(y)]
            kb_name = kb_name_uri.replace("_", " ")
    return render_template('knowledge-base-search.html', **locals())


@app.route('/kb-item', methods=['POST'])
def show_kb_item():
    if not session.get('logged_in'):
        abort(401)
    
    id = int(request.form['id'])
    items = []
    full_file_paths = []
    full_file_paths = get_filepaths(os.path.join(app.root_path, "markdown"))

    for path in full_file_paths:
        if id == get_num(path):
	    filemd = open(path, 'r').read()
            content = Markup(markdown.markdown(filemd)) 

    return render_template('knowledge-base-item.html', **locals())

@app.route('/knowledge-base', methods=['GET'])
def knowledge_base():
    """Shows the knowledge base markdown files."""
    if not session.get('logged_in'):
        abort(401)
    items = []
    id_items = []
    full_file_paths = []
    full_file_paths = get_filepaths(os.path.join(app.root_path, "markdown"))

    for path in full_file_paths:
        id_item = get_num(path)
        path = path.split("-")
	y = len(path)-3 
	kb_name_uri = path[(y)]
        kb_name = kb_name_uri.replace("_", " ")
        items.append(kb_name)
	id_items.append(id_item)
        
    return render_template('knowledge-base.html', items=items, id_items=id_items)

@app.route('/project-new', methods=['GET'])
def projects():
    if not session.get('logged_in'):
        abort(401)
    return render_template('project-new.html')

@app.route('/project-add', methods=['POST'])
def add_entry():
    if not session.get('logged_in'):
        abort(401)
    db = get_db()
    db.execute('insert into projects (projectName, projectVersion, projectDesc) values (?, ?, ?)',
               [request.form['inputName'], request.form['inputVersion'], request.form['inputDesc']])
    db.commit()
    return redirect(url_for('project_list'))


@app.route('/project-list', methods=['GET'])
def project_list():
    if not session.get('logged_in'):
        abort(401)

    db = get_db()
    cur = db.execute('select projectName, projectVersion, projectDesc, projectID, timestamp from projects order by projectID desc')
    entries = cur.fetchall()
    return render_template('project-list.html', entries=entries)

@app.route('/project-del', methods=['POST'])
def project_del():
    if not session.get('logged_in'):
        abort(401)

    db = get_db()
    db.execute("delete from projects where projectID=?",
               [request.form['projectID']])
    db.commit()
    return render_template('project-del.html')

@app.route('/code-examples', methods=['GET'])
def code_examples():
    if not session.get('logged_in'):
        abort(401)
    return render_template('code-examples.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != app.config['USERNAME']:
            error = 'Invalid username/password'
        elif request.form['password'] != app.config['PASSWORD']:
            error = 'Invalid username/password'
        else:
            session['logged_in'] = True
            return render_template('dashboard.html')
    return render_template('login.html', error=error)

@app.route('/logout', methods=['GET', 'POST'])
def logout():
    session.pop('logged_in', None)
    return redirect(url_for('login'))







