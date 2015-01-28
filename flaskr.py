# -*- coding: utf-8 -*-
"""
Foobar
"""

import os, re, markdown 
from functools import wraps
from sqlite3 import dbapi2 as sqlite3
from flask import Flask, request, session, g, redirect, url_for, abort, \
     render_template, flash, Markup, make_response

# create our little application :)
app = Flask(__name__)

def add_response_headers(headers={}):
    """This decorator adds the headers passed in to the response"""
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            resp = make_response(f(*args, **kwargs))
            h = resp.headers
            for header, value in headers.items():
                h[header] = value
            return resp
        return decorated_function
    return decorator

def security(f):
    """This decorator passes X-Robots-Tag: noindex"""
    return add_response_headers({'X-Frame-Options': 'deny', 'X-XSS-Protection': '1', 'X-Content-Type-Options': 'nosniff', 'Cache-Control': 'no-store, no-cache', 'Server': 'Security Knowledge Framework'})(f)

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

def projects_functions_techlist():
    if not session.get('logged_in'):
        abort(401)

    db = get_db()
    cur = db.execute('select techID, techName, vulnID from techhacks order by techID desc')
    entries = cur.fetchall()
    return entries 







@app.route('/')
@security
def show_entries():
    session['code_lang'] = "php"
    return render_template('login.html')

@app.route('/dashboard', methods=['GET'])
@security
def dashboard():
    if not session.get('logged_in'):
        abort(401)
    return render_template('dashboard.html')

@app.route('/login', methods=['GET', 'POST'])
@security
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
@security
def logout():
    session.pop('logged_in', None)
    return redirect(url_for('login'))

@app.route('/code/<code_lang>', methods=['GET'])
@security
def set_code_lang(code_lang):
    if not session.get('logged_in'):
        abort(401)
    allowed = "php java python perl"
    found = allowed.find(code_lang)
    if found != -1:
        session['code_lang'] = code_lang
    return redirect(url_for('code_examples'))

@app.route('/code-examples', methods=['GET'])
@security
def code_examples():
    """Shows the knowledge base markdown files."""
    if not session.get('logged_in'):
        abort(401)
    items = []
    id_items = []
    full_file_paths = []
    full_file_paths = get_filepaths(os.path.join(app.root_path, "markdown/code_examples/"+session['code_lang']))


    for path in full_file_paths:
        id_item = get_num(path)
        path = path.split("-")
        y = len(path)-3 
        kb_name_uri = path[(y)]
        kb_name = kb_name_uri.replace("_", " ")
        items.append(kb_name)
        id_items.append(id_item)
        
    return render_template('code-examples.html', items=items, id_items=id_items)

@app.route('/code-search', methods=['POST'])
@security
def show_code_search():
    if not session.get('logged_in'):
        abort(401)

    search = request.form['search']
    full_file_paths = []
    full_file_paths = get_filepaths(os.path.join(app.root_path, "markdown/code_examples/"+session['code_lang']))
    for path in full_file_paths:
        found = path.find(search)
        if found != -1:
            filemd = open(path, 'r').read()
            content = Markup(markdown.markdown(filemd))
            path = path.split("-")
            y = len(path)-3
            kb_name_uri = path[(y)]
            kb_name = kb_name_uri.replace("_", " ")
    return render_template('code-examples-search.html', **locals())

@app.route('/code-item', methods=['POST'])
@security
def show_code_item():
    if not session.get('logged_in'):
        abort(401)
    
    id = int(request.form['id'])
    items = []
    full_file_paths = []
    full_file_paths = get_filepaths(os.path.join(app.root_path, "markdown/code_examples/"+session['code_lang']))

    for path in full_file_paths:
        if id == get_num(path):
            filemd = open(path, 'r').read()
            content = Markup(markdown.markdown(filemd)) 

    return render_template('code-examples-item.html', **locals())

@app.route('/kb-search', methods=['POST'])
@security
def show_kb_search():
    if not session.get('logged_in'):
        abort(401)

    search = request.form['search']
    full_file_paths = []
    full_file_paths = get_filepaths(os.path.join(app.root_path, "markdown/knowledge_base"))
    for path in full_file_paths:
        found = path.find(search)
        if found != -1:
            filemd = open(path, 'r').read()
            content = Markup(markdown.markdown(filemd))
            path = path.split("-")
            y = len(path)-3
            kb_name_uri = path[(y)]
            kb_name = kb_name_uri.replace("_", " ")
    return render_template('knowledge-base-search.html', **locals())


@app.route('/kb-item', methods=['POST'])
@security
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
@security
def knowledge_base():
    """Shows the knowledge base markdown files."""
    if not session.get('logged_in'):
        abort(401)
    items = []
    id_items = []
    full_file_paths = []
    full_file_paths = get_filepaths(os.path.join(app.root_path, "markdown/knowledge_base"))
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
@security
def projects():
    if not session.get('logged_in'):
        abort(401)
    return render_template('project-new.html')

