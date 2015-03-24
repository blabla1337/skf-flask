# -*- coding: utf-8 -*-
"""
    Security Knowledge Framework is an expert system application 
    that uses OWASP Application Security Verification Standard, code examples,
    helps developers in pre-development and post-development.  
    Copyright (C) 2015  Glenn ten Cate, Riccardo ten Cate

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU Affero General Public License as
    published by the Free Software Foundation, either version 3 of the
    License, or (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU Affero General Public License for more details.

    You should have received a copy of the GNU Affero General Public License
    along with this program. If not, see <http://www.gnu.org/licenses/>.
"""

import os, markdown, datetime, string, base64, re, sys
from OpenSSL import SSL, rand
from docx import Document
from BeautifulSoup import BeautifulSoup
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.shared import Inches
from functools import wraps 
from sqlite3 import dbapi2 as sqlite3
from flask import Flask, request, session, g, redirect, url_for, abort, \
     render_template, flash, Markup, make_response

# create the application
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
    """This decorator passes multiple security headers and checks log file to block users"""
    blockUsers()
    return add_response_headers({'X-Frame-Options': 'deny', 'X-XSS-Protection': '1', 'X-Content-Type-Options': 'nosniff', 'Cache-Control': 'no-store, no-cache','Strict-Transport-Security': 'max-age=16070400; includeSubDomains', 'Server': 'Security Knowledge Framework'})(f)

def check_token():
    """Checks the submitted CSRF token"""
    if not session.get('csrf_token') == request.form['csrf_token']:
        log("User supplied not valid CSRF token", "FAIL", "HIGH")
        session.clear()
        return abort(500)(f)

def generate_pass():
    chars = string.letters + string.digits + '+/'
    assert 256 % len(chars) == 0  # non-biased later modulo
    PWD_LEN = 12
    generated_pass = ''.join(chars[ord(c) % len(chars)] for c in os.urandom(PWD_LEN))
    return generated_pass

def log(message, value, threat):
    """Create log file and write events triggerd by the user
    The variables: message can be everything, value contains FAIL or SUCCESS and threat LOW MEDIUM HIGH"""
    now = datetime.datetime.now()
    dateLog = now.strftime("%Y-%m")
    dateTime = now.strftime("%Y-%m-%d %H:%M")
    headers_list = request.headers.getlist("X-Forwarded-For")
    ip = headers_list[0] if headers_list else request.remote_addr
    try:
        file = open('logs/'+dateLog+'.txt', 'a+')
    except IOError:
        # If not exists, create the file
        file = open('logs/'+dateLog+'.txt', 'w+')
    file.write(dateTime +' '+ message +' ' + ' ' + value + ' ' + threat + ' ' +ip + "\r\n")
    file.close  

def blockUsers():
    """Check the log file and based on the FAIL items block a user"""
    dateLog  = datetime.datetime.now().strftime("%Y-%m")
    count = 0
    try:
        read = open('logs/'+dateLog+'.txt', 'a+')
    except IOError:
        # If not exists, create the file
        read = open('logs/'+dateLog+'.txt', 'w+')
    for line in read:
        match = re.search('FAIL', line)
        # If-statement after search() tests if it succeeded
        if match:                      
            count += 1   
            str(count) 
            if count > 11:
                sys.exit('Due to to many FAILED logs in your logging file we have the suspicion your application has been under attack by hackers. Please check your log files to validate and take repercussions. After validation clear your log or simply change the FAIL items to another value.')            
    			                
def valAlphaNum(value):
    match = re.findall(r"[^a-zA-Z0-9_-]", value)
    if match:
        log("User supplied not an a-zA-Z0-9 value", "FAIL", "MEDIUM")
        blockUsers()
        abort(406)
        return False
    else:
	    return True

def valNum(value):
    match = re.findall(r'[a-zA-Z_]', str(value))
    if match:
        log("malicious input found", "FAIL", "MEDIUM")
        abort(406)
        return False
    else:
        return True
        
def encodeInput(html):
    """Encode evil chars..."""
    result = re.sub('"', "&quot;", html)
    result = re.sub("'", "&#39;", result)
    result = re.sub("&", "&amp;", result)
    result = re.sub("<", "&lt;", result)
    result = re.sub(">", "&gt;", result)
    log("User supplied input was encoded", "SUCCESS", "NULL")
    blockUsers()
    return result

#secret key for flask internal session use
secret_key = rand.bytes(512)
password   = generate_pass()
csrf_token_raw = rand.bytes(128)
csrf_token = base64.b64encode(csrf_token_raw)
    
# Load default config and override config from an environment variable
# You can also replace password with static password:  PASSWORD='pass!@#example'
app.config.update(dict(
    DATABASE=os.path.join(app.root_path, 'skf.db'),
    DEBUG=True,
    SECRET_KEY=secret_key,
    USERNAME='admin',
    SESSION_COOKIE_SECURE=True,
    PASSWORD=password,
    SESSION_COOKIE_HTTPONLY = True
))


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
    file_paths = [] 
    for root, directories, files in os.walk(directory):
        for filename in files:
            filepath = os.path.join(root, filename)
            file_paths.append(filepath)
    return file_paths  

def get_num(x):
    """get numbers from a string"""
    return int(''.join(ele for ele in x if ele.isdigit()))

