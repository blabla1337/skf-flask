# -*- coding: utf-8 -*-
"""
    SKF Tests
    ~~~~~~~~~~~~

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

def login(client, username, password):
    return client.post('/login', data=dict(
        username=username,
        password=password,
        csrf_token="AAAA"
    ), follow_redirects=True)


def test_empty_db(client):
    """Start with a blank database."""
    rv = client.get('/')
    assert b'Security Knowledge Framework' in rv.data


def test_login(client):
    """Make sure login works"""
    rv = login(client, skf.app.config['USERNAME'], skf.app.config['PASSWORD'])
    assert b'New Project' in rv.data
    rv = login(client, skf.app.config['USERNAME'], skf.app.config['PASSWORD'] + 'x')
    assert b'UNLOCK' in rv.data

def test_knowledge_base_items(client):
    """Make sure knowledge-base items are visible"""
    login(client, skf.app.config['USERNAME'], skf.app.config['PASSWORD'])
    rv = client.get('/knowledge-base')
    assert b'Knowledge Base Security Vulnerabilities' in rv.data
    assert b'Filename injection Path traversel' in rv.data
    assert b'Repudiation attack' in rv.data
    assert b'Open forward & Open redirects' in rv.data
    assert b'Verify that the session id is never disclosed' in rv.data
    assert b'Logging guidelines' in rv.data

def test_knowledge_base_item(client):
    """Make sure knowledge-base item content works"""
    login(client, skf.app.config['USERNAME'], skf.app.config['PASSWORD'])
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


def test_knowledge_base_item_search(client):
    """Make sure knowledge-base item search works"""
    login(client, skf.app.config['USERNAME'], skf.app.config['PASSWORD'])
    rv = client.post('/kb-search', data=dict(
        search="input"
    ), follow_redirects=True)
    assert b'Single input validation controls' in rv.data
    assert b'Input validation ' in rv.data

def test_code_base_items(client):
    """Make sure code-example items are visible"""
    login(client, skf.app.config['USERNAME'], skf.app.config['PASSWORD'])
    rv = client.get('/code-examples')
    assert b'Knowledge Base Code Examples' in rv.data
    assert b'File upload' in rv.data
    assert b'Input validation' in rv.data
    assert b'Single input validation validation' in rv.data
    assert b'Debug enabling' in rv.data
    assert b'Anti caching headers' in rv.data

def test_code_base_item(client):
    """Make sure code-example item content works"""
    login(client, skf.app.config['USERNAME'], skf.app.config['PASSWORD'])
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

def test_code_base_item_search(client):
    """Make sure code example item search works"""
    login(client, skf.app.config['USERNAME'], skf.app.config['PASSWORD'])
    rv = client.post('/code-search', data=dict(
        search="headers"
    ), follow_redirects=True)
    assert b'Anti clickjacking headers' in rv.data
    assert b'Anti caching headers' in rv.data

def test_create_project(client):
    """Make sure skf is able to create new project and shows in listhttps://localhost:5443/project-checklists/1"""
    login(client, skf.app.config['USERNAME'], skf.app.config['PASSWORD'])
    rv = client.get('/project-new')
    assert b'Create new project' in rv.data
    rv = client.post('/project-add', data=dict(
        inputDesc="This is a test Description.",
        inputName="SKF Project",
        inputVersion="4.1.1",
        csrf_token="AAAA"
    ), follow_redirects=True)
    assert b'history of your projects' in rv.data
    assert b'SKF Project' in rv.data

def test_create_project_function(client):
    """Make sure skf is able to create new project functions"""
    login(client, skf.app.config['USERNAME'], skf.app.config['PASSWORD'])
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
        test0="152--24",
        test1="3--17",
        test2="46--1",
        csrf_token="AAAA"
    ), follow_redirects=True)
    rv = client.get('/project-functions/1')
    assert b'SQL commands' in rv.data
    assert b'Access controls or Login systems' in rv.data
    assert b'JSON' in rv.data
    rv = client.get('/results-functions')
    assert b'SKF Phase' in rv.data
    rv = client.get('/results-function-report/1')
    assert b'SQL commands' in rv.data
    assert b'Access controls or Login systems' in rv.data
    assert b'JSON' in rv.data
    rv = client.get('/results-function-docx/1')
    assert b'attachment' in rv.headers['Content-Disposition']

