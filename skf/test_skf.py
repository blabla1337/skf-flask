# -*- coding: utf-8 -*-
"""
    SKF Tests
    ~~~~~~~~~

"""

import pytest
import tempfile
import os 
import datetime
import skf


@pytest.fixture
def client(request):
    skf.app.config['TESTING'] = True
    client = skf.app.test_client()
    with skf.app.app_context():
        skf.init_db()
        skf.log = _log
        skf.check_token = _check_token

    def teardown():
        request.addfinalizer(teardown)

    return client

def _log(message, value, threat):
    print "SKF LOG entry Message: '"+message+"' Value: '"+value+"' Threat: '"+threat+"'"

def _check_token():
    """Checks the submitted CSRF token"""
    _log("User supplied not valid CSRF token", "FAIL", "HIGH")

def _login_token():
    """Checks the emailed login token for creation of account"""
    return "AAAA"

def first_login(client):
    return client.post('/create-account', data=dict(
        email="example@owasp.org",
        password="test-skf",
        password2="test-skf",
        token="1234"
    ), follow_redirects=True)

def login(client, username, password):
    first_login(client)
    return client.post('/login', data=dict(
        username=username,
        password=password,
        csrf_token="AAAA"
    ), follow_redirects=True)

def test_empty_db(client):
    """Start with a blank database."""
    rv = client.get('/')
    assert b'Security Knowledge Framework' in rv.data

def test_first_login(client):
    """Make sure login works"""
    rv = first_login(client)
    assert b'First login' in rv.data

def test_login(client):
    """Make sure login works"""
    rv = login(client, "admin", "test-skf")
    assert b'Start new project' in rv.data
    rv = login(client, "foobar", "X")
    assert b'login' in rv.data

def test_knowledge_base_items(client):
    """Make sure knowledge-base items are visible"""
    login(client, "admin", "test-skf")
    rv = client.get('/knowledge-base')
    assert b'Knowledge Base Security Vulnerabilities' in rv.data
    assert b'Filename injection Path traversel' in rv.data
    assert b'Repudiation attack' in rv.data
    assert b'Open forward' in rv.data
    assert b'Verify that the session id is never disclosed' in rv.data
    assert b'Logging guidelines' in rv.data

def test_manage_users(client):
    """Make sure manage users is working"""
    login(client, "admin", "test-skf")
    rv = client.get('/users-manage')
    assert b'admin' in rv.data
    assert b'edit:read:manage:delete' in rv.data

def test_add_user(client):
    """"Make sure we can add users """
    login(client, "admin", "test-skf")
    return client.post('/users-add', data=dict(
        addUser="Create user",
        email="test@localhost",
        privID="3",
        username="Test",
        csrf_token="AAAA"
    ), follow_redirects=True)
    assert b'test@localhost' in rv.data

def test_new_user_group(client):
    """Make sure we can create new user group"""
    login(client, "admin", "test-skf")
    rv = client.get('/group-manage')
    return client.post('/users-add', data=dict(
        groupName="Testing group",
        projectFormSubmit="Create group",
        csrf_token="AAAA"
    ), follow_redirects=True)
    assert b'Add users to groups' in rv.data

def test_add_new_user_group(client):
    """Make sure we can create new user group"""
    login(client, "admin", "test-skf")
    rv = client.get('/group-users')
    return client.post('/group-add-users', data=dict(
        groupName="2",
        test0="2--",
        submit='Add values',
        csrf_token="AAAA"
    ), follow_redirects=True)
    assert b'Test' in rv.data

def test_new_user_login(client):
    """Make sure we cant login with the new user"""
    login(client, "Test", "x")
    rv = client.get('/group-users')
    assert b'bad password' in rv.data

def test_access_new_user_group(client):
    """Make sure we can create new user group"""
    login(client, "admin", "test-skf")
    rv = client.get('/users-manage')
    return client.post('/user-access', data=dict(
        access="true",
        userID="2",
        csrf_token="AAAA"
    ), follow_redirects=True)
    login(client, "Test", "test-skf")
    assert b'Start new project' in rv.data

def test_first_login_post(client):
    """Make sure we setup new user """
    rv = client.get('/first-login')
    return client.post('/create-account', data=dict(
        email="test@localhost",
        password="test-skf",
        password2='test-skf',
        token="AAAA"
    ), follow_redirects=True)
    assert b'bad password' in rv.data