@app.route('/project-add', methods=['POST'])
@security
def add_entry():
    if not session.get('logged_in'):
        abort(401)
    db = get_db()
    db.execute('insert into projects (projectName, projectVersion, projectDesc) values (?, ?, ?)',
               [request.form['inputName'], request.form['inputVersion'], request.form['inputDesc']])
    db.commit()
    return redirect(url_for('project_list'))

@app.route('/project-del', methods=['POST'])
@security
def project_del():
    if not session.get('logged_in'):
        abort(401)

    db = get_db()
    db.execute("delete from projects where projectID=?",
               [request.form['projectID']])
    db.commit()
    return render_template('reload.html')

@app.route('/project-list', methods=['GET'])
@security
def project_list():
    if not session.get('logged_in'):
        abort(401)

    db = get_db()
    cur = db.execute('select projectName, projectVersion, projectDesc, projectID, timestamp from projects order by projectID desc')
    entries = cur.fetchall()
    return render_template('project-list.html', entries=entries)

@app.route('/project-options/<project_id>', methods=['GET'])
@security
def projects_options(project_id):
    if not session.get('logged_in'):
        abort(401)
    return render_template('project-options.html', project_id=project_id)

@app.route('/project-functions/<project_id>', methods=['GET'])
@security
def project_functions(project_id):
    if not session.get('logged_in'):
        abort(401)
    techlist = projects_functions_techlist()
    db = get_db()
    cur = db.execute('select paramID, functionName, functionDesc, projectID, tech, entryDate from parameters order by projectID desc')
    entries = cur.fetchall()
    return render_template('project-functions.html', project_id=project_id, techlist=projects_functions_techlist(), entries=entries)

@app.route('/project-function-del', methods=['POST'])
@security
def function_del():
    if not session.get('logged_in'):
        abort(401)
    id = int(request.form['projectID'])
    db = get_db()
    db.execute("delete from parameters where projectID=? and paramID=?",
               [request.form['projectID'],request.form['paramID']])
    db.commit()
    redirect_url = "/project-functions/"+str(id)
    return redirect(redirect_url)


@app.route('/project-function-add', methods=['POST'])
@security
def add_function():
    if not session.get('logged_in'):
        abort(401)
    id = int(request.form['project_id'])
    f = request.form
    for key in f.keys():
        for value in f.getlist(key):
            found = ""
    	    found = key.find("test")
            if found != -1:
                db = get_db()
                db.execute('insert into parameters (functionName, functionDesc, tech, projectID) values (?, ?, ?, ?)',
                           [request.form['functionName'], request.form['functionDesc'], value, request.form['project_id']])
                db.commit()

    redirect_url = "/project-functions/"+str(id)
    return redirect(redirect_url)









@app.route('/project-checklists/<project_id>', methods=['GET'])
@security
def project_checklists(project_id):
    if not session.get('logged_in'):
        abort(401)
    id = int(project_id)
    owasp_items = []
    owasp_ids = []
    owasp_content = []
    basic_items = []
    basic_ids = []
    basic_content = []
    advanced_items = []
    advanced_ids = []
    advanced_content = []

    full_file_paths = []
    full_file_paths = get_filepaths(os.path.join(app.root_path, "markdown/checklists"))

    for path in full_file_paths:

       found = path.find("owasp10")
       if found != -1:
            owasp_org_path = path
            owasp_path = path.split("-")
            owasp_checklist_name = owasp_path[3]
            owasp_id = get_num(owasp_path[1])
            owasp_items.append(owasp_checklist_name)
            owasp_ids.append(owasp_id)
            filemd = open(owasp_org_path, 'r').read()
            owasp_content.append(Markup(markdown.markdown(filemd)))
            print owasp_id
            print owasp_checklist_name

    for path in full_file_paths:
    
       found = path.find("cs_basic_audit")
       if found != -1:

            basic_org_path = path
            basic_path = path.split("-")
            basic_checklist_name = basic_path[3]
            basic_id = get_num(basic_path[1])
            basic_items.append(basic_checklist_name)
            basic_ids.append(basic_id)
            filemd = open(basic_org_path, 'r').read()
            basic_content.append(Markup(markdown.markdown(filemd)))
            print basic_id
            print basic_checklist_name

    for path in full_file_paths:

       found = path.find("cs_advanced_audit")
       if found != -1:

            advanced_org_path = path
            advanced_path = path.split("-")
            advanced_name = advanced_path[3]
            advanced_id = get_num(advanced_path[1])
            advanced_items.append(advanced_name)
            advanced_ids.append(advanced_id)
            filemd = open(advanced_org_path, 'r').read()
            advanced_content.append(Markup(markdown.markdown(filemd)))
            print advanced_id
            print advanced_name


    return render_template('project-checklists.html', **locals())