def test_create_project_checklist1(client):
    """Make sure skf is able to create, read, download new project checklist"""
    login(client, skf.app.config['USERNAME'], skf.app.config['PASSWORD'])
    rv = client.get('/project-new')
    rv = client.post('/project-add', data=dict(
        inputDesc="This is a test Description.",
        inputName="SKF Project",
        inputVersion="4.1.1",
        csrf_token="AAAA"
    ), follow_redirects=True)
    rv = client.get('/project-checklists/1')
    #add owasp top 10 list and check if works
    rv = client.post('/project-checklist-add', data=dict(
        answer1="no",
        questionID1="101",
        vulnID1="14",
        listID1="owasp",
        answer2="yes",
        questionID2="102",
        vulnID2="62",
        listID2="owasp",
        answer3="yes",
        questionID3="103",
        vulnID3="63",
        listID3="owasp",
        answer4="yes",
        questionID4="104",
        vulnID4="16",
        listID4="owasp",
        answer5="yes",
        questionID5="105",
        vulnID5="61",
        listID5="owasp",
        answer6="yes",
        questionID6="106",
        vulnID6="64",
        listID6="owasp",
        answer7="yes",
        questionID7="108",
        vulnID7="65",
        listID7="owasp",
        answer8="yes",
        questionID8="109",
        vulnID8="52",
        listID8="owasp",
        answer9="yes",
        questionID9="110",
        vulnID9="42",
        listID9="owasp",
        answer10="yes",
        questionID10="111",
        vulnID10="19",
        listID10="owasp",
        answer11="yes",
        questionID11="112",
        vulnID11="31",
        listID11="owasp",
        answer12="yes",
        questionID12="114",
        vulnID12="66",
        listID12="owasp",
        answer13="yes",
        questionID13="115",
        vulnID13="66",
        listID13="owasp",
        answer14="yes",
        questionID14="116",
        vulnID14="44",
        listID14="owasp",
        answer15="yes",
        questionID15="118",
        vulnID15="5",
        listID15="owasp",
        answer16="yes",
        questionID16="120",
        vulnID16="14",
        listID16="owasp",
        answer17="no",
        questionID17="122",
        vulnID17="67",
        listID17="owasp",
        answer18="yes",
        questionID18="76",
        vulnID18="47",
        listID18="owasp",
        answer19="yes",
        questionID19="77",
        vulnID19="49",
        listID19="owasp",
        answer20="yes",
        questionID20="78",
        vulnID20="50",
        listID20="owasp",
        answer21="yes",
        questionID21="79",
        vulnID21="46",
        listID21="owasp",
        answer22="yes",
        questionID22="80",
        vulnID22="1",
        listID22="owasp",
        answer23="yes",
        questionID23="81",
        vulnID23="8",
        listID23="owasp",
        answer24="yes",
        questionID24="82",
        vulnID24="4",
        listID24="owasp",
        answer25="yes",
        questionID25="83",
        vulnID25="7",
        listID25="owasp",
        answer26="yes",
        questionID26="84",
        vulnID26="32",
        listID26="owasp",
        answer27="yes",
        questionID27="85",
        vulnID27="39",
        listID27="owasp",
        answer28="yes",
        questionID28="86",
        vulnID28="38",
        listID28="owasp",
        answer29="yes",
        questionID29="87",
        vulnID29="40",
        listID29="owasp",
        answer30="yes",
        questionID30="88",
        vulnID30="6",
        listID30="owasp",
        answer31="yes",
        questionID31="89",
        vulnID31="34",
        listID31="owasp",
        answer32="yes",
        questionID32="90",
        vulnID32="13",
        listID32="owasp",
        answer33="yes",
        questionID33="92",
        vulnID33="3",
        listID33="owasp",
        answer34="yes",
        questionID34="93",
        vulnID34="3",
        listID34="owasp",
        answer35="no",
        questionID35="94",
        vulnID35="3",
        listID35="owasp",
        answer36="yes",
        questionID36="95",
        vulnID36="3",
        listID36="owasp",
        answer37="yes",
        questionID37="96",
        vulnID37="3",
        listID37="owasp",
        answer38="yes",
        questionID38="99",
        vulnID38="44",
        listID38="owasp",
        projectID="1",
        projectName="SKF Project",
        csrf_token="AAAA"
    ), follow_redirects=True)
    assert b'SKF Project' in rv.data
    assert b'owasp' in rv.data
    date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
    rv = client.get('/results-checklist-report/'+date)
    assert b'Checklist: owasp' in rv.data
    rv = client.get('/results-checklist-docx/'+date)
    assert b'attachment' in rv.headers['Content-Disposition']