@app.teardown_appcontext
def close_db(error):
    """Closes the database again at the end of the request."""
    if hasattr(g, 'sqlite_db'):
        g.sqlite_db.close()

def projects_functions_techlist():
    """get list of technology used for creating project functions"""
    if not session.get('logged_in'):
        abort(401)
    db = get_db()
    cur = db.execute('SELECT techID, techName, vulnID from techhacks ORDER BY techID DESC')
    entries = cur.fetchall()
    return entries 

@app.route('/')
@security
def show_landing():
    """show the loging page and set default code language"""
    session['csrf_token'] = csrf_token
    session['code_lang'] = "php"
    return render_template('login.html', csrf_token=session['csrf_token'])
    
@app.route('/dashboard', methods=['GET'])
@security
def dashboard():
    blockUsers()
    """show the landing page"""
    if not session.get('logged_in'):
        log("User with no valid session tries access to page /dashboard", "FAIL", "HIGH")
        abort(401)
    return render_template('dashboard.html')

@app.route('/login', methods=['GET', 'POST'])
@security
def login():
    blockUsers()
    check_token()
    """validate the login data for access dashboard page"""
    error = None
    if request.method == 'POST':
        if request.form['username'] != app.config['USERNAME']:
            log("Invalid username submit", "FAIL", "LOW")
            valAlphaNum(request.form['username'])
            error = 'Invalid username/password'
        elif request.form['password'] != app.config['PASSWORD']:
            log("Invalid password submit", "FAIL", "LOW")
            error = 'Invalid username/password'
        else:
            log("Valid username/password submit", "SUCCESS", "HIGH")
            session['logged_in'] = True
            session['csrf_token'] = csrf_token
            session['code_lang'] = "php"
            return render_template('dashboard.html')
    return render_template('login.html', error=error, )

@app.route('/logout', methods=['GET', 'POST'])
@security
def logout():
    """logout and destroy session"""
    log("Authenticated session destroyed", "SUCCESS", "LOW")
    session.pop('logged_in', None)
    session.clear()
    return redirect(url_for('login'))

@app.route('/code/<code_lang>', methods=['GET'])
@security
def set_code_lang(code_lang):
    blockUsers()
    """set a code language: php java python perl"""
    if not session.get('logged_in'):
        log("User with no valid session tries access to page /code", "FAIL", "HIGH")
        abort(401)
    allowed = "php java python perl"
    valAlphaNum(code_lang)
    safe_code_lang = encodeInput(code_lang)
    found = allowed.find(safe_code_lang)
    if found != -1:
        #to do below security issue... Create white-list of the languages
        session['code_lang'] = safe_code_lang
    return redirect(url_for('code_examples'))

@app.route('/code-examples', methods=['GET'])
@security
def code_examples():
    blockUsers()
    """Shows the knowledge base markdown files."""
    if not session.get('logged_in'):
        log("User with no valid session tries access to page /code-examples", "FAIL", "HIGH")
        abort(401)
    items = []
    id_items = []
    full_file_paths = []
    allowed = set(string.ascii_lowercase + string.ascii_uppercase + '.')
    if set(session['code_lang']) <= allowed:
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
    blockUsers()
    """show the landing page"""
    if not session.get('logged_in'):
        log("User with no valid session tries access to page /code-search", "FAIL", "HIGH")
        abort(401)
    search = request.form['search'].lower()
    valAlphaNum(search)
    safe_search = encodeInput(search)
    content = []
    kb_name = []
    full_file_paths = []
    allowed = set(string.ascii_lowercase + string.ascii_uppercase + '.')
    if set(session['code_lang']) <= allowed:
        full_file_paths = get_filepaths(os.path.join(app.root_path, "markdown/code_examples/"+session['code_lang']))
        for path in full_file_paths:
            path_lwr = path.lower()
            found = path_lwr.find(safe_search)
            if found != -1:
                filemd = open(path, 'r').read()
                content.append(Markup(markdown.markdown(filemd)))
                path = path.split("-")
                y = len(path)-3
                kb_name_uri = path[(y)]
                kb_name.append(kb_name_uri.replace("_", " "))
    return render_template('code-examples-search.html', **locals())

@app.route('/code-item', methods=['POST'])
@security
def show_code_item():
    blockUsers()
    """show the coding examples page"""
    if not session.get('logged_in'):
        log("User with no valid session tries access to page /code-item", "FAIL", "HIGH")
        abort(401)
    id = int(request.form['id'])
    valNum(id)
    items = []
    full_file_paths = []
    allowed = set(string.ascii_lowercase + string.ascii_uppercase + '.')
    if set(session['code_lang']) <= allowed:
        full_file_paths = get_filepaths(os.path.join(app.root_path, "markdown/code_examples/"+session['code_lang']))
        for path in full_file_paths:
            if id == get_num(path):
                filemd = open(path, 'r').read()
                content = Markup(markdown.markdown(filemd)) 
    return render_template('code-examples-item.html', **locals())

