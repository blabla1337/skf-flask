import os, json, unittest, tempfile, skf
from skf import settings
from skf.api.security import log, val_num, val_float, val_alpha, val_alpha_num, security_headers
from skf.db_tools import init_db, connect_db, get_db, init_md_knowledge_base, init_md_checklists, init_md_code_examples
from skf.app import app


class TestRestPlusApi(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.client = app.test_client()
        with app.app_context():
            init_db()
            settings.TESTING = True
            skf.app.initialize_app(app)


    def test_get_status(self):
        """Test if the API GUI is available"""
        response = self.client.get('/api/')
        self.assertEqual(response.status_code, 200)
        assert b'OWASP-SKF API' in response.data


    def test_activate_user(self):
        """Test if the activate user call is working"""
        payload = {'accessToken': 1234, 'email': 'example@owasp.org', 'password': 'admin', 'repassword': 'admin', 'username': 'admin'}
        headers = {'content-type': 'application/json'}
        response = self.client.put('/api/user/activate/1', data=json.dumps(payload), headers=headers)
        self.assertEqual(response.status_code, 200)
        response_dict = json.loads(response.data.decode('utf-8'))
        self.assertTrue(response_dict.get('message'))


    def test_login(self):
        """Test if the login call is working"""
        payload = {'username': 'admin', 'password': 'admin'}
        headers = {'content-type': 'application/json'}
        response = self.client.post('/api/user/login', data=json.dumps(payload), headers=headers)
        self.assertEqual(response.status_code, 200)
        response_dict = json.loads(response.data.decode('utf-8'))
        self.assertTrue(response_dict.get('Authorization token'))


    def test_login_create(self):
        """Test if the login create call is working"""
        jwt = self.login('admin', 'admin')
        payload = {'email': 'test_user@owasp.org', 'privilege': 1}
        headers = {'content-type': 'application/json', 'Authorization': jwt}
        response = self.client.put('/api/user/create', data=json.dumps(payload), headers=headers)
        self.assertEqual(response.status_code, 200)
        response_dict = json.loads(response.data.decode('utf-8'))
        self.assertEqual(response_dict['email'], "test_user@owasp.org")


    def login(self, username, password):
        """Login method needed for testing"""
        payload = {'username': ''+username+'', 'password': ''+password+''}
        headers = {'content-type': 'application/json'}
        response = self.client.post('/api/user/login', data=json.dumps(payload), headers=headers)
        self.assertEqual(response.status_code, 200)
        response_dict = json.loads(response.data.decode('utf-8'))
        return response_dict.get('Authorization token')


    def test_get_checklist(self):
        """Test if the get checklist items call is working"""
        response = self.client.get('/api/checklist/items')
        self.assertEqual(response.status_code, 200)
        response_dict = json.loads(response.data.decode('utf-8'))
        self.assertEqual(response_dict[0]['checklist_items_checklistID'], "1.0")


    def test_get_checklist_fail(self):
        """Test if the get checklist items fail call is working"""
        response = self.client.get('/api/checklist/1337.1337')
        self.assertEqual(response.status_code, 400)


    def test_get_checklist_item_10(self):
        """Test if the get specific checklist item call is working"""
        response = self.client.get('/api/checklist/10.0')
        self.assertEqual(response.status_code, 200)
        response_dict = json.loads(response.data.decode('utf-8'))
        self.assertEqual(response_dict['checklist_items_checklistID'], "10.0")


    def test_get_checklist_items_level(self):
        """Test if the get specific checklist item by level call is working"""
        payload = {'level': '1'}
        headers = {'content-type': 'application/json'}
        response = self.client.post('/api/checklist/level', data=json.dumps(payload), headers=headers)
        self.assertEqual(response.status_code, 200)
        response_dict = json.loads(response.data.decode('utf-8'))
        self.assertEqual(response_dict[0]['checklist_items_content'], "Architecture, design and threat modelling")
        self.assertEqual(response_dict[0]['checklist_items_level'], "0")


    def test_get_kb(self):
        """Test if the get kb items call is working"""
        response = self.client.get('/api/kb/items')
        self.assertEqual(response.status_code, 200)
        response_dict = json.loads(response.data.decode('utf-8'))
        self.assertEqual(response_dict['items'][1]['title'], "External DTD parsing")


    def test_get_kb_item_10(self):
        """Test if the get specific kb item call is working"""
        response = self.client.get('/api/kb/10')
        self.assertEqual(response.status_code, 200)
        response_dict = json.loads(response.data.decode('utf-8'))
        self.assertEqual(response_dict['title'], "Repudiation attack")


    def test_update_kb(self):
        """Test if the update kb items call is working"""
        jwt = self.login('admin', 'admin')        
        payload = {'content': 'Unit test content update', 'title': 'Unit test title update'}
        headers = {'content-type': 'application/json', 'Authorization': jwt}
        response = self.client.put('/api/kb/update/1', data=json.dumps(payload), headers=headers)
        self.assertEqual(response.status_code, 200)
        response_dict = json.loads(response.data.decode('utf-8'))
        self.assertEqual(response_dict['message'], "KB item successfully updated")
        response = self.client.get('/api/kb/items')
        self.assertEqual(response.status_code, 200)
        response_dict = json.loads(response.data.decode('utf-8'))
        self.assertEqual(response_dict['items'][0]['title'], "Unit test title update")


    def test_create_project(self):
        """Test if the create new project call is working"""
        jwt = self.login('admin', 'admin')        
        payload = {'description': 'Unit test description project', 'name': 'Unit test name project', 'version': 'version 1.0'}
        headers = {'content-type': 'application/json', 'Authorization': jwt}
        response = self.client.put('/api/project/new', data=json.dumps(payload), headers=headers)
        self.assertEqual(response.status_code, 200)
        response_dict = json.loads(response.data.decode('utf-8'))
        self.assertEqual(response_dict['message'], "Project successfully created")


    def test_create_project_fail(self):
        """Test if the create new project fail call is working"""
        jwt = self.login('admin', 'admin')        
        payload = {'description_wrong': 'Unit test description project'}
        headers = {'content-type': 'application/json', 'Authorization': jwt}
        response = self.client.put('/api/project/new', data=json.dumps(payload), headers=headers)
        self.assertEqual(response.status_code, 400)


    def test_project_items(self):
        """Test if the project items call is working"""
        jwt = self.login('admin', 'admin') 
        headers = {'Authorization': jwt}
        response = self.client.get('/api/project/items', headers=headers)
        self.assertEqual(response.status_code, 200)
        response_dict = json.loads(response.data.decode('utf-8'))
        self.assertEqual(response_dict['items'][0]['projectName'], "Unit test name project")


    def test_project_item(self):
        """Test if the project item call is working"""
        jwt = self.login('admin', 'admin') 
        headers = {'content-type': 'application/json', 'Authorization': jwt}
        response = self.client.get('/api/project/2', headers=headers)
        self.assertEqual(response.status_code, 200)
        response_dict = json.loads(response.data.decode('utf-8'))
        self.assertEqual(response_dict['projectName'], "Unit test name project")


    def test_update_project_item(self):
        """Test if the project update call is working"""
        jwt = self.login('admin', 'admin') 
        payload = {'description': 'Unit test description project update', 'name': 'Unit test name project update', 'version': 'version 1.1'}
        headers = {'content-type': 'application/json', 'Authorization': jwt}
        response = self.client.put('/api/project/update/2', data=json.dumps(payload), headers=headers)
        self.assertEqual(response.status_code, 200)
        response_dict = json.loads(response.data.decode('utf-8'))
        self.assertEqual(response_dict['message'], "Project successfully updated")
        response = self.client.get('/api/project/2', headers=headers)
        self.assertEqual(response.status_code, 200)
        response_dict = json.loads(response.data.decode('utf-8'))
        self.assertEqual(response_dict['projectName'], "Unit test name project update")


    def test_delete_project_item(self):
        """Test if the delete project item call is working"""
        jwt = self.login('admin', 'admin') 
        payload = {'description': 'Unit test description project', 'name': 'Unit test name project', 'version': 'version 1.0'}
        headers = {'content-type': 'application/json', 'Authorization': jwt}
        response = self.client.put('/api/project/new', data=json.dumps(payload), headers=headers)
        self.assertEqual(response.status_code, 200)
        response_dict = json.loads(response.data.decode('utf-8'))
        self.assertEqual(response_dict['message'], "Project successfully created")
        response = self.client.delete('/api/project/delete/1', headers=headers)
        self.assertEqual(response.status_code, 200)
        response_dict = json.loads(response.data.decode('utf-8'))
        self.assertEqual(response_dict['message'], "Project successfully deleted")


    def test_stats_project_items(self):
        """Test if the stats of sprint call is working"""
        jwt = self.login('admin', 'admin') 
        payload = {'description': 'Unit test description project for sprint', 'name': 'Unit test name project for sprint', 'version': 'version 1.0'}
        headers = {'content-type': 'application/json', 'Authorization': jwt}
        response = self.client.put('/api/project/new', data=json.dumps(payload), headers=headers)
        self.assertEqual(response.status_code, 200)
        response_dict = json.loads(response.data.decode('utf-8'))
        self.assertEqual(response_dict['message'], "Project successfully created")
        payload = {'description': 'Unit test description sprint', 'name': 'Unit test name sprint', 'projectID': '3'}
        response = self.client.put('/api/sprint/new', data=json.dumps(payload), headers=headers)
        self.assertEqual(response.status_code, 200)
        payload = {'questions': [ {'projectID': '3', 'question_sprint_ID': '1','result': 'True', 'sprintID': '4'},{'projectID': '3', 'question_sprint_ID': '2','result': 'True', 'sprintID': '4'} ]}
        response = self.client.put('/api/questions_sprint/store', data=json.dumps(payload), headers=headers)
        self.assertEqual(response.status_code, 200)
        response_dict = json.loads(response.data.decode('utf-8'))
        self.assertEqual(response_dict['message'], "Sprint questions successfully created")
        payload = {'description': 'Unit test description sprint', 'name': 'Unit test name sprint', 'projectID': '3'}
        response = self.client.put('/api/sprint/new', data=json.dumps(payload), headers=headers)
        self.assertEqual(response.status_code, 200)
        payload = {'questions': [ {'projectID': '3', 'question_sprint_ID': '1','result': 'True', 'sprintID': '5'},{'projectID': '3', 'question_sprint_ID': '2','result': 'True', 'sprintID': '5'} ]}
        response = self.client.put('/api/questions_sprint/store', data=json.dumps(payload), headers=headers)
        self.assertEqual(response.status_code, 200)
        response_dict = json.loads(response.data.decode('utf-8'))
        self.assertEqual(response_dict['message'], "Sprint questions successfully created")
        response = self.client.get('/api/project/stats/3', headers=headers)
        self.assertEqual(response.status_code, 200)
        response_dict = json.loads(response.data.decode('utf-8'))
        self.assertEqual(response_dict['project_open'], 71)


    def test_create_sprint(self):
        """Test if the create new sprint call is working"""
        jwt = self.login('admin', 'admin')        
        payload = {'description': 'Unit test description sprint', 'name': 'Unit test name sprint', 'projectID': '1'}
        headers = {'content-type': 'application/json', 'Authorization': jwt}
        response = self.client.put('/api/sprint/new', data=json.dumps(payload), headers=headers)
        self.assertEqual(response.status_code, 200)
        response_dict = json.loads(response.data.decode('utf-8'))
        self.assertEqual(response_dict['message'], "Sprint successfully created")


    def test_create_sprint_fail(self):
        """Test if the create new sprint fail call is working"""
        jwt = self.login('admin', 'admin')        
        payload = {'description_wrong': 'Unit test description sprint'}
        headers = {'content-type': 'application/json', 'Authorization': jwt}
        response = self.client.put('/api/sprint/new', data=json.dumps(payload), headers=headers)
        self.assertEqual(response.status_code, 400)


    def test_sprint_item(self):
        """Test if the sprint item call is working"""
        jwt = self.login('admin', 'admin') 
        headers = {'content-type': 'application/json', 'Authorization': jwt}
        payload = {'description': 'Unit test description sprint', 'name': 'Unit test name sprint', 'projectID': '1'}
        response = self.client.put('/api/sprint/new', data=json.dumps(payload), headers=headers)
        self.assertEqual(response.status_code, 200)
        response_dict = json.loads(response.data.decode('utf-8'))
        self.assertEqual(response_dict['message'], "Sprint successfully created")
        response = self.client.get('/api/sprint/3', headers=headers)
        self.assertEqual(response.status_code, 200)
        response_dict = json.loads(response.data.decode('utf-8'))
        self.assertEqual(response_dict[0]['sprintName'], "Unit test name sprint")


    def test_update_sprint_item(self):
        """Test if the sprint update call is working"""
        jwt = self.login('admin', 'admin') 
        payload = {'description': 'Unit test description sprint update', 'name': 'Unit test name sprint update', 'projectID': '1'}
        headers = {'content-type': 'application/json', 'Authorization': jwt}
        response = self.client.put('/api/sprint/update/2', data=json.dumps(payload), headers=headers)
        self.assertEqual(response.status_code, 200)
        response_dict = json.loads(response.data.decode('utf-8'))
        self.assertEqual(response_dict['message'], "Sprint successfully updated")
        response = self.client.get('/api/sprint/2', headers=headers)
        self.assertEqual(response.status_code, 200)
        response_dict = json.loads(response.data.decode('utf-8'))
        self.assertEqual(response_dict[0]['sprintName'], "Unit test name sprint update")


    def test_delete_sprint_item(self):
        """Test if the delete project item call is working"""
        jwt = self.login('admin', 'admin') 
        payload = {'description': 'Unit test description sprint', 'name': 'Unit test name sprint', 'projectID': '1'}
        headers = {'content-type': 'application/json', 'Authorization': jwt}
        response = self.client.put('/api/sprint/new', data=json.dumps(payload), headers=headers)
        self.assertEqual(response.status_code, 200)
        response_dict = json.loads(response.data.decode('utf-8'))
        self.assertEqual(response_dict['message'], "Sprint successfully created")
        response = self.client.delete('/api/sprint/delete/1', headers=headers)
        self.assertEqual(response.status_code, 200)
        response_dict = json.loads(response.data.decode('utf-8'))
        self.assertEqual(response_dict['message'], "Sprint successfully deleted")


    def test_stats_sprint_items(self):
        """Test if the stats of sprint call is working"""
        jwt = self.login('admin', 'admin') 
        payload = {'description': 'Unit test description project for sprint', 'name': 'Unit test name project for sprint', 'version': 'version 1.0'}
        headers = {'content-type': 'application/json', 'Authorization': jwt}
        response = self.client.put('/api/project/new', data=json.dumps(payload), headers=headers)
        self.assertEqual(response.status_code, 200)
        response_dict = json.loads(response.data.decode('utf-8'))
        self.assertEqual(response_dict['message'], "Project successfully created")
        payload = {'description': 'Unit test description sprint', 'name': 'Unit test name sprint', 'projectID': '1'}
        response = self.client.put('/api/sprint/new', data=json.dumps(payload), headers=headers)
        self.assertEqual(response.status_code, 200)
        payload = {'questions': [ {'projectID': '1', 'question_sprint_ID': '1','result': 'True', 'sprintID': '2'},{'projectID': '1', 'question_sprint_ID': '2','result': 'True', 'sprintID': '2'} ]}
        response = self.client.put('/api/questions_sprint/store', data=json.dumps(payload), headers=headers)
        self.assertEqual(response.status_code, 200)
        response_dict = json.loads(response.data.decode('utf-8'))
        self.assertEqual(response_dict['message'], "Sprint questions successfully created")
        response = self.client.get('/api/sprint/stats/1', headers=headers)
        self.assertEqual(response.status_code, 200)
        response_dict = json.loads(response.data.decode('utf-8'))
        self.assertEqual(response_dict[0]['sprint_open'], 71)


    def test_delete_project_item_fail(self):
        """Test if the delete project item fail call is working"""
        jwt = self.login('admin', 'admin') 
        headers = {'content-type': 'application/json', 'Authorization': jwt}
        response = self.client.delete('/api/project/delete/1', headers=headers)
        self.assertEqual(response.status_code, 400)


    def test_delete_project_item_fail(self):
        """Test if the delete project item fail call is working"""
        jwt = self.login('admin', 'admin') 
        payload = {'description': 'Unit test description project', 'name': 'Unit test name project', 'version': 'version 1.0'}
        headers = {'content-type': 'application/json', 'Authorization': 'woopwoopwrong'}
        response = self.client.put('/api/project/new', data=json.dumps(payload), headers=headers)
        self.assertEqual(response.status_code, 403)
    

    def test_get_code(self):
        """Test if the get code items call is working"""
        response = self.client.get('/api/code/items')
        self.assertEqual(response.status_code, 200)
        response_dict = json.loads(response.data.decode('utf-8'))
        self.assertEqual(response_dict['items'][1]['title'], "Anti clickjacking headers")


    def test_get_code_item_10(self):
        """Test if the get specific code item call is working"""
        response = self.client.get('/api/code/10')
        self.assertEqual(response.status_code, 200)
        response_dict = json.loads(response.data.decode('utf-8'))
        self.assertEqual(response_dict['title'], "Enforce secure passwords")


    def test_update_code(self):
        """Test if the update code items call is working"""
        jwt = self.login('admin', 'admin')        
        payload = {'code_lang': 'php', 'content': 'Unit test content update', 'title': 'Unit test title update'}
        headers = {'content-type': 'application/json', 'Authorization': jwt}
        response = self.client.put('/api/code/update/1', data=json.dumps(payload), headers=headers)
        self.assertEqual(response.status_code, 200)
        response_dict = json.loads(response.data.decode('utf-8'))
        self.assertEqual(response_dict['message'], "Code example item successfully updated")
        response = self.client.get('/api/code/items')
        self.assertEqual(response.status_code, 200)
        response_dict = json.loads(response.data.decode('utf-8'))
        self.assertEqual(response_dict['items'][0]['title'], "Unit test title update")


    def test_get_code_item_lang_php(self):
        """Test if the php language code items call is working"""
        payload = {'code_lang': 'php'}
        headers = {'content-type': 'application/json'}
        response = self.client.post('/api/code/lang/', data=json.dumps(payload), headers=headers)
        self.assertEqual(response.status_code, 200)
        response_dict = json.loads(response.data.decode('utf-8'))
        self.assertEqual(response_dict['items'][0]['title'], "File upload")


    def test_get_code_item_lang_asp(self):
        """Test if the asp language code items call is working"""
        payload = {'code_lang': 'asp'}
        headers = {'content-type': 'application/json'}
        response = self.client.post('/api/code/lang/', data=json.dumps(payload), headers=headers)
        self.assertEqual(response.status_code, 200)
        response_dict = json.loads(response.data.decode('utf-8'))
        self.assertEqual(response_dict['items'][1]['title'], "Anti clickjacking headers")


    def test_get_code_item_lang_java(self):
        """Test if the java language code items call is working"""
        payload = {'code_lang': 'java'}
        headers = {'content-type': 'application/json'}
        response = self.client.post('/api/code/lang/', data=json.dumps(payload), headers=headers)
        self.assertEqual(response.status_code, 200)
        response_dict = json.loads(response.data.decode('utf-8'))
        self.assertEqual(response_dict['items'][1]['title'], "CSRF Token JSF")


    def test_get_questions_sprint_items(self):
        """Test if the questions sprint items call is working"""
        headers = {'content-type': 'application/json'}
        response = self.client.get('/api/questions_sprint/items', headers=headers)
        self.assertEqual(response.status_code, 200)
        response_dict = json.loads(response.data.decode('utf-8'))
        self.assertEqual(response_dict[0]['question'], "Does the sprint implement/changes authentication?")


    def test_store_questions_sprint_items(self):
        """Test if the question sprint items call is working"""
        jwt = self.login('admin', 'admin') 
        payload = {'description': 'Unit test description project for sprint', 'name': 'Unit test name project for sprint', 'version': 'version 1.0'}
        headers = {'content-type': 'application/json', 'Authorization': jwt}
        response = self.client.put('/api/project/new', data=json.dumps(payload), headers=headers)
        self.assertEqual(response.status_code, 200)
        response_dict = json.loads(response.data.decode('utf-8'))
        self.assertEqual(response_dict['message'], "Project successfully created")
        payload = {'questions': [ {'projectID': '3', 'question_sprint_ID': '1','result': 'True', 'sprintID': '1'},{'projectID': '3', 'question_sprint_ID': '2','result': 'True', 'sprintID': '1'} ]}
        response = self.client.put('/api/questions_sprint/store', data=json.dumps(payload), headers=headers)
        self.assertEqual(response.status_code, 200)
        response_dict = json.loads(response.data.decode('utf-8'))
        self.assertEqual(response_dict['message'], "Sprint questions successfully created")


    def test_get_questions_pre_items(self):
        """Test if the questions pre items call is working"""
        headers = {'content-type': 'application/json'}
        response = self.client.get('/api/questions_pre/items', headers=headers)
        self.assertEqual(response.status_code, 200)
        response_dict = json.loads(response.data.decode('utf-8'))
        self.assertEqual(response_dict[0]['question'], "You have a blueprint for the design, architecture and validated this using ASVS?")


    def test_store_questions_pre_items(self):
        """Test if the store question pre items call is working"""
        jwt = self.login('admin', 'admin') 
        payload = {'description': 'Unit test description project for pre', 'name': 'Unit test name project for pre', 'version': 'version 1.0'}
        headers = {'content-type': 'application/json', 'Authorization': jwt}
        response = self.client.put('/api/project/new', data=json.dumps(payload), headers=headers)
        self.assertEqual(response.status_code, 200)
        response_dict = json.loads(response.data.decode('utf-8'))
        self.assertEqual(response_dict['message'], "Project successfully created")
        payload = {'questions': [ {'projectID': '2', 'question_pre_ID': '1','result': 'True'},{'projectID': '2', 'question_pre_ID': '2','result': 'True'} ]}
        response = self.client.put('/api/questions_pre/store', data=json.dumps(payload), headers=headers)
        self.assertEqual(response.status_code, 200)
        response_dict = json.loads(response.data.decode('utf-8'))
        self.assertEqual(response_dict['message'], "Pre questions successfully created")


    def test_update_questions_pre_items(self):
        """Test if the update question pre items call is working"""
        jwt = self.login('admin', 'admin') 
        payload = {'description': 'Unit test description project for pre', 'name': 'Unit test name project for pre', 'version': 'version 1.0'}
        headers = {'content-type': 'application/json', 'Authorization': jwt}
        response = self.client.put('/api/project/new', data=json.dumps(payload), headers=headers)
        self.assertEqual(response.status_code, 200)
        response_dict = json.loads(response.data.decode('utf-8'))
        self.assertEqual(response_dict['message'], "Project successfully created")
        payload = {'questions': [ {'projectID': '2', 'question_pre_ID': '1','result': 'True'},{'projectID': '2', 'question_pre_ID': '2','result': 'True'} ]}
        response = self.client.put('/api/questions_pre/store', data=json.dumps(payload), headers=headers)
        self.assertEqual(response.status_code, 200)
        response_dict = json.loads(response.data.decode('utf-8'))
        self.assertEqual(response_dict['message'], "Pre questions successfully created")
        payload = {'questions': [ {'question_pre_ID': '1','result': 'False'},{'question_pre_ID': '2','result': 'False'} ]}
        response = self.client.put('/api/questions_pre/update/3', data=json.dumps(payload), headers=headers)
        self.assertEqual(response.status_code, 200)
        response_dict = json.loads(response.data.decode('utf-8'))
        self.assertEqual(response_dict['message'], "Pre questions successfully updated")

    def test_assert_403_project_get(self):
        headers = {'content-type': 'application/json'}
        response = self.client.get('/api/project/1')
        self.assertEqual(response.status_code, 403)


    def test_assert_403_project_new(self):
        payload = {'description': 'Unit test description project', 'name': 'Unit test name project', 'version': 'version 1.0'}
        headers = {'content-type': 'application/json'}
        response = self.client.put('/api/project/new', data=json.dumps(payload), headers=headers)
        self.assertEqual(response.status_code, 403)


    def test_assert_403_project_update(self):
        payload = {'description': 'Unit test description project update', 'name': 'Unit test name project update', 'version': 'version 1.1'}
        headers = {'content-type': 'application/json'}
        response = self.client.put('/api/project/update/1', data=json.dumps(payload), headers=headers)
        self.assertEqual(response.status_code, 403)


    def test_assert_403_project_delete(self):
        payload = {'test': 'test'}
        headers = {'content-type': 'application/json'}
        response = self.client.delete('/api/project/delete/1', data=json.dumps(payload), headers=headers)
        self.assertEqual(response.status_code, 403)


    def test_assert_403_user_create(self):
        payload = {'email': 'test_user123@owasp.org', 'privilege': 1}
        headers = {'content-type': 'application/json'}
        response = self.client.put('/api/user/create', data=json.dumps(payload), headers=headers)
        self.assertEqual(response.status_code, 403)



class TestDB(unittest.TestCase):


    def test_connect_db(self):
        """Test if the connect_db is working"""
        self.assertTrue(connect_db())


    def test_init_md_knowledge_base(self):
        """Test if the init markdown of kb items is working"""
        self.assertTrue(init_md_knowledge_base())
        os.remove(os.path.join(app.root_path, 'db.sqlite_schema'))


    def test_init_md_checklists(self):
        """Test if the init markdown of checklist items is working"""
        self.assertTrue(init_md_checklists())
        os.remove(os.path.join(app.root_path, 'db.sqlite_schema'))


    def test_init_md_code_examples(self):
        """Test if the init markdown of code items is working"""
        self.assertTrue(init_md_code_examples())
        os.remove(os.path.join(app.root_path, 'db.sqlite_schema'))


    def test_init_db(self):
        """Test if the init db is working"""
        self.assertTrue(init_db())
        


class TestSecurity(unittest.TestCase):

    def test_val_alpha(self):
        """Test if the val_alpha method is working"""
        self.assertTrue(val_alpha("woopwoop"))
        self.assertFalse(val_alpha("woop %$*@><'1337"))
        self.assertFalse(val_alpha("woop woop 1337"))


    def test_val_num(self):
        """Test if the val_num method is working"""
        self.assertTrue(val_num(1337))
        self.assertFalse(val_num("woopwoop"))        
        self.assertFalse(val_num("woop woop 1337"))
        self.assertFalse(val_num("woop %$*@><'1337"))


    def test_val_alpha_num(self):
        """Test if the val_alpha_num method is working"""
        self.assertTrue(val_alpha_num("woop woop 1337"))
        self.assertFalse(val_alpha_num("woop %$*@><'1337"))


    def test_val_float(self):
        """Test if the val_float method is working"""
        self.assertTrue(val_float(10.11))
        self.assertFalse(val_float(1337))
        self.assertFalse(val_float("woop woop 1337"))
        self.assertFalse(val_float("woop %$*@><'1337"))


    def test_security_headers(self):
        """Test if the security_headers method is working"""
        result_headers = security_headers()
        self.assertEqual(result_headers['X-Frame-Options'], "deny")
        self.assertEqual(result_headers['X-XSS-Protection'], "1")
        self.assertEqual(result_headers['X-Content-Type-Options'], "nosniff")
        self.assertEqual(result_headers['Cache-Control'], "no-store, no-cache")



if __name__ == '__main__':
    unittest.main()