def test_knowledge_base_item(client):
    """Make sure knowledge-base item content works"""
    login(client, "admin", "test-skf")
    rv = client.post('/kb-item', data=dict(
        id=144
    ), follow_redirects=True)
    assert rv.status_code == 200

    rv = client.post('/kb-item', data=dict(
        id=61
    ), follow_redirects=True)
    assert rv.status_code == 200

    rv = client.post('/kb-item', data=dict(
        id=122
    ), follow_redirects=True)
    assert rv.status_code == 200

    rv = client.post('/kb-item', data=dict(
        id=97
    ), follow_redirects=True)
    assert rv.status_code == 200

def test_code_base_items(client):
    """Make sure code-example items are visible"""
    login(client, "admin", "test-skf")
    rv = client.get('/code-examples')
    assert b'Knowledge Base Code Examples' in rv.data
    assert b'File upload' in rv.data
    assert b'Input validation' in rv.data
    assert b'Debug enabling' in rv.data
    assert b'Anti caching headers' in rv.data

def test_code_base_item(client):
    """Make sure code-example item content works"""
    login(client, "admin", "test-skf")
    rv = client.post('/code-item', data=dict(
        id=1
    ), follow_redirects=True)
    assert rv.status_code == 200

    rv = client.post('/code-item', data=dict(
        id=4
    ), follow_redirects=True)
    assert rv.status_code == 200

    rv = client.post('/code-item', data=dict(
        id=6
    ), follow_redirects=True)
    assert rv.status_code == 200

    rv = client.post('/code-item', data=dict(
        id=7
    ), follow_redirects=True)
    assert rv.status_code == 200

    rv = client.post('/code-item', data=dict(
        id=9
    ), follow_redirects=True)
    assert rv.status_code == 200

def test_create_project(client):
    """Make sure skf is able to create new project and shows in listhttps://localhost:5443/project-checklists/1"""
    login(client, "admin", "test-skf")
    rv = client.get('/project-new')
    assert b'Create new project' in rv.data
    rv = client.post('/project-add', data=dict(
        inputDesc="This is a test Description.",
        inputName="SKF Project",
        projectFormSubmit="Create Project", 
        inputVersion="4.1.1",
        csrf_token="AAAA"
    ), follow_redirects=True)
    assert b'is a test Description' in rv.data
    assert b'4.1.1' in rv.data
    assert b'SKF Project' in rv.data

def test_create_project_function(client):
    """Make sure skf is able to create new project functions"""
    login(client, "admin", "test-skf")
    rv = client.get('/project-new')
    rv = client.post('/project-add', data=dict(
        inputDesc="This is a test Description.",
        inputName="SKF Project",
        inputVersion="4.1.1",
        csrf_token="AAAA"
    ), follow_redirects=True)
    rv = client.get('/project-functions/1')
    rv = client.post('/project-function-add', data=dict(
        functionDesc="This is a test Description for the selected release.",
        functionName="SKF Phase 1",
        project_id="1",
        test0="158--24",
        test1="157--22",
        test2="154--20",
        csrf_token="AAAA"
    ), follow_redirects=True)
    rv = client.get('/project-functions/1')
    assert b'Sessions' in rv.data
    assert b'User registration' in rv.data
    assert b'sub-domains' in rv.data
    rv = client.get('/results-functions')
    assert b'SKF Phase' in rv.data
    rv = client.get('/results-function-report/1')
    assert b'Sessions' in rv.data
    assert b'User registration' in rv.data
    assert b'sub-domains' in rv.data
    rv = client.get('/results-function-docx/1')
    assert b'attachment' in rv.headers['Content-Disposition']

def test_create_project_checklist2(client):
    """Make sure skf is able to create, read, download new project checklist"""
    login(client, "admin", "test-skf")
    rv = client.get('/project-new')
    rv = client.post('/project-add', data=dict(
        inputDesc="This is a test Description.",
        inputName="SKF Project",
        inputVersion="4.1.1",
        projectFormSubmit="Create Project", 
        csrf_token="AAAA"
    ), follow_redirects=True)
    rv = client.get('/project-checklists/1')
    #add ASVS level-1 list and check if works
    rv = client.post('/project-checklist-add', data=dict(
        answer1="na",
        answer2="no",
        csrf_token="AAAA",
        listID1="",
        listID2="", 
        projectID="1",
        projectName="1",
        questionID1="431",
        questionID2="432",
        submit="",
        vulnID1="1",
        vulnID2="14"
    ), follow_redirects=True)
    print rv.data
    assert b'SKF Project' in rv.data
    date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
    rv = client.get('/results-checklist-report/'+date)
    assert b'Version management' in rv.data
    rv = client.get('/results-checklist-docx/'+date)
    assert b'attachment' in rv.headers['Content-Disposition']
