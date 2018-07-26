import os, json, unittest, tempfile, skf
from werkzeug.exceptions import BadRequest
from skf import settings
from skf.api.security import log, val_num, val_float, val_alpha, val_alpha_num, security_headers
from skf.db_tools import init_db, update_db, connect_db, get_db, init_md_knowledge_base, init_md_checklists, init_md_code_examples
from skf.app import app


class TestRestPlusApi(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.client = app.test_client()
        with app.app_context():
            init_db()
            update_db()
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
        self.assertEqual(response_dict['message'], "User successfully activated")


    def login(self, username, password):
        """Login method needed for testing"""
        payload = {'username': ''+username+'', 'password': ''+password+''}
        headers = {'content-type': 'application/json'}
        response = self.client.post('/api/user/login', data=json.dumps(payload), headers=headers)
        self.assertEqual(response.status_code, 200)
        response_dict = json.loads(response.data.decode('utf-8'))
        return response_dict.get('Authorization token')
        

    def test_fail_token_activate_user(self):
        """Test if the fail token activate user call is working"""
        payload = {'accessToken': 123, 'email': 'example@owasp.org', 'password': 'admin', 'repassword': 'admin', 'username': 'admin'}
        headers = {'content-type': 'application/json'}
        response = self.client.put('/api/user/activate/1', data=json.dumps(payload), headers=headers)
        self.assertEqual(response.status_code, 200)
        response_dict = json.loads(response.data.decode('utf-8'))
        self.assertEqual(response_dict['message'], "User could not be activated")


    def test_fail_email_activate_user(self):
        """Test if the fail email activate user call is working"""
        payload = {'accessToken': 1234, 'email': 'woop@owasp.org', 'password': 'admin', 'repassword': 'admin', 'username': 'admin'}
        headers = {'content-type': 'application/json'}
        response = self.client.put('/api/user/activate/1', data=json.dumps(payload), headers=headers)
        self.assertEqual(response.status_code, 200)
        response_dict = json.loads(response.data.decode('utf-8'))
        self.assertEqual(response_dict['message'], "User could not be activated")


    def test_fail_password_activate_user(self):
        """Test if the fail password activate user call is working"""
        payload = {'accessToken': 1234, 'email': 'example@owasp.org', 'password': 'admin', 'repassword': 'admintypo', 'username': 'admin'}
        headers = {'content-type': 'application/json'}
        response = self.client.put('/api/user/activate/1', data=json.dumps(payload), headers=headers)
        self.assertEqual(response.status_code, 200)
        response_dict = json.loads(response.data.decode('utf-8'))
        self.assertEqual(response_dict['message'], "User could not be activated")


    def test_login(self):
        """Test if the login call is working"""
        payload = {'username': 'admin', 'password': 'admin'}
        headers = {'content-type': 'application/json'}
        response = self.client.post('/api/user/login', data=json.dumps(payload), headers=headers)
        self.assertEqual(response.status_code, 200)
        response_dict = json.loads(response.data.decode('utf-8'))
        self.assertTrue(len(response_dict['Authorization token']) > 32)


    def test_fail_user_login(self):
        """Test if the fail user login call is working"""
        payload = {'username': 'adm', 'password': 'admin'}
        headers = {'content-type': 'application/json'}
        response = self.client.post('/api/user/login', data=json.dumps(payload), headers=headers)
        self.assertEqual(response.status_code, 200)
        response_dict = json.loads(response.data.decode('utf-8'))
        self.assertEqual(response_dict['Authorization token'], "")


    def test_fail_password_login(self):
        """Test if the fail password login call is working"""
        payload = {'username': 'admin', 'password': 'bla'}
        headers = {'content-type': 'application/json'}
        response = self.client.post('/api/user/login', data=json.dumps(payload), headers=headers)
        self.assertEqual(response.status_code, 200)
        response_dict = json.loads(response.data.decode('utf-8'))
        self.assertEqual(response_dict['Authorization token'], "")


    def test_login_create(self):
        """Test if the login create call is working"""
        jwt = self.login('admin', 'admin')
        payload = {'email': 'woop@owasp.org', 'privilege': 2}
        headers = {'content-type': 'application/json', 'Authorization': jwt}
        response = self.client.put('/api/user/create', data=json.dumps(payload), headers=headers)
        self.assertEqual(response.status_code, 200)
        response_dict = json.loads(response.data.decode('utf-8'))
        self.assertEqual(response_dict['email'], "woop@owasp.org")


    def test_login_list(self):
        """Test if the login list call is working"""
        jwt = self.login('admin', 'admin')
        headers = {'Authorization': jwt}
        response = self.client.get('/api/user/list', headers=headers)
        self.assertEqual(response.status_code, 200)
        response_dict = json.loads(response.data.decode('utf-8'))
        self.assertEqual(response_dict['items'][0]['userName'], "admin")


    def test_user_manage(self):
        """Test if the user manage call is working"""
        jwt = self.login('admin', 'admin')
        payload = {'active': 'False'}
        headers = {'content-type': 'application/json', 'Authorization': jwt}
        response = self.client.put('/api/user/manage/2', data=json.dumps(payload), headers=headers)
        self.assertEqual(response.status_code, 200)
        response_dict = json.loads(response.data.decode('utf-8'))
        self.assertEqual(response_dict['message'], "User successfully managed")


    def test_expired_login_create(self):
        """Test if the expired token login create call is working"""
        payload = {'email': 'test@owasp.org', 'privilege': 2}
        headers = {'content-type': 'application/json', 'Authorization': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJVc2VySWQiOjEsImlhdCI6MTQ5NjQxMzg1NiwicHJpdmlsZWdlIjoiZWRpdDpyZWFkOm1hbmFnZTpkZWxldGUiLCJleHAiOjE0OTY0MjEwNTZ9.FkwLGwLNqPi87JC8nl2muRB5QLNk01r4XFcaFdFHiDc'}
        response = self.client.put('/api/user/create', data=json.dumps(payload), headers=headers)
        self.assertEqual(response.status_code, 403)
        response_dict = json.loads(response.data.decode('utf-8'))
        self.assertEqual(response_dict['message'], "JWT decode error")


    def test_decode_login_create(self):
        """Test if the decode token login create call is working"""
        payload = {'email': 'test@owasp.org', 'privilege': 2}
        headers = {'content-type': 'application/json', 'Authorization': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJVc2VySWQiOjEsImlhdCI6MTQ5NjQxMzg1NiwicHJpdmlsZWdlIjoiZWRpdDpyZWFkOm1hbmFnZTpkZWxldGUiLCJleHAiOjE0OTY0MjEwNTZ9.FkwLGwLNqPi87JC8nl2muRB5QLNk01r4XFfoobar'}
        response = self.client.put('/api/user/create', data=json.dumps(payload), headers=headers)
        self.assertEqual(response.status_code, 403)
        response_dict = json.loads(response.data.decode('utf-8'))
        self.assertEqual(response_dict['message'], "JWT decode error")


    def test_fail_login_create_priv(self):
        """Test if the fail login create privilege call is working"""
        jwt = self.login('admin', 'admin')
        payload = {'email': 'test_user2@owasp.org', 'privilege': 1}
        headers = {'content-type': 'application/json', 'Authorization': jwt}
        response = self.client.put('/api/user/create', data=json.dumps(payload), headers=headers)
        self.assertEqual(response.status_code, 200)
        response_dict = json.loads(response.data.decode('utf-8'))
        self.assertEqual(response_dict['email'], None)


    def test_get_checklist(self):
        """Test if the get checklist items call is working"""
        response = self.client.get('/api/checklist/items/0')
        self.assertEqual(response.status_code, 200)
        response_dict = json.loads(response.data.decode('utf-8'))
        self.assertEqual(response_dict['items'][0]['checklist_items_checklistID'], '1.0')


    def test_get_checklist_fail(self):
        """Test if the get checklist items fail call is working"""
        response = self.client.get('/api/checklist/1337.1337,0')
        self.assertEqual(response.status_code, 400)


    def test_get_checklist_item_10(self):
        """Test if the get specific checklist item call is working"""
        response = self.client.get('/api/checklist/1.1,0')
        self.assertEqual(response.status_code, 200)
        response_dict = json.loads(response.data.decode('utf-8'))
        self.assertEqual(response_dict['checklist_items_checklistID'], '1.1')


    def test_get_checklist_items_level1(self):
        """Test if the get specific checklist item by level call is working"""
        response = self.client.get('/api/checklist/level/1')
        self.assertEqual(response.status_code, 200)
        response_dict = json.loads(response.data.decode('utf-8'))
        self.assertEqual(response_dict['items'][0]['checklist_items_content'], "Architecture, design and threat modelling")
        self.assertEqual(response_dict['items'][0]['checklist_items_level'], 0)


    def test_get_checklist_items_level2(self):
        """Test if the get specific checklist item by level 2 call is working"""
        response = self.client.get('/api/checklist/level/2')
        self.assertEqual(response.status_code, 200)
        response_dict = json.loads(response.data.decode('utf-8'))
        self.assertEqual(response_dict['items'][0]['checklist_items_content'], "Architecture, design and threat modelling")
        self.assertEqual(response_dict['items'][0]['checklist_items_level'], 0)


    def test_get_checklist_items_level3(self):
        """Test if the get specific checklist item by level 3 call is working"""
        response = self.client.get('/api/checklist/level/3')
        self.assertEqual(response.status_code, 200)
        response_dict = json.loads(response.data.decode('utf-8'))
        self.assertEqual(response_dict['items'][0]['checklist_items_content'], "Architecture, design and threat modelling")
        self.assertEqual(response_dict['items'][0]['checklist_items_level'], 0)


    def test_get_kb(self):
        """Test if the get kb items call is working"""
        response = self.client.get('/api/kb/items')
        self.assertEqual(response.status_code, 200)
        response_dict = json.loads(response.data.decode('utf-8'))
        self.assertEqual(response_dict['items'][1]['title'], "xss injection")


    def test_get_kb_item_10(self):
        """Test if the get specific kb item call is working"""
        response = self.client.get('/api/kb/10')
        self.assertEqual(response.status_code, 200)
        response_dict = json.loads(response.data.decode('utf-8'))
        self.assertEqual(response_dict['title'], "External DTD parsing")


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
        payload = {'description': 'Unit test description project', 'name': 'Unit test name project', 'level': 1, 'version': 'version 1.0'}
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
        payload = {'description': 'Unit test description project update', 'name': 'Unit test name project update', 'level': 1, 'version': 'version 1.1'}
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
        payload = {'description': 'Unit test description project', 'name': 'Unit test name project', 'level': 1, 'version': 'version 1.0'}
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
        payload = {'description': 'Unit test description project for sprint', 'name': 'Unit test name project for sprint', 'level': 1, 'version': 'version 1.0'}
        headers = {'content-type': 'application/json', 'Authorization': jwt}
        response = self.client.put('/api/project/new', data=json.dumps(payload), headers=headers)
        self.assertEqual(response.status_code, 200)
        response_dict = json.loads(response.data.decode('utf-8'))
        self.assertEqual(response_dict['message'], "Project successfully created")
        payload = {'description': 'Unit test description sprint', 'name': 'Unit test name sprint', 'projectID': 3}
        response = self.client.put('/api/sprint/new', data=json.dumps(payload), headers=headers)
        self.assertEqual(response.status_code, 200)
        payload = {'questions': [ {'projectID': 3, 'question_sprint_ID': 1,'result': 'True', 'sprintID': 4},{'projectID': 3, 'question_sprint_ID': 2,'result': 'True', 'sprintID': 4} ]}
        response = self.client.put('/api/questions_sprint/store', data=json.dumps(payload), headers=headers)
        self.assertEqual(response.status_code, 200)
        response_dict = json.loads(response.data.decode('utf-8'))
        self.assertEqual(response_dict['message'], "Sprint questions successfully created")
        payload = {'description': 'Unit test description sprint', 'name': 'Unit test name sprint', 'projectID': 3}
        response = self.client.put('/api/sprint/new', data=json.dumps(payload), headers=headers)
        self.assertEqual(response.status_code, 200)
        payload = {'questions': [ {'projectID': 3, 'question_sprint_ID': 1,'result': 'True', 'sprintID': 5},{'projectID': 3, 'question_sprint_ID': 2,'result': 'True', 'sprintID': 5} ]}
        response = self.client.put('/api/questions_sprint/store', data=json.dumps(payload), headers=headers)
        self.assertEqual(response.status_code, 200)
        response_dict = json.loads(response.data.decode('utf-8'))
        self.assertEqual(response_dict['message'], "Sprint questions successfully created")
        response = self.client.get('/api/project/stats/3', headers=headers)
        self.assertEqual(response.status_code, 200)
        response_dict = json.loads(response.data.decode('utf-8'))
        self.assertEqual(response_dict['project_open'], 109)


    def test_results_sprint(self):
        """Test if the results sprint call is working"""
        jwt = self.login('admin', 'admin')
        payload = {'description': 'Unit test description project for pre', 'name': 'Unit test name project for pre', 'level': 3, 'version': 'version 1.0'}
        headers = {'content-type': 'application/json', 'Authorization': jwt}
        response = self.client.put('/api/project/new', data=json.dumps(payload), headers=headers)
        self.assertEqual(response.status_code, 200)
        response_dict = json.loads(response.data.decode('utf-8'))
        self.assertEqual(response_dict['message'], "Project successfully created")
        payload = {'description': 'Unit test description sprint', 'name': 'Unit test name sprint', 'projectID': 3}
        response = self.client.put('/api/sprint/new', data=json.dumps(payload), headers=headers)
        self.assertEqual(response.status_code, 200)
        payload = {'questions': [ {'projectID': 3, 'question_pre_ID': 1,'result': 'True'},{'projectID': 3, 'question_pre_ID': 2,'result': 'False'}, {'projectID': 3, 'question_pre_ID': 3,'result': 'True'},{'projectID': 3, 'question_pre_ID': 4,'result': 'False'} ]}
        response = self.client.put('/api/questions_pre/store', data=json.dumps(payload), headers=headers)
        self.assertEqual(response.status_code, 200)
        response_dict = json.loads(response.data.decode('utf-8'))
        self.assertEqual(response_dict['message'], "Pre questions successfully created")
        payload = {'questions': [ {'projectID': 3, 'question_sprint_ID': 1,'result': 'True', 'sprintID': 3},{'projectID': 3, 'question_sprint_ID': 2,'result': 'True', 'sprintID': 3} ]}
        response = self.client.put('/api/questions_sprint/store', data=json.dumps(payload), headers=headers)
        self.assertEqual(response.status_code, 200)
        response_dict = json.loads(response.data.decode('utf-8'))
        self.assertEqual(response_dict['message'], "Sprint questions successfully created")
        response = self.client.get('/api/sprint/results/3', headers=headers)
        self.assertEqual(response.status_code, 200)
        response_dict = json.loads(response.data.decode('utf-8'))
        payload = {'checklistID': '1.1', 'comment': 'Unit test comment', 'sprintID': 7, 'status': 3}
        response = self.client.put('/api/comment/new', data=json.dumps(payload), headers=headers)
        self.assertEqual(response.status_code, 200)
        response_dict = json.loads(response.data.decode('utf-8'))
        self.assertEqual(response_dict['message'], "Comment item successfully created")
        response = self.client.get('/api/sprint/results/audit/3', headers=headers)
        self.assertEqual(response.status_code, 200)
        response_dict = json.loads(response.data.decode('utf-8'))
        #self.assertEqual(response_dict['items'][0]['projectID'], 3)


    def test_create_sprint(self):
        """Test if the create new sprint call is working"""
        jwt = self.login('admin', 'admin')        
        payload = {'description': 'Unit test description sprint', 'name': 'Unit test name sprint', 'projectID': 1}
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
        payload = {'description': 'Unit test description sprint', 'name': 'Unit test name sprint', 'projectID': 2}
        response = self.client.put('/api/sprint/new', data=json.dumps(payload), headers=headers)
        self.assertEqual(response.status_code, 200)
        response_dict = json.loads(response.data.decode('utf-8'))
        self.assertEqual(response_dict['message'], "Sprint successfully created")
        response = self.client.get('/api/sprint/3', headers=headers)
        self.assertEqual(response.status_code, 200)
        response_dict = json.loads(response.data.decode('utf-8'))
        self.assertEqual(response_dict['sprintName'], "Unit test name sprint")


    def test_update_sprint_item(self):
        """Test if the sprint update call is working"""
        jwt = self.login('admin', 'admin') 
        payload = {'description': 'Unit test description sprint update', 'name': 'Unit test name sprint update', 'projectID': 7}
        headers = {'content-type': 'application/json', 'Authorization': jwt}
        response = self.client.put('/api/sprint/update/3', data=json.dumps(payload), headers=headers)
        self.assertEqual(response.status_code, 200)
        response_dict = json.loads(response.data.decode('utf-8'))
        self.assertEqual(response_dict['message'], "Sprint successfully updated")
        response = self.client.get('/api/sprint/3', headers=headers)
        self.assertEqual(response.status_code, 200)
        response_dict = json.loads(response.data.decode('utf-8'))
        self.assertEqual(response_dict['sprintName'], "Unit test name sprint update")


    def test_delete_sprint_item(self):
        """Test if the delete project item call is working"""
        jwt = self.login('admin', 'admin') 
        payload = {'description': 'Unit test description sprint', 'name': 'Unit test name sprint', 'projectID': 2}
        headers = {'content-type': 'application/json', 'Authorization': jwt}
        response = self.client.put('/api/sprint/new', data=json.dumps(payload), headers=headers)
        response_dict = json.loads(response.data.decode('utf-8'))
        self.assertEqual(response_dict['message'], "Sprint successfully created")
        response = self.client.delete('/api/sprint/delete/2', headers=headers)
        self.assertEqual(response.status_code, 200)
        response_dict = json.loads(response.data.decode('utf-8'))
        self.assertEqual(response_dict['message'], "Sprint successfully deleted")


    def test_stats_sprint_items(self):
        """Test if the stats of sprint call is working"""
        jwt = self.login('admin', 'admin') 
        payload = {'description': 'Unit test description project for sprint', 'name': 'Unit test name project for sprint', 'level': 1, 'version': 'version 1.0'}
        headers = {'content-type': 'application/json', 'Authorization': jwt}
        response = self.client.put('/api/project/new', data=json.dumps(payload), headers=headers)
        self.assertEqual(response.status_code, 200)
        response_dict = json.loads(response.data.decode('utf-8'))
        self.assertEqual(response_dict['message'], "Project successfully created")
        payload = {'description': 'Unit test description sprint', 'name': 'Unit test name sprint', 'projectID': 5}
        response = self.client.put('/api/sprint/new', data=json.dumps(payload), headers=headers)
        self.assertEqual(response.status_code, 200)
        response_dict = json.loads(response.data.decode('utf-8'))
        payload = {'questions': [ {'projectID': 5, 'question_sprint_ID': 1,'result': 'False', 'sprintID': 7},{'projectID': 5, 'question_sprint_ID': 2,'result': 'True', 'sprintID': 7} ]}
        response = self.client.put('/api/questions_sprint/store', data=json.dumps(payload), headers=headers)
        self.assertEqual(response.status_code, 200)
        response_dict = json.loads(response.data.decode('utf-8'))
        self.assertEqual(response_dict['message'], "Sprint questions successfully created")
        response = self.client.get('/api/sprint/stats/5', headers=headers)
        self.assertEqual(response.status_code, 200)
        response_dict = json.loads(response.data.decode('utf-8'))
        self.assertEqual(response_dict[0]['sprint_open'], 7)


    def test_delete_project_item_fail(self):
        """Test if the delete project item fail call is working"""
        jwt = self.login('admin', 'admin') 
        headers = {'content-type': 'application/json', 'Authorization': jwt}
        response = self.client.delete('/api/project/delete/1', headers=headers)
        self.assertEqual(response.status_code, 400)


    def test_auth_protected_call(self):
        """Test if the delete project item fail call is working"""
        payload = {'description': 'Unit test description project', 'name': 'Unit test name project', 'level': 1, 'version': 'version 1.0'}
        headers = {'content-type': 'application/json', 'Authorization': 'woopwoopwrong'}
        response = self.client.put('/api/project/new', data=json.dumps(payload), headers=headers)
        self.assertEqual(response.status_code, 403)
    

    def test_get_code(self):
        """Test if the get code items call is working"""
        response = self.client.get('/api/code/items')
        self.assertEqual(response.status_code, 200)
        response_dict = json.loads(response.data.decode('utf-8'))
        self.assertNotEqual(response_dict['items'][0]['title'], "")


    def test_get_code_item_10(self):
        """Test if the get specific code item call is working"""
        response = self.client.get('/api/code/10')
        self.assertEqual(response.status_code, 200)
        response_dict = json.loads(response.data.decode('utf-8'))
        self.assertNotEqual(response_dict['title'], "")


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
        response = self.client.get('/api/code/lang/php')
        self.assertEqual(response.status_code, 200)
        response_dict = json.loads(response.data.decode('utf-8'))
        self.assertNotEqual(response_dict['items'][0]['title'], "")


    def test_get_code_item_lang_asp(self):
        """Test if the asp language code items call is working"""
        response = self.client.get('/api/code/lang/asp')
        self.assertEqual(response.status_code, 200)
        response_dict = json.loads(response.data.decode('utf-8'))
        self.assertNotEqual(response_dict['items'][0]['title'], "")


    def test_get_code_item_lang_java(self):
        """Test if the java language code items call is working"""
        response = self.client.get('/api/code/lang/java')
        self.assertEqual(response.status_code, 200)
        response_dict = json.loads(response.data.decode('utf-8'))
        self.assertNotEqual(response_dict['items'][0]['title'], "")


    def test_get_code_item_lang_go(self):
        """Test if the go language code items call is working"""
        response = self.client.get('/api/code/lang/go')
        self.assertEqual(response.status_code, 200)
        response_dict = json.loads(response.data.decode('utf-8'))
        self.assertEqual(len(response_dict['items']), 5)


    def test_get_questions_sprint_items(self):
        """Test if the questions sprint items call is working"""
        headers = {'content-type': 'application/json'}
        response = self.client.get('/api/questions_sprint/items', headers=headers)
        self.assertEqual(response.status_code, 200)
        response_dict = json.loads(response.data.decode('utf-8'))
        self.assertEqual(response_dict['items'][0]['question'], "Does the sprint implement/changes authentication?")


    def test_store_questions_sprint_items(self):
        """Test if the question sprint items call is working"""
        jwt = self.login('admin', 'admin') 
        payload = {'description': 'Unit test description project for sprint', 'name': 'Unit test name project for sprint', 'level': 2, 'version': 'version 1.0'}
        headers = {'content-type': 'application/json', 'Authorization': jwt}
        response = self.client.put('/api/project/new', data=json.dumps(payload), headers=headers)
        self.assertEqual(response.status_code, 200)
        response_dict = json.loads(response.data.decode('utf-8'))
        self.assertEqual(response_dict['message'], "Project successfully created")
        payload = {'questions': [ {'projectID': 3, 'question_sprint_ID': 1,'result': 'True', 'sprintID': 1},{'projectID': 3, 'question_sprint_ID': 2,'result': 'True', 'sprintID': 1} ]}
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
        self.assertEqual(response_dict['items'][0]['question'], "You have a blueprint for the design, architecture and validated this using ASVS?")


    def test_store_questions_pre_items(self):
        """Test if the store question pre items call is working"""
        jwt = self.login('admin', 'admin') 
        payload = {'description': 'Unit test description project for pre', 'name': 'Unit test name project for pre', 'level': 1, 'version': 'version 1.0'}
        headers = {'content-type': 'application/json', 'Authorization': jwt}
        response = self.client.put('/api/project/new', data=json.dumps(payload), headers=headers)
        self.assertEqual(response.status_code, 200)
        response_dict = json.loads(response.data.decode('utf-8'))
        self.assertEqual(response_dict['message'], "Project successfully created")
        payload = {'description': 'Unit test description sprint', 'name': 'Unit test name sprint', 'projectID': 6}
        response = self.client.put('/api/sprint/new', data=json.dumps(payload), headers=headers)
        self.assertEqual(response.status_code, 200)
        payload = {'questions': [ {'projectID': 6, 'question_pre_ID': 1,'result': 'True'},{'projectID': 6, 'question_pre_ID': 2,'result': 'False'} ]}
        response = self.client.put('/api/questions_pre/store', data=json.dumps(payload), headers=headers)
        self.assertEqual(response.status_code, 200)
        response_dict = json.loads(response.data.decode('utf-8'))
        self.assertEqual(response_dict['message'], "Pre questions successfully created")


    def test_update_questions_pre_items(self):
        """Test if the update question pre items call is working"""
        jwt = self.login('admin', 'admin') 
        payload = {'description': 'Unit test description project for pre', 'name': 'Unit test name project for pre', 'level': 3, 'version': 'version 1.0'}
        headers = {'content-type': 'application/json', 'Authorization': jwt}
        response = self.client.put('/api/project/new', data=json.dumps(payload), headers=headers)
        self.assertEqual(response.status_code, 200)
        response_dict = json.loads(response.data.decode('utf-8'))
        self.assertEqual(response_dict['message'], "Project successfully created")
        payload = {'description': 'Unit test description sprint', 'name': 'Unit test name sprint', 'projectID': 7}
        response = self.client.put('/api/sprint/new', data=json.dumps(payload), headers=headers)
        self.assertEqual(response.status_code, 200)
        payload = {'questions': [ {'projectID': 7, 'question_pre_ID': 1,'result': 'True'},{'projectID': 7, 'question_pre_ID': 2, 'result': 'False', 'question_pre_ID': 3, 'result': 'True', 'question_pre_ID': 4, 'result': 'False'} ]}
        response = self.client.put('/api/questions_pre/store', data=json.dumps(payload), headers=headers)
        self.assertEqual(response.status_code, 200)
        response_dict = json.loads(response.data.decode('utf-8'))
        self.assertEqual(response_dict['message'], "Pre questions successfully created")
        payload = {'questions': [ {'question_pre_ID': 1,'result': 'True'},{'question_pre_ID': 2,'result': 'False'} ]}
        response = self.client.put('/api/questions_pre/update/7', data=json.dumps(payload), headers=headers)
        self.assertEqual(response.status_code, 200)
        response_dict = json.loads(response.data.decode('utf-8'))
        self.assertEqual(response_dict['message'], "Pre questions successfully updated")


    def test_create_comment_item(self):
        """Test if the create comment item call is working"""
        jwt = self.login('admin', 'admin') 
        payload = {'checklistID': '1.1', 'comment': 'Unit test comment', 'sprintID': 7, 'status': 2}
        headers = {'content-type': 'application/json', 'Authorization': jwt}
        response = self.client.put('/api/comment/new', data=json.dumps(payload), headers=headers)
        self.assertEqual(response.status_code, 200)
        response_dict = json.loads(response.data.decode('utf-8'))
        self.assertEqual(response_dict['message'], "Comment item successfully created")


    def test_create_post_checklist(self):
        """Test if the create post checklist call is working"""
        jwt = self.login('admin', 'admin') 
        payload = {'questions': [ {'checklistID': '8.4', 'projectID': 1, 'sprintID': 1, 'kbID': 105, 'status': 1}, {'checklistID': '8.5', 'projectID': 1, 'sprintID': 1, 'kbID': 103, 'status': 2}, {'checklistID': '8.6', 'projectID': 1, 'sprintID': 1, 'kbID': 101, 'status': 1} ]}
        headers = {'content-type': 'application/json', 'Authorization': jwt}
        response = self.client.put('/api/questions_post/store', data=json.dumps(payload), headers=headers)
        self.assertEqual(response.status_code, 200)
        response_dict = json.loads(response.data.decode('utf-8'))
        self.assertEqual(response_dict['message'], "Post questions successfully stored")


    def test_get_post_checklist(self):
        """Test if the post checklist call is working"""
        jwt = self.login('admin', 'admin') 
        headers = {'content-type': 'application/json', 'Authorization': jwt}
        response = self.client.get('/api/questions_post/1', headers=headers)
        self.assertEqual(response.status_code, 200)
        response_dict = json.loads(response.data.decode('utf-8'))
        self.assertEqual(response_dict['items'][0]['kb_item_title'], "Malicious intent")


    def test_get_comment_item(self):
        """Test if the get comment items call is working"""
        jwt = self.login('admin', 'admin') 
        payload = {'checklistID': '1.1', 'sprintID': 7}
        headers = {'content-type': 'application/json', 'Authorization': jwt}
        response = self.client.post('/api/comment/items', data=json.dumps(payload), headers=headers)
        self.assertEqual(response.status_code, 200)
        response_dict = json.loads(response.data.decode('utf-8'))
        self.assertEqual(response_dict['items'][0]['comment'], "Unit test comment")


    def test_get_description_item(self):
        """Test if the description call is working"""
        payload = {"question": "waht is xss?", "question_option": 0, "question_lang": "string"}
        headers = {'content-type': 'application/json', 'Accept':'application/json'}
        response = self.client.post('/api/chatbot/question', data=json.dumps(payload), headers=headers)
        self.assertEqual(response.status_code, 200)
        response_dict = json.loads(response.data.decode('utf-8'))
        self.assertEqual(response_dict['options'][0]['answer'], "Description for xss injection is : Every time the application gets userinput, whether this showing it on screen or processingthis data in the application background, these parameters should be escaped for maliciouscode in order to prevent crosssite scripting injections.When an attacker gains the possibility to perform an XSS injection,he is given the opportunity to inject HTML and JavaScript code directly into theapplication. This could lead to accounts being compromised by stealing session cookies or directly affect the operation of the target application.")

    def test_get_solution_item(self):
        """Test if the solution call is working"""
        payload = {"question": "how to resolve xss?", "question_option": 0, "question_lang": "string"}
        headers = {'content-type': 'application/json', 'Accept':'application/json'}
        response = self.client.post('/api/chatbot/question', data=json.dumps(payload), headers=headers)
        self.assertEqual(response.status_code, 200)
        response_dict = json.loads(response.data.decode('utf-8'))
        self.assertEqual(response_dict['options'][0]['answer'], "Solution for xss injection is : In order to prevent XSS injections, all userinput should be escaped or encoded.You could start by sanitizing userinput as soon as it is inserted into the application,by preference using a so called whitelisting method.This means you should not check for malicious content like the tags or anything,but only allow the expected input. Every input which is outside of the intended operationof the application should immediately be detected and login rejected.Do not try to help use the input in any way because that could introduce a new type of attack by converting characters. The second step would be encoding all the parameters or userinput before putting this inyour html with encoding libraries specially designed for this purpose.You should take into consideration that there are several contexts for encoding userinput forescaping XSS injections. These contexts are amongst others:HTML encoding is for whenever your userinput is displayed directly into your HTML.HTML attribute encoding is the type of encoding/escaping that should be applied whenever your user input is displayed into the attribute of your HTML tags.HTML URL encoding ;This type of encoding/escaping should be applied to whenever you are using userinput into a HREF tag.JavaScript encoding should be used whenever parameters are rendered via JavaScript; your application will detect normal injections in the first instant. But your application still remains vulnerable to JavaScript encoding which will not be detected by the normal encoding/escaping methods.")


    def test_code_item_list(self):
        """Test if the code item is working"""
        payload = {"question": "code for xss filtering?", "question_option": 0, "question_lang": "string"}
        headers = {'content-type': 'application/json', 'Accept':'application/json'}
        response = self.client.post('/api/chatbot/question', data=json.dumps(payload), headers=headers)
        self.assertEqual(response.status_code, 200)
        response_dict = json.loads(response.data.decode('utf-8'))
        self.assertEqual(response_dict['options'][0]['answer'], "Code xss filtering in java")

    def test_no_match(self):
        """Test if the options are working"""
        payload = {"question": "what is bla?", "question_option": 0, "question_lang": "string"}
        headers = {'content-type': 'application/json', 'Accept':'application/json'}
        response = self.client.post('/api/chatbot/question', data=json.dumps(payload), headers=headers)
        self.assertEqual(response.status_code, 200)
        response_dict = json.loads(response.data.decode('utf-8'))
        self.assertEqual(response_dict['options'][0]['answer'], "Please be more specific")

    def test_get_entity2_item(self):
        """Test if the options are working"""
        payload = {"question": "what is the risk of hsts?", "question_option": 0, "question_lang": "string"}
        headers = {'content-type': 'application/json', 'Accept':'application/json'}
        response = self.client.post('/api/chatbot/question', data=json.dumps(payload), headers=headers)
        self.assertEqual(response.status_code, 200)
        response_dict = json.loads(response.data.decode('utf-8'))
        try:
            self.assertEqual(response_dict['options'][0]['answer'], "Description the possible risks to the application must be documented")
        except BadRequest:
            return True    


    def test_code_lang_item(self):
        """Test if the options are working"""
        payload = {"question": "code example for code encoder", "question_option": 0, "question_lang": "string"}
        headers = {'content-type': 'application/json', 'Accept':'application/json'}
        response = self.client.post('/api/chatbot/question', data=json.dumps(payload), headers=headers)
        self.assertEqual(response.status_code, 200)
        response_dict = json.loads(response.data.decode('utf-8'))
        try:
            self.assertEqual(response_dict['options'][0]['answer'], "Code encoder in php")
        except BadRequest:
            return True    
        
    
    def test_code_classify_item(self):
        """Test if the code classify is working"""
        payload = {"question": "code example for xss filtering in java", "question_option": 0, "question_lang": "string"}
        headers = {'content-type': 'application/json', 'Accept':'application/json'}
        response = self.client.post('/api/chatbot/question', data=json.dumps(payload), headers=headers)
        self.assertEqual(response.status_code, 200)
        response_dict = json.loads(response.data.decode('utf-8'))
        self.assertEqual(response_dict['options'][0]['answer'], "Code for  XSS filtering\n\n\n Example:\n\n\n\t\tpackage com.edw;\n\n\t\timport org.owasp.esapi.ESAPI;\n\t\timport org.jsoup.Jsoup;\n\t\timport org.jsoup.safety.Whitelist;\n\n\t\tpublic final class XssFilter {\n\n\t\t\t/**\n\t\t\t* Strips any potential XSS threats out of the value\n\t\t\t* @param value\n\t\t\t* @return\n\t\t\t*/\n\t\t\tpublic String filter( String value ) {\n\t\t\t    if( value == null )\n\t\t\t\t\t\t\treturn null;\n\t\t\t\n\t\t\t\t// Use the ESAPI library to avoid encoded attacks.\n\t\t\t\tvalue = ESAPI.encoder().canonicalize( value );\n\t\t\t\n\t\t\t\t// Avoid null characters\n\t\t\t\tvalue = value.replaceAll(\"\\0\", \"\");\n\t\t\t\n\t\t\t\t// Clean out HTML\n\t\t\t\tvalue = Jsoup.clean( value, Whitelist.none() );\n\t\t\t\n\t\t\t\treturn value;\n\t\t\t}\t\n\t\t}\n\n\n Code language is java")


    def test_assert_403_project_get(self):
        headers = {'content-type': 'application/json'}
        response = self.client.get('/api/project/1')
        self.assertEqual(response.status_code, 403)


    def test_assert_403_project_new(self):
        payload = {'description': 'Unit test description project', 'name': 'Unit test name project', 'level': 1, 'version': 'version 1.0'}
        headers = {'content-type': 'application/json'}
        response = self.client.put('/api/project/new', data=json.dumps(payload), headers=headers)
        self.assertEqual(response.status_code, 403)


    def test_assert_403_project_update(self):
        payload = {'description': 'Unit test description project update', 'name': 'Unit test name project update', 'level': 1, 'version': 'version 1.1'}
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


    def test_assert_400_user_create(self):
        """Test if the login fail create call is working"""
        jwt = self.login('admin', 'admin')
        payload = {'email': 'test_user@owasp.org', 'privilege': 2}
        headers = {'content-type': 'application/json', 'Authorization': jwt}
        response = self.client.put('/api/user/create', data=json.dumps(payload), headers=headers)
        self.assertEqual(response.status_code, 200)
        response_dict = json.loads(response.data.decode('utf-8'))
        self.assertEqual(response_dict['email'], "test_user@owasp.org")
        response = self.client.put('/api/user/create', data=json.dumps(payload), headers=headers)
        self.assertEqual(response.status_code, 400)
        response_dict = json.loads(response.data.decode('utf-8'))
        self.assertEqual(response_dict['message'], "A database result was required but none was found.")



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
        try:
            self.assertFalse(val_alpha("woop %$*@><'1337"))
            self.assertFalse(val_alpha("woop woop 1337"))
        except BadRequest:
            return True


    def test_val_num(self):
        """Test if the val_num method is working"""
        self.assertTrue(val_num(1337))
        try:
            self.assertFalse(val_num("woopwoop"))        
            self.assertFalse(val_num("woop woop 1337"))
            self.assertFalse(val_num("woop %$*@><'1337"))
        except BadRequest:
            return True


    def test_val_alpha_num(self):
        """Test if the val_alpha_num method is working"""
        self.assertTrue(val_alpha_num("woop woop 1337"))
        try:
            self.assertFalse(val_alpha_num("woop %$*@><'1337"))
        except BadRequest:
            return True


    def test_val_float(self):
        """Test if the val_float method is working"""
        self.assertTrue(val_float(10.11))
        try:
            self.assertFalse(val_float(1337))
            self.assertFalse(val_float("woop woop 1337"))
            self.assertFalse(val_float("woop %$*@><'1337"))
        except BadRequest:
            return True


    def test_security_headers(self):
        """Test if the security_headers method is working"""
        result_headers = security_headers()
        self.assertEqual(result_headers['X-Frame-Options'], "deny")
        self.assertEqual(result_headers['X-XSS-Protection'], "1")
        self.assertEqual(result_headers['X-Content-Type-Options'], "nosniff")
        self.assertEqual(result_headers['Cache-Control'], "no-store, no-cache")


if __name__ == '__main__':
    unittest.main()