@app.route('/kb-search', methods=['POST'])
@security
def show_kb_search():
    blockUsers()
    """show the knowledge base search page"""
    if not session.get('logged_in'):
        log("User with no valid session tries access to page /kb-search", "FAIL", "HIGH")
        abort(401)
    search = request.form['search'].lower()
    valAlphaNum(search)
    safe_search = encodeInput(search)
    full_file_paths = []
    content = []
    kb_name = []
    full_file_paths = get_filepaths(os.path.join(app.root_path, "markdown/knowledge_base"))
    for path in full_file_paths:
        path_lwr = path.lower()
        found = path_lwr.find(safe_search)
        if found != -1:
            filemd = open(path, 'r').read()
            content.append(Markup(markdown.markdown(filemd)))
            path = path.split("-")
            y = len(path)-3
            kb_name_uri = path[(y)]
            kb_name.append(kb_name_uri.replace("_", " "))
    return render_template('knowledge-base-search.html', **locals())


@app.route('/kb-item', methods=['POST'])
@security
def show_kb_item():
    blockUsers()
    """show the knowledge base search result page"""
    if not session.get('logged_in'):
        log("User with no valid session tries access to page /kb-item", "FAIL", "HIGH")
        abort(401)
    id = int(request.form['id'])
    valNum(id)
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
    blockUsers()
    """Shows the knowledge base markdown files."""
    if not session.get('logged_in'):
        log("User with no valid session tries access to page /knowledge-base", "FAIL", "HIGH")
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
    blockUsers()
    """show the create new project page"""
    if not session.get('logged_in'):
        log("User with no valid session tries access to page /project-new", "FAIL", "HIGH")
        abort(401)     
    return render_template('project-new.html', csrf_token=session['csrf_token'])

@app.route('/project-add', methods=['POST'])
@security
def add_entry():
    blockUsers()
    """add a new project to database"""
    if not session.get('logged_in'):
        log("User with no valid session tries access to page /project-add", "FAIL", "HIGH")
        abort(401)
    check_token()
    db = get_db()
    valAlphaNum(request.form['inputName'])
    valNum(request.form['inputVersion'])
    safe_inputName = encodeInput(request.form['inputName'])
    safe_inputVersion = encodeInput(request.form['inputVersion'])
    safe_inputDesc = encodeInput(request.form['inputDesc'])
    date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
    db.execute('INSERT INTO projects (timestamp, projectName, projectVersion, projectDesc) VALUES (?, ?, ?, ?)',
               [date, safe_inputName, safe_inputVersion, safe_inputDesc])
    db.commit()
    return redirect(url_for('project_list'))

@app.route('/project-del', methods=['POST'])
@security
def project_del():
    blockUsers()
    """delete project from database"""
    if not session.get('logged_in'):
        log("User with no valid session tries access to page /project-del", "FAIL", "HIGH")
        abort(401)
    id = int(request.form['projectID'])
    check_token()
    valNum(id)
    db = get_db()
    db.execute("DELETE FROM projects WHERE projectID=?",
               [id])
    db.commit()
    return render_template('reload.html')

@app.route('/project-list', methods=['GET'])
@security
def project_list():
    blockUsers()
    """show the project list page"""
    if not session.get('logged_in'):
        log("User with no valid session tries access to page /project-list", "FAIL", "HIGH")
        abort(401)
    db = get_db()
    cur = db.execute('SELECT projectName, projectVersion, projectDESC, projectID, timestamp FROM projects ORDER BY projectID DESC')
    entries = cur.fetchall()
    return render_template('project-list.html', entries=entries, csrf_token=session['csrf_token'])

@app.route('/project-options/<project_id>', methods=['GET'])
@security
def projects_options(project_id):
    blockUsers()
    """show the project options landing page"""
    if not session.get('logged_in'):
        log("User with no valid session tries access to page /project-options", "FAIL", "HIGH")
        abort(401)
    valNum(project_id)
    safe_project_id = encodeInput(project_id)
    return render_template('project-options.html', project_id=safe_project_id, csrf_token=session['csrf_token'])

@app.route('/project-functions/<project_id>', methods=['GET'])
@security
def project_functions(project_id):
    blockUsers()
    """show the lproject functions page"""
    if not session.get('logged_in'):
        log("User with no valid session tries access to page /project-functions", "FAIL", "HIGH")
        abort(401)
    techlist = projects_functions_techlist()
    valNum(project_id)
    safe_project_id = encodeInput(project_id)
    db = get_db()
    db.commit()
    cur = db.execute('SELECT p.paramID, p.functionName, p.functionDesc, p.projectID, p.tech, p.techVuln, p.entryDate, t.techName FROM parameters AS p JOIN techhacks AS t ON p.tech = t.techID WHERE p.projectID=? ORDER BY p.projectID DESC',
                      [safe_project_id])
    entries = cur.fetchall()
    return render_template('project-functions.html', project_id=project_id, techlist=projects_functions_techlist(), entries=entries, csrf_token=session['csrf_token'])

@app.route('/project-function-del', methods=['POST'])
@security
def function_del():
    blockUsers()
    """delete a project function"""
    if not session.get('logged_in'):
        log("User with no valid session tries access to page /project-function-del", "FAIL", "HIGH")
        abort(401)
    check_token()
    id = int(request.form['projectID'])
    id_param = int(request.form['paramID'])
    valNum(id)
    valNum(id_param)
    db = get_db()
    db.execute("DELETE FROM parameters WHERE projectID=? AND paramID=?",
               [id,id_param])
    db.commit()
    redirect_url = "/project-functions/"+str(id)
    return redirect(redirect_url)