def test_create_project_checklist2(client):
    """Make sure skf is able to create, read, download new project checklist"""
    login(client, skf.app.config['USERNAME'], skf.app.config['PASSWORD'])
    rv = client.get('/project-new')
    rv = client.post('/project-add', data=dict(
        inputDesc="This is a test Description.",
        inputName="SKF Project",
        inputVersion="4.1.1",
        csrf_token="AAAA"
    ), follow_redirects=True)
    rv = client.get('/project-checklists/1')
    #add ASVS level-1 list and check if works
    rv = client.post('/project-checklist-add', data=dict(
        answer1="no",
        questionID1="154",
        vulnID1="45",
        listID1="ASVS-level-1",
        answer2="yes",
        questionID2="155",
        vulnID2="113",
        listID2="ASVS-level-1",
        answer3="yes",
        questionID3="156",
        vulnID3="43",
        listID3="ASVS-level-1",
        answer4="yes",
        questionID4="157",
        vulnID4="114",
        listID4="ASVS-level-1",
        answer5="yes",
        questionID5="158",
        vulnID5="122",
        listID5="ASVS-level-1",
        answer6="yes",
        questionID6="159",
        vulnID6="28",
        listID6="ASVS-level-1",
        answer7="yes",
        questionID7="160",
        vulnID7="70",
        listID7="ASVS-level-1",
        answer8="yes",
        questionID8="161",
        vulnID8="63",
        listID8="ASVS-level-1",
        answer9="yes",
        questionID9="163",
        vulnID9="132",
        listID9="ASVS-level-1",
        answer10="yes",
        questionID10="164",
        vulnID10="57",
        listID10="ASVS-level-1",
        answer11="yes",
        questionID11="165",
        vulnID11="60",
        listID11="ASVS-level-1",
        answer12="yes",
        questionID12="166",
        vulnID12="90",
        listID12="ASVS-level-1",
        answer13="yes",
        questionID13="167",
        vulnID13="91",
        listID13="ASVS-level-1",
        answer14="yes",
        questionID14="168",
        vulnID14="39",
        listID14="ASVS-level-1",
        answer15="yes",
        questionID15="169",
        vulnID15="38",
        listID15="ASVS-level-1",
        answer16="yes",
        questionID16="171",
        vulnID16="44",
        listID16="ASVS-level-1",
        answer17="yes",
        questionID17="172",
        vulnID17="45",
        listID17="ASVS-level-1",
        answer18="yes",
        questionID18="173",
        vulnID18="45",
        listID18="ASVS-level-1",
        answer19="yes",
        questionID19="174",
        vulnID19="34",
        listID19="ASVS-level-1",
        answer20="no",
        questionID20="175",
        vulnID20="61",
        listID20="ASVS-level-1",
        answer21="yes",
        questionID21="176",
        vulnID21="93",
        listID21="ASVS-level-1",
        answer22="yes",
        questionID22="177",
        vulnID22="82",
        listID22="ASVS-level-1",
        answer23="yes",
        questionID23="178",
        vulnID23="5",
        listID23="ASVS-level-1",
        answer24="yes",
        questionID24="180",
        vulnID24="146",
        listID24="ASVS-level-1",
        answer25="yes",
        questionID25="181",
        vulnID25="94",
        listID25="ASVS-level-1",
        answer26="yes",
        questionID26="182",
        vulnID26="95",
        listID26="ASVS-level-1",
        answer27="yes",
        questionID27="183",
        vulnID27="46",
        listID27="ASVS-level-1",
        answer28="yes",
        questionID28="184",
        vulnID28="11",
        listID28="ASVS-level-1",
        answer29="yes",
        questionID29="185",
        vulnID29="4",
        listID29="ASVS-level-1",
        answer30="yes",
        questionID30="186",
        vulnID30="6",
        listID30="ASVS-level-1",
        answer31="yes",
        questionID31="187",
        vulnID31="8",
        listID31="ASVS-level-1",
        answer32="yes",
        questionID32="188",
        vulnID32="3",
        listID32="ASVS-level-1",
        answer33="yes",
        questionID33="190",
        vulnID33="15",
        listID33="ASVS-level-1",
        answer34="yes",
        questionID34="192",
        vulnID34="140",
        listID34="ASVS-level-1",
        answer35="yes",
        questionID35="193",
        vulnID35="72",
        listID35="ASVS-level-1",
        answer36="yes",
        questionID36="195",
        vulnID36="101",
        listID36="ASVS-level-1",
        answer37="yes",
        questionID37="197",
        vulnID37="129",
        listID37="ASVS-level-1",
        answer38="yes",
        questionID38="198",
        vulnID38="104",
        listID38="ASVS-level-1",
        answer39="yes",
        questionID39="199",
        vulnID39="20",
        listID39="ASVS-level-1",
        answer40="yes",
        questionID40="201",
        vulnID40="67",
        listID40="ASVS-level-1",
        answer41="yes",
        questionID41="202",
        vulnID41="1",
        listID41="ASVS-level-1",
        answer42="yes",
        questionID42="203",
        vulnID42="13",
        listID42="ASVS-level-1",
        answer43="yes",
        questionID43="204",
        vulnID43="1",
        listID43="ASVS-level-1",
        answer44="yes",
        questionID44="205",
        vulnID44="1",
        listID44="ASVS-level-1",
        answer45="no",
        questionID45="206",
        vulnID45="112",
        listID45="ASVS-level-1",
        projectID="1",
        projectName="SKF Project",
        csrf_token="AAAA"
    ), follow_redirects=True)
    assert b'SKF Project' in rv.data
    assert b'ASVS-level-1' in rv.data
    date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
    rv = client.get('/results-checklist-report/'+date)
    assert b'Checklist: ASVS-level-1' in rv.data
    rv = client.get('/results-checklist-docx/'+date)
    assert b'attachment' in rv.headers['Content-Disposition']