@app.route('/project-function-add', methods=['POST'])
@security
def add_function():
    blockUsers()
    """add a project function"""
    if not session.get('logged_in'):
        log("User with no valid session tries access to page /project-function-add", "FAIL", "HIGH")
        abort(401)
    check_token()
    id = int(request.form['project_id'])
    valNum(id)
    valAlphaNum(request.form['functionName'])
    valAlphaNum(request.form['functionDesc'])
    safe_fName = encodeInput(request.form['functionName'])
    safe_fDesc = encodeInput(request.form['functionDesc'])
    f = request.form
    for key in f.keys():
        for value in f.getlist(key):
                found = key.find("test")
                if found != -1:
                    db = get_db()
                    date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
                    items = value.split("-")
                    techID = items[2]
                    vulnID = items[0]
                    valAlphaNum(techID)
                    valAlphaNum(vulnID)
                    safe_techID = encodeInput(techID)
                    safe_vulnID = encodeInput(vulnID)
                    db.execute('INSERT INTO parameters (entryDate, functionName, functionDesc, techVuln, tech, projectID) VALUES (?, ?, ?, ?, ?, ?)',
                           [date, safe_fName, safe_fDesc, safe_vulnID, safe_techID, id])
                    db.commit()
    redirect_url = '/project-functions/'+str(id) 
    return redirect(redirect_url)

@app.route('/project-checklist-add', methods=['POST'])
@security
def add_checklist():
    blockUsers()
    """add project checklist"""
    if not session.get('logged_in'):
        log("User with no valid session tries access to page /project-checklist-add", "FAIL", "HIGH")
        abort(401)
    check_token()
    f = request.form
    i = 1
    for key in f.keys():
        for value in f.getlist(key):
            found = key.find("vuln")
            if found != -1:
                listID = "listID"+str(i)
                answerID = "answer"+str(i)
                questionID = "questionID"+str(i) 
                vulnID = "vulnID"+str(i)
                valAlphaNum(request.form[answerID])
                valNum(request.form[questionID])
                valNum(request.form[vulnID])
                valAlphaNum(request.form[listID])
                valAlphaNum(request.form['projectName'])
                valAlphaNum(request.form['projectID'])
                safe_answerID = encodeInput(request.form[answerID])
                safe_questionID = encodeInput(request.form[questionID])
                safe_vulnID = encodeInput(request.form[vulnID])
                safe_listID = encodeInput(request.form[listID])
                safe_pName = encodeInput(request.form['projectName'])
                safe_id = encodeInput(request.form['projectID'])
                date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
                db = get_db()
                db.execute('INSERT INTO questionlist (entryDate, answer, projectName, projectID, questionID, vulnID, listName) VALUES (?, ?, ?, ?, ?, ?, ?)',
                           [date, safe_answerID, safe_pName, safe_id, safe_questionID, safe_vulnID, safe_listID])
                db.commit()
                i += 1
    redirect_url = "/results-checklists"
    return redirect(redirect_url)

@app.route('/project-checklists/<project_id>', methods=['GET'])
@security
def project_checklists(project_id):
    blockUsers()
    """show the project checklists page"""
    if not session.get('logged_in'):
        log("User with no valid session tries access to page /project-checklists", "FAIL", "HIGH")
        abort(401)
    valNum(project_id)
    safe_id = int(project_id)
    db = get_db()
    cur = db.execute('SELECT * FROM projects WHERE projectID=?',
                        [safe_id])
    row = cur.fetchall()
    owasp_items = []
    owasp_ids = []
    owasp_kb_ids = []
    owasp_content = []
    owasp_items_lvl1 = []
    owasp_items_lvl1_ygb = []
    owasp_ids_lvl1 = []
    owasp_kb_ids_lvl1 = []
    owasp_content_lvl1 = []
    owasp_content_desc_lvl1 = []
    owasp_items_lvl2 = []
    owasp_items_lvl2_ygb = []
    owasp_ids_lvl2 = []
    owasp_kb_ids_lvl2 = []
    owasp_content_lvl2 = []
    owasp_content_desc_lvl2 = []
    owasp_items_lvl3 = []
    owasp_items_lvl3_ygb = []
    owasp_ids_lvl3 = []
    owasp_kb_ids_lvl3 = []
    owasp_content_lvl3 = []
    owasp_content_desc_lvl3 = []
    custom_items = []
    custom_ids = []
    custom_kb_ids = []
    custom_content = []
    basic_items = []
    basic_ids = []
    basic_kb_ids = []
    basic_content = []
    advanced_items = []
    advanced_ids = []
    advanced_kb_ids = []
    advanced_content = []
    full_file_paths = []
    full_file_paths = get_filepaths(os.path.join(app.root_path, "markdown/checklists"))
    for path in full_file_paths:
       found = path.find("owasp")
       if found != -1:
            owasp_org_path = path
            owasp_list = "owasp"
            owasp_path = path.split("-")
            owasp_kb = owasp_path[5]
            owasp_checklist_name = owasp_path[3]
            owasp_id = get_num(owasp_path[1])
            owasp_items.append(owasp_checklist_name)
            owasp_ids.append(owasp_id)
            owasp_kb_ids.append(owasp_kb)
            filemd = open(owasp_org_path, 'r').read()
            owasp_content.append(Markup(markdown.markdown(filemd)))
    for path in full_file_paths:
       found = path.find("ASVS-level-1")
       if found != -1:
            owasp_org_path = path
            owasp_list_lvl1 = "ASVS-level-1"
            owasp_path_lvl1 = path.split("-")
            owasp_kb = owasp_path_lvl1[7]
            owasp_id = get_num(owasp_path_lvl1[1])
            owasp_items_lvl1.append(owasp_checklist_name)
            owasp_ids_lvl1.append(owasp_id)
            owasp_items_lvl1_ygb.append(owasp_path_lvl1[9])
            owasp_kb_ids_lvl1.append(owasp_kb)
            filemd = open(owasp_org_path, 'r').read()
            owasp_content_lvl1.append(Markup(markdown.markdown(filemd)))
            full_file_paths_kb = get_filepaths(os.path.join(app.root_path, "markdown/knowledge_base"))
            for path in full_file_paths_kb:
                org_path = path
                path_kb = path.split("markdown")
                path_vuln = get_num(path_kb[1])
                if int(owasp_kb) == int(path_vuln):
                    filemd = open(org_path, 'r').read()
                    description = filemd.split("**") 
                    owasp_content_desc_lvl1.append(description[2])
    for path in full_file_paths:
       found = path.find("ASVS-level-2")
       if found != -1:
            owasp_org_path = path
            owasp_list_lvl2 = "ASVS-level-2"
            owasp_path_lvl2 = path.split("-")
            owasp_kb = owasp_path_lvl2[7]
            owasp_id = get_num(owasp_path_lvl2[1])
            owasp_items_lvl2.append(owasp_checklist_name)
            owasp_ids_lvl2.append(owasp_id)
            owasp_kb_ids_lvl2.append(owasp_kb)
            owasp_items_lvl2_ygb.append(owasp_path_lvl2[9])
            filemd = open(owasp_org_path, 'r').read()
            owasp_content_lvl2.append(Markup(markdown.markdown(filemd)))
            full_file_paths_kb = get_filepaths(os.path.join(app.root_path, "markdown/knowledge_base"))
            for path in full_file_paths_kb:
                org_path = path
                path_kb = path.split("markdown")
                path_vuln = get_num(path_kb[1])
                if int(owasp_kb) == int(path_vuln):
                    filemd = open(org_path, 'r').read()
                    description = filemd.split("**") 
                    owasp_content_desc_lvl2.append(description[2])
    for path in full_file_paths:
       found = path.find("ASVS-level-3")
       if found != -1:
            owasp_org_path = path
            owasp_list_lvl3 = "ASVS-level-3"
            owasp_path_lvl3 = path.split("-")
            owasp_kb = owasp_path_lvl3[7]
            owasp_checklist_name = owasp_path_lvl3[3] +" "+owasp_path_lvl3[4]+" "+owasp_path_lvl3[5]
            owasp_id = get_num(owasp_path_lvl3[1])
            owasp_items_lvl3.append(owasp_checklist_name)
            owasp_ids_lvl3.append(owasp_id)
            owasp_kb_ids_lvl3.append(owasp_kb)
            owasp_items_lvl3_ygb.append(owasp_path_lvl3[9])
            filemd = open(owasp_org_path, 'r').read()
            owasp_content_lvl3.append(Markup(markdown.markdown(filemd)))
            full_file_paths_kb = get_filepaths(os.path.join(app.root_path, "markdown/knowledge_base"))
            for path in full_file_paths_kb:
                org_path = path
                path_kb = path.split("markdown")
                path_vuln = get_num(path_kb[1])
                if int(owasp_kb) == int(path_vuln):
                    filemd = open(org_path, 'r').read()
                    description = filemd.split("**") 
                    owasp_content_desc_lvl3.append(description[2])
    for path in full_file_paths:
       found = path.find("CS_basic_audit")
       if found != -1:
            basic_org_path = path
            basic_list = "CS_basic_audit"
            basic_path = path.split("-")
            basic_kb = basic_path[5]
            basic_checklist_name = basic_path[3]
            basic_id = get_num(basic_path[1])
            basic_items.append(basic_checklist_name)
            basic_ids.append(basic_id)
            basic_kb_ids.append(basic_kb)
            filemd = open(basic_org_path, 'r').read()
            basic_content.append(Markup(markdown.markdown(filemd)))
    for path in full_file_paths:
       found = path.find("CS_advanced_audit")
       if found != -1:
            advanced_org_path = path
            advanced_list = "CS_advanced_audit"
            advanced_path = path.split("-")
            advanced_kb = advanced_path[5]
            advanced_name = advanced_path[3]
            advanced_id = get_num(advanced_path[1])
            advanced_items.append(advanced_name)
            advanced_ids.append(advanced_id)
            advanced_kb_ids.append(advanced_kb)
            filemd = open(advanced_org_path, 'r').read()
            advanced_content.append(Markup(markdown.markdown(filemd)))
    for path in full_file_paths:
       found = path.find("custom")
       if found != -1:
            custom_org_path = path
            custom_list = "custom"
            custom_path = path.split("-")
            custom_kb = custom_path[5]
            custom_name = custom_path[3]
            custom_id = get_num(custom_path[1])
            custom_items.append(custom_name)
            custom_ids.append(custom_id)
            custom_kb_ids.append(custom_kb)
            filemd = open(custom_org_path, 'r').read()
            custom_content.append(Markup(markdown.markdown(filemd)))
    return render_template('project-checklists.html', csrf_token=session['csrf_token'],  **locals())

@app.route('/results-checklists', methods=['GET'])
@security
def results_checklists():
    blockUsers()
    """show the results checklists page"""
    if not session.get('logged_in'):
        log("User with no valid session tries access to page /results-checklists", "FAIL", "HIGH")
        abort(401)
    db = get_db()
    cur = db.execute('SELECT q.answer, q.projectID, q.questionID,  q.vulnID, q.listName, q.entryDate, p.projectName, p.projectVersion, p.projectDesc FROM questionlist AS q JOIN projects AS p ON q.projectID = p.projectID  GROUP BY q.listName, q.entryDate ORDER BY p.projectName ASC')
    entries = cur.fetchall()
    return render_template('results-checklists.html', entries=entries, csrf_token=session['csrf_token'])

@app.route('/results-functions', methods=['GET'])
@security
def results_functions():
    blockUsers()
    """show the results functions page"""
    if not session.get('logged_in'):
        log("User with no valid session tries access to page /results-functions", "FAIL", "HIGH")
        abort(401)
    db = get_db()
    cur = db.execute('SELECT p.projectName, p.projectID, par.entryDate, p.projectDesc, p.projectVersion, par.paramID, par.functionName, par.projectID FROM projects AS p join parameters AS par on p.projectID = par.projectID GROUP BY p.projectVersion ')
    entries = cur.fetchall()
    return render_template('results-functions.html', entries=entries, csrf_token=session['csrf_token'])

@app.route('/results-functions-del', methods=['POST'])
@security
def functions_del():
    blockUsers()
    """delete functions result items"""
    if not session.get('logged_in'):
        log("User with no valid session tries access to page /results-functions-del", "FAIL", "HIGH")
        abort(401)
    check_token()
    safe_entryDate = encodeInput(request.form['entryDate'])
    db = get_db()
    db.execute("DELETE FROM parameters WHERE entryDate=?",
               [safe_entryDate])
    db.commit()
    return render_template('reload.html')

@app.route('/results-checklists-del', methods=['POST'])
@security
def checklists_del():
    blockUsers()
    """delete checklist result item"""
    if not session.get('logged_in'):
        log("User with no valid session tries access to page /results-checklists-del", "FAIL", "HIGH")
        abort(401)
    check_token()
    safe_entryDate = encodeInput(request.form['entryDate'])
    db = get_db()
    db.execute("DELETE FROM questionlist WHERE entryDate=?",
               [safe_entryDate])
    db.commit()
    return render_template('reload.html')


@app.route('/results-checklist-report/<entryDate>', methods=['GET'])
@security
def checklist_results(entryDate):
    blockUsers()
    """show checklist results report"""
    if not session.get('logged_in'):
        log("User with no valid session tries access to page /results-checklist-report", "FAIL", "HIGH")
        abort(401)
    ygb = []
    id_items = []
    questions = []
    content = []
    full_file_paths = []
    safe_entryDate = encodeInput(entryDate)
    db = get_db()
    cur = db.execute("SELECT * FROM questionlist WHERE answer='no' AND entryDate=?",
               [safe_entryDate])
    entries = cur.fetchall()
    for entry in entries:
        projectName = entry[3]
        questionID = entry[4]
        vulnID = entry[5]
        listName = entry[6]
        entryDate = entry[7]
        full_file_paths = get_filepaths(os.path.join(app.root_path, "markdown/knowledge_base"))
        for path in full_file_paths:
            org_path = path
            path = path.split("markdown")
            path_vuln = get_num(path[1])
            if int(vulnID) == int(path_vuln):
                filemd = open(org_path, 'r').read()
                content.append(Markup(markdown.markdown(filemd)))
                full_file_paths = get_filepaths(os.path.join(app.root_path, "markdown/checklists"))
                for path in full_file_paths:
                    org_path = path
                    custom_path = org_path.split("-")
                    path_questionID = get_num(custom_path[1])
                    if int(questionID) == int(path_questionID):
                        filemd = open(org_path, 'r').read()
                        questions.append(Markup(markdown.markdown(filemd)))
                        custom_paths = org_path.split("-")
                        found = custom_paths[3].find("ASVS")
                        if found != -1:
                            ygb.append(custom_paths[9])
    return render_template('results-checklist-report.html', **locals())


@app.route('/results-checklist-docx/<entryDate>')
def download_file_checklist(entryDate):
    blockUsers()
    """Download checklist results report in docx"""
    if not session.get('logged_in'):
        log("User with no valid session tries access to page /results-checklist-docx", "FAIL", "HIGH")
        abort(401)
    ygb_docx = []    
    content_raw = []
    content_checklist = []
    content_title = []
    safe_entryDate = encodeInput(entryDate)
    db = get_db()
    cur = db.execute("SELECT * FROM questionlist WHERE answer='no' AND entryDate=?",
               [safe_entryDate])
    entries = cur.fetchall()
    document = Document()
    document.add_picture('static/img/owaspdocx.png', width=Inches(4.75), height=Inches(1.15))
    last_paragraph = document.paragraphs[-1] 
    last_paragraph.alignment = WD_ALIGN_PARAGRAPH.LEFT
    document.add_heading('Security Knowledge Framework', 0)
    last_paragraph = document.paragraphs[-1] 
    last_paragraph.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p = document.add_paragraph()
    projectName = entries[0][3]
    listName = entries[0][6]
    ygb = False
    p.add_run('Used Checklist: '+listName)
    p.add_run('\r\n')
    p.add_run('Date: '+datetime.datetime.now().strftime("%Y-%m-%d %H:%M"))
    p.add_run('\r\n')
    p.add_run('Project: '+projectName)
    document.add_page_break()
    p = document.add_heading('Table of contents', level=1)
    p.add_run('\r\n')
    document.add_paragraph('Introduction')
    for entry in entries:
        projectName = entry[3]
        questionID = entry[4]
        vulnID = entry[5]
        listName = entry[6]
        entryDate = entry[7]
        full_file_paths = get_filepaths(os.path.join(app.root_path, "markdown/knowledge_base"))
        for path in full_file_paths:
            org_path = path
            path = path.split("markdown")
            path_vuln = get_num(path[1])
            if int(vulnID) == int(path_vuln):
                filemd = open(org_path, 'r').read()
                content = Markup(markdown.markdown(filemd))
                text = ''.join(BeautifulSoup(content).findAll(text=True))
                text_encode = text.encode('utf-8')
                content_title.append(text_encode.splitlines()[0])
                text_encode = text_encode.replace("Solution", "\nSolution");
                content_raw.append(text_encode)
                full_file_paths = get_filepaths(os.path.join(app.root_path, "markdown/checklists"))
                for path in full_file_paths:
                    org_path = path
                    path = path.split("markdown")
                    tmp_path = path[1].split("-")
                    custom_path = get_num(tmp_path[0])
                    path_questionID = custom_path
                    if int(questionID) == int(path_questionID):
                        filemd = open(org_path, 'r').read()
                        content_checklist.append(Markup(markdown.markdown(filemd)))
                        custom_paths = org_path.split("-")
                        found = custom_paths[3].find("ASVS")
                        if found != -1:
                            ygb = True
                            ygb_docx.append(custom_paths[9])
    for item in content_title:
        p = document.add_paragraph(item)
        p.add_run()
    document.add_page_break()
    document.add_heading('Introduction', level=1)
    p = document.add_paragraph(
        'The security knowledge framework is composed by means of the highest security standards currently available and is designed to maintain the integrity of your application, so you and your costumers sensitive data is protected against hackers. This document is provided with a checklist in which the programmers of your application had to run through in order to provide a secure product.'
    )
    p.add_run('\n')
    p = document.add_paragraph(
        'In the post-development stage of the security knowledge framework the developer double-checks his application against a checklist which consists out of several questions asking the developer about different stages of development and the methodology of implementing different types of functionality the application contains. After filling in this checklist the developer gains feedback on the failed checklist items providing him with solutions about how to solve the additional vulnerability\'s found in the application.'
    )
    document.add_page_break()
    i = 0
    for item in content_raw:
        document.add_heading(content_title[i], level=1)
        result = re.sub("<p>", " ", content_checklist[i])
        result1 = re.sub("</p>", " ", result)
        document.add_heading(result1, level=4)
        p = document.add_paragraph(item.partition("\n")[2])
        if ygb == True:
            if ygb_docx[i] == "b":
                image = document.add_picture('static/img/blue.png', width=Inches(0.20))
            elif ygb_docx[i] == "gb":
                image = document.add_picture('static/img/green.png', width=Inches(0.20))
                image = document.add_picture('static/img/blue.png', width=Inches(0.20))
            elif ygb_docx[i] == "ygb":
                image = document.add_picture('static/img/yellow.png', width=Inches(0.20))
                image = document.add_picture('static/img/green.png', width=Inches(0.20))            
                image = document.add_picture('static/img/blue.png', width=Inches(0.20))
        p.add_run("\n")
        document.add_page_break()
        i += 1
    document.save("checklist-security-report.docx")
    headers = {"Content-Disposition": "attachment; filename=%s" % "checklist-security-report.docx"}
    file_path = os.path.join(app.root_path, "checklist-security-report.docx")
    with open("checklist-security-report.docx", 'rb') as f:
        body = f.read()
    return make_response((body, headers))
    
    
@app.route('/results-function-report/<projectID>', methods=['GET'])
@security
def function_results(projectID):
    blockUsers()
    """show checklist results report"""
    if not session.get('logged_in'):
        log("User with no valid session tries access to page /results-function-report", "FAIL", "HIGH")
        abort(401)
    id_items = []
    content = []
    full_file_paths = []
    valNum(projectID)
    safe_id = encodeInput(projectID)
    db = get_db()
    cur = db.execute("SELECT projects.projectName, projects.projectID, projects.projectVersion, parameters.functionName, parameters.tech, parameters.functionDesc, parameters.entryDate, parameters.techVuln, techhacks.techName FROM projects JOIN parameters ON parameters.projectID=projects.projectID JOIN techhacks ON techhacks.techID  = parameters.tech WHERE parameters.projectID=? GROUP BY parameters.tech;",
               [safe_id])
    entries = cur.fetchall()
    for entry in entries:
        projectName = entry[0]
        vulnID = entry[7]
        full_file_paths = get_filepaths(os.path.join(app.root_path, "markdown/knowledge_base"))
        for path in full_file_paths:
            org_path = path
            path = path.split("markdown")
            path_vuln = get_num(path[1])
            if int(vulnID) == int(path_vuln):
                filemd = open(org_path, 'r').read()
                content.append(Markup(markdown.markdown(filemd)))
    return render_template('results-function-report.html', **locals())

@app.route('/results-function-docx/<projectID>')
def download_file_function(projectID):
    blockUsers()
    """Download checklist results report in docx"""
    if not session.get('logged_in'):
        log("User with no valid session tries access to page /results-function-docx", "FAIL", "HIGH")
        abort(401)
    content_raw = []
    content_title = []
    content_tech = []
    valNum(projectID)
    safe_id = encodeInput(projectID)
    db = get_db()
    cur = db.execute("SELECT projects.projectName, projects.projectID, projects.projectVersion, parameters.functionName, parameters.tech, parameters.functionDesc, parameters.entryDate, parameters.techVuln, techhacks.techName FROM projects JOIN parameters ON parameters.projectID=projects.projectID JOIN techhacks ON techhacks.techID  = parameters.tech WHERE parameters.projectID=? GROUP BY parameters.tech;",
               [safe_id])
    entries = cur.fetchall()
    document = Document()
    document.add_picture('static/img/owaspdocx.png', width=Inches(4.75), height=Inches(1.15))
    last_paragraph = document.paragraphs[-1] 
    last_paragraph.alignment = WD_ALIGN_PARAGRAPH.LEFT
    document.add_heading('Security Knowledge Framework', 0)
    last_paragraph = document.paragraphs[-1] 
    last_paragraph.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p = document.add_paragraph()
    projectName = entries[0][0]
    functionName = entries[0][3]
    functionDesc= entries[0][5]
    p.add_run('Function Name: '+functionName)
    p.add_run('\r\n')
    p.add_run('Date: '+datetime.datetime.now().strftime("%Y-%m-%d %H:%M"))
    p.add_run('\r\n')
    p.add_run('Project: '+projectName)
    document.add_page_break()
    p = document.add_heading('Table of contents', level=1)
    p.add_run('\r\n')
    document.add_paragraph('Introduction')
    for entry in entries:
        entryDate = entry[6]
        vulnID = entry[7]
        full_file_paths = get_filepaths(os.path.join(app.root_path, "markdown/knowledge_base"))
        for path in full_file_paths:
            org_path = path
            path = path.split("markdown")
            path_vuln = get_num(path[1])
            if int(vulnID) == int(path_vuln):
                filemd = open(org_path, 'r').read()
                content = Markup(markdown.markdown(filemd))
                text = ''.join(BeautifulSoup(content).findAll(text=True))
                text_encode = text.encode('utf-8')
                content_title.append(text_encode.splitlines()[0])
                text_encode = text_encode.replace("Solution", "\nSolution");
                content_raw.append(text_encode)
    for item in content_title:
        p = document.add_paragraph(item)
        p.add_run()
    document.add_page_break()
    document.add_heading('Introduction', level=1)
    p = document.add_paragraph(
        'The security knowledge framework is composed by means of the highest security standards currently available and is designed to maintain the integrity of your application, so you and your costumers sensitive data is protected against hackers. This document is provided with a checklist in which the programmers of your application had to run through in order to provide a secure product.'
    )
    p.add_run('\n')
    p = document.add_paragraph(
        'In this part of security knowledge framework, al the parameters and variables are audited by means of the information given by the programmer such as the processing techniques. Ech of these techniques contain different types of vulnerabilities when implemented in a inproper fashion. This document will rais awareness about these vulnerabilities, as well as presenting solutions for the right implementation.'
    )
    document.add_page_break()
    i = 0
    for item in content_raw:
        document.add_heading("Knowledge-Base: "+content_title[i], level=1)
        document.add_heading("Technology: "+entries[i][8], level=2)
        p = document.add_paragraph(item.partition("\n")[2])
        p.add_run("\n")
        document.add_page_break()
        i += 1
    document.save('function-security-report.docx')
    headers = {"Content-Disposition": "attachment; filename=%s" % "function-security-report.docx"}
    with open("function-security-report.docx", 'rb') as f:
        body = f.read()
    return make_response((body, headers))

if __name__ == "__main__":
    print("Generated Password for access SKF: "+password)
    if os.path.isfile('server.crt') == False: 
       app.run(host='127.0.0.1', port=5443, ssl_context='adhoc')
    else:
       context = SSL.Context(SSL.TLSv1_METHOD)
       context.use_privatekey_file('server.key')  #Location of Key
       context.use_certificate_file('server.crt') #Location of Cert
       context.set_cipher_list('TLSv1+HIGH:!aNULL:!eNULL:!3DES:@STRENGTH')
       app.run(host='127.0.0.1', port=5443, ssl_context=context)
