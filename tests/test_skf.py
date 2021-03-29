import os, json, unittest, tempfile, skf
from werkzeug.exceptions import BadRequest
from skf import settings
from skf.api.security import log, val_num, val_float, val_alpha, val_alpha_num, security_headers
from skf.db_tools import clear_db, clean_db, update_db, init_md_knowledge_base, init_md_code_examples
from skf import chatbot_tools
from skf.app import app
from skf.api.change_password import ChangePassword, ChangePasswordForm

import pytest

class TestRestPlusApi(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.client = app.test_client()
        with app.app_context():
            clean_db()
            update_db()
            #chatbot_tools.init_dataset()
            settings.TESTING = True
        app.app_context().push()

    #@classmethod
    #def tearDownClass(cls):
    #        cls.client = app.test_client()
    #        with app.app_context():
    #            clear_db()
 
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
        self.assertEqual(response.status_code, 400)
        response_dict = json.loads(response.data.decode('utf-8'))
        self.assertEqual(response_dict['message'], "User could not be activated")


    def test_fail_email_activate_user(self):
        """Test if the fail email activate user call is working"""
        payload = {'accessToken': 1234, 'email': 'woop@owasp.org', 'password': 'admin', 'repassword': 'admin', 'username': 'admin'}
        headers = {'content-type': 'application/json'}
        response = self.client.put('/api/user/activate/1', data=json.dumps(payload), headers=headers)
        self.assertEqual(response.status_code, 400)
        response_dict = json.loads(response.data.decode('utf-8'))
        self.assertEqual(response_dict['message'], "User could not be activated")


    def test_fail_password_activate_user(self):
        """Test if the fail password activate user call is working"""
        payload = {'accessToken': 1234, 'email': 'example@owasp.org', 'password': 'admin', 'repassword': 'admintypo', 'username': 'admin'}
        headers = {'content-type': 'application/json'}
        response = self.client.put('/api/user/activate/1', data=json.dumps(payload), headers=headers)
        self.assertEqual(response.status_code, 400)
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
        self.assertEqual(response.status_code, 400)
        response_dict = json.loads(response.data.decode('utf-8'))
        self.assertEqual(response_dict['message'], "Login was failed")


    def test_fail_password_login(self):
        """Test if the fail password login call is working"""
        payload = {'username': 'admin', 'password': 'bla'}
        headers = {'content-type': 'application/json'}
        response = self.client.post('/api/user/login', data=json.dumps(payload), headers=headers)
        self.assertEqual(response.status_code, 400)
        response_dict = json.loads(response.data.decode('utf-8'))
        self.assertEqual(response_dict['message'], "Login was failed")


    def test_login_create(self):
        """Test if the login create call is working"""
        jwt = self.login('admin', 'admin')
        payload = {'email': 'woop@owasp.org', 'privilege_id': 2}
        headers = {'content-type': 'application/json', 'Authorization': jwt}
        response = self.client.put('/api/user/create', data=json.dumps(payload), headers=headers)
        self.assertEqual(response.status_code, 200)
        response_dict = json.loads(response.data.decode('utf-8'))
        self.assertEqual(response_dict['email'], "woop@owasp.org")


    def test_login_list(self):
        """Test if the login list call is working"""
        jwt = self.login('admin', 'admin')
        headers = {'content-type': 'application/json', 'Authorization': jwt}
        response = self.client.get('/api/user/list', headers=headers)
        self.assertEqual(response.status_code, 200)
        response_dict = json.loads(response.data.decode('utf-8'))
        self.assertEqual(response_dict['items'][0]['username'], "admin")


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
        payload = {'email': 'test@owasp.org', 'privilege_id': 2}
        headers = {'content-type': 'application/json', 'Authorization': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJVc2VySWQiOjEsImlhdCI6MTQ5NjQxMzg1NiwicHJpdmlsZWdlIjoiZWRpdDpyZWFkOm1hbmFnZTpkZWxldGUiLCJleHAiOjE0OTY0MjEwNTZ9.FkwLGwLNqPi87JC8nl2muRB5QLNk01r4XFcaFdFHiDc'}
        response = self.client.put('/api/user/create', data=json.dumps(payload), headers=headers)
        self.assertEqual(response.status_code, 403)
        response_dict = json.loads(response.data.decode('utf-8'))
        self.assertEqual(response_dict['message'], "JWT decode error")


    def test_decode_login_create(self):
        """Test if the decode token login create call is working"""
        payload = {'email': 'test@owasp.org', 'privilege_id': 2}
        headers = {'content-type': 'application/json', 'Authorization': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJVc2VySWQiOjEsImlhdCI6MTQ5NjQxMzg1NiwicHJpdmlsZWdlIjoiZWRpdDpyZWFkOm1hbmFnZTpkZWxldGUiLCJleHAiOjE0OTY0MjEwNTZ9.FkwLGwLNqPi87JC8nl2muRB5QLNk01r4XFfoobar'}
        response = self.client.put('/api/user/create', data=json.dumps(payload), headers=headers)
        self.assertEqual(response.status_code, 403)
        response_dict = json.loads(response.data.decode('utf-8'))
        self.assertEqual(response_dict['message'], "JWT decode error")


    def test_login_create_priv(self):
        """Test if the login create privilege_id call is working"""
        jwt = self.login('admin', 'admin')
        payload = {'email': 'test_user2@owasp.org', 'privilege_id': 1}
        headers = {'content-type': 'application/json', 'Authorization': jwt}
        response = self.client.put('/api/user/create', data=json.dumps(payload), headers=headers)
        self.assertEqual(response.status_code, 200)
        response_dict = json.loads(response.data.decode('utf-8'))
        self.assertEqual(response_dict['email'], "test_user2@owasp.org")


    def test_get_checklist(self):
        """Test if the get checklist items call is working"""
        response = self.client.get('/api/checklist/items/1')
        self.assertEqual(response.status_code, 200)
        response_dict = json.loads(response.data.decode('utf-8'))
        self.assertEqual(response_dict['items'][0]['checklist_items_checklist_id'], '1.0')


    def test_update_checklist_item_15(self):
        """Test if the update specific checklist item call is working"""
        jwt = self.login('admin', 'admin') 
        headers = {'content-type': 'application/json', 'Authorization': jwt}
        payload = {"content": "This is a updated checklist item", "kb_id": 319, "checklist_id": "1.9.1", "maturity": 2, "include_always": "False", "question_id": 8, "add_resources": "http://google.com" }
        response = self.client.put('/api/checklist/update/item/19', data=json.dumps(payload), headers=headers)
        self.assertEqual(response.status_code, 200)
        response_dict = json.loads(response.data.decode('utf-8'))
        self.assertEqual(response_dict['message'], "Checklist item successfully updated")


    def test_get_checklist_types(self):
        """Test if the get all checklist types call is working"""
        jwt = self.login('admin', 'admin') 
        headers = {'content-type': 'application/json', 'Authorization': jwt}
        response = self.client.get('/api/checklist_types/types/1', headers=headers)
        self.assertEqual(response.status_code, 200)
        response_dict = json.loads(response.data.decode('utf-8'))
        self.assertEqual(response_dict['items'][0]['title'], 'Architecture, Design and Threat Modeling Requirements')


    def test_new_checklist_cat(self):
        """Test if the create new checklist category call is working"""
        jwt = self.login('admin', 'admin') 
        headers = {'content-type': 'application/json', 'Authorization': jwt}
        payload = {"description": "This is a checklist cat description", "name": "Custom security category"}
        response = self.client.put('/api/checklist_category/new', data=json.dumps(payload), headers=headers)
        self.assertEqual(response.status_code, 200)
        response_dict = json.loads(response.data.decode('utf-8'))
        self.assertEqual(response_dict['message'], "Checklist category successfully created")


    def test_update_checklist_cat(self):
        """Test if the update checklist type call is working"""
        jwt = self.login('admin', 'admin') 
        headers = {'content-type': 'application/json', 'Authorization': jwt}
        payload = {"name": "Custom security category update", "description": "This is a checklist category description update"}
        response = self.client.put('/api/checklist_category/update/1', data=json.dumps(payload), headers=headers)
        self.assertEqual(response.status_code, 200)
        response_dict = json.loads(response.data.decode('utf-8'))
        self.assertEqual(response_dict['message'], "Checklist category successfully updated")


    def test_delete_checklist_cat(self):
        """Test if the delete checklist category call is working"""
        jwt = self.login('admin', 'admin') 
        headers = {'content-type': 'application/json', 'Authorization': jwt}
        response = self.client.delete('/api/checklist_category/delete/2', headers=headers)
        self.assertEqual(response.status_code, 200)
        response_dict = json.loads(response.data.decode('utf-8'))
        self.assertEqual(response_dict['message'], "Checklist category successfully deleted")


    def test_get_checklist_cat(self):
        """Test if the get all checklist category call is working"""
        jwt = self.login('admin', 'admin') 
        headers = {'content-type': 'application/json', 'Authorization': jwt}
        response = self.client.get('/api/checklist_category/items', headers=headers)
        self.assertEqual(response.status_code, 200)
        response_dict = json.loads(response.data.decode('utf-8'))
        self.assertEqual(response_dict['items'][0]['name'], 'Web applications')


    def test_get_checklist_cat_item(self):
        """Test if the get item checklist category call is working"""
        jwt = self.login('admin', 'admin') 
        headers = {'content-type': 'application/json', 'Authorization': jwt}
        response = self.client.get('/api/checklist_category/1', headers=headers)
        self.assertEqual(response.status_code, 200)
        response_dict = json.loads(response.data.decode('utf-8'))
        self.assertEqual(response_dict['name'], 'Web applications')


    def test_new_checklist_type(self):
        """Test if the create new checklist type call is working"""
        jwt = self.login('admin', 'admin') 
        headers = {'content-type': 'application/json', 'Authorization': jwt}
        payload = {"description": "This is a checklist type description", "name": "Custom security list", "visibility": 1}
        response = self.client.put('/api/checklist_category/new', data=json.dumps(payload), headers=headers)
        self.assertEqual(response.status_code, 200)
        response_dict = json.loads(response.data.decode('utf-8'))
        self.assertEqual(response_dict['message'], "Checklist category successfully created")


    def test_update_checklist_type(self):
        """Test if the update checklist type call is working"""
        jwt = self.login('admin', 'admin') 
        headers = {'content-type': 'application/json', 'Authorization': jwt}
        payload = {"description": "This is a checklist type description update", "name": "Custom security list new", "visibility": 1}
        response = self.client.put('/api/checklist_types/update/1', data=json.dumps(payload), headers=headers)
        self.assertEqual(response.status_code, 200)
        response_dict = json.loads(response.data.decode('utf-8'))
        self.assertEqual(response_dict['message'], "Checklist item successfully updated")


    def test_delete_checklist_type(self):
        """Test if the delete checklist type call is working"""
        jwt = self.login('admin', 'admin') 
        headers = {'content-type': 'application/json', 'Authorization': jwt}
        response = self.client.delete('/api/checklist_types/delete/20', headers=headers)
        self.assertEqual(response.status_code, 200)
        response_dict = json.loads(response.data.decode('utf-8'))
        self.assertEqual(response_dict['message'], "Checklist type successfully deleted")


    def test_new_checklist_item(self):
        """Test if the create new checklist item call is working"""
        jwt = self.login('admin', 'admin') 
        headers = {'content-type': 'application/json', 'Authorization': jwt}
        payload = {"content": "This is a new checklist item", "maturity": 1, "kb_id": 12, "include_always": "False", "question_id": 0, "checklist_id": "14.5.41", "add_resources": "http://test.com" }
        response = self.client.put('/api/checklist/new/item/type/13', data=json.dumps(payload), headers=headers)
        self.assertEqual(response.status_code, 200)
        response_dict = json.loads(response.data.decode('utf-8'))
        self.assertEqual(response_dict['message'], "Checklist item successfully created")


    def test_delete_checklist_item(self):
        """Test if the delete a checklist item call is working"""
        jwt = self.login('admin', 'admin') 
        headers = {'content-type': 'application/json', 'Authorization': jwt}
        response = self.client.delete('/api/checklist/delete/item/31', headers=headers)
        self.assertEqual(response.status_code, 200)
        response_dict = json.loads(response.data.decode('utf-8'))
        self.assertEqual(response_dict['message'], "Checklist item successfully deleted")


    def test_get_checklist_question_sprint_3(self):
        """Test if the get specific checklist item correlated to question sprint call is working"""
        jwt = self.login('admin', 'admin') 
        headers = {'content-type': 'application/json', 'Authorization': jwt}
        response = self.client.get('/api/checklist/item/question_sprint/1', headers=headers)
        self.assertEqual(response.status_code, 200)
        response_dict = json.loads(response.data.decode('utf-8'))
        self.assertEqual(response_dict['items'][0]['kb_item_id'], '272')


    def test_get_checklist_item_10(self):
        """Test if the get specific checklist item call is working"""
        response = self.client.get('/api/checklist/item/1')
        self.assertEqual(response.status_code, 200)
        response_dict = json.loads(response.data.decode('utf-8'))
        self.assertEqual(response_dict['checklist_id'], '1.0')


    def test_get_checklist_items_level1(self):
        """Test if the get specific ASVS checklist item by level call is working"""
        response = self.client.get('/api/checklist/items/1')
        self.assertEqual(response.status_code, 200)
        response_dict = json.loads(response.data.decode('utf-8'))
        self.assertEqual(response_dict['items'][0]['checklist_items_content'][0:30], 'Architecture, Design and Threa')


    def test_get_checklist_items_level2(self):
        """Test if the get specific ASVS checklist item by level 2 call is working"""
        response = self.client.get('/api/checklist/items/2')
        self.assertEqual(response.status_code, 200)
        response_dict = json.loads(response.data.decode('utf-8'))
        self.assertEqual(response_dict['items'][0]['checklist_items_content'][0:30], 'Authentication Verification Re')


    def test_get_labs(self):
        """Test if the get labs items call is working"""
        response = self.client.get('/api/interactive_labs/items')
        self.assertEqual(response.status_code, 200)
        response_dict = json.loads(response.data.decode('utf-8'))
        self.assertEqual(response_dict['items'][0]['title'], "Path traversal (LFI)")


    def test_get_labs_code_solutions(self):
        """Test if the get labs code solution items call is working"""
        response = self.client.get('/api/interactive_labs/code/items/solutions/1')
        self.assertEqual(response.status_code, 200)
        response_dict = json.loads(response.data.decode('utf-8'))
        self.assertEqual(response_dict['items'][0]['vuln'], "Denial Of Service")


    def test_get_labs_code_items(self):
        """Test if the get labs code items call is working"""
        response = self.client.get('/api/interactive_labs/code/items/type/php')
        self.assertEqual(response.status_code, 200)
        response_dict = json.loads(response.data.decode('utf-8'))
        self.assertEqual(response_dict['items'][0]['id'], 1)


    def test_get_labs_code_solutions_correct(self):
        """Test if the get labs code solution item is correct call is working"""
        response = self.client.get('/api/interactive_labs/code/items/code/1/solution/2')
        self.assertEqual(response.status_code, 200)
        response_dict = json.loads(response.data.decode('utf-8'))
        self.assertEqual(response_dict['status'], "correct")


    def test_get_labs_code_solutions_incorrect(self):
        """Test if the get labs code solution item is incorrect call is working"""
        response = self.client.get('/api/interactive_labs/code/items/code/1/solution/22')
        self.assertEqual(response.status_code, 200)
        response_dict = json.loads(response.data.decode('utf-8'))
        self.assertEqual(response_dict['status'], "incorrect")


    def test_get_kb(self):
        """Test if the get kb items call is working"""
        response = self.client.get('/api/kb/items/1')
        self.assertEqual(response.status_code, 200)
        response_dict = json.loads(response.data.decode('utf-8'))
        self.assertEqual(response_dict['items'][0]['title'], "empty control")


    def test_get_kb_item_10(self):
        """Test if the get specific kb item call is working"""
        response = self.client.get('/api/kb/9')
        self.assertEqual(response.status_code, 200)
        response_dict = json.loads(response.data.decode('utf-8'))
        self.assertEqual(response_dict['title'], "J2EE Misconfiguration Weak Access Permissions for EJB Methods")


    def test_update_kb(self):
        """Test if the update kb items call is working"""
        jwt = self.login('admin', 'admin')        
        payload = {'content': 'Unit test content update', 'title': 'Unit test title update'}
        headers = {'content-type': 'application/json', 'Authorization': jwt}
        response = self.client.put('/api/kb/update/1', data=json.dumps(payload), headers=headers)
        self.assertEqual(response.status_code, 200)
        response_dict = json.loads(response.data.decode('utf-8'))
        self.assertEqual(response_dict['message'], "KB item successfully updated")
        response = self.client.get('/api/kb/items/1')
        self.assertEqual(response.status_code, 200)
        response_dict = json.loads(response.data.decode('utf-8'))
        self.assertEqual(response_dict['items'][0]['title'], "empty control")


    def test_new_kb(self):
        """Test if the create kb items call is working"""
        jwt = self.login('admin', 'admin')        
        payload = {'content': 'Unit test content new', 'title': 'Unit test title new'}
        headers = {'content-type': 'application/json', 'Authorization': jwt}
        response = self.client.put('/api/kb/new/1', data=json.dumps(payload), headers=headers)
        self.assertEqual(response.status_code, 200)
        response_dict = json.loads(response.data.decode('utf-8'))
        self.assertEqual(response_dict['message'], "KB item successfully created")



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
        self.assertEqual(response_dict['items'][0]['name'], "Design Patterns ASVS LvL 2")


    def test_delete_project_item(self):
        """Test if the delete project item call is working"""
        jwt = self.login('admin', 'admin') 
        payload = {'description': 'Unit test description project', 'name': 'Unit test name project', 'checklist_type': 1, 'version': 'version 1.0'}
        headers = {'content-type': 'application/json', 'Authorization': jwt}
        response = self.client.put('/api/project/new', data=json.dumps(payload), headers=headers)
        self.assertEqual(response.status_code, 200)
        response_dict = json.loads(response.data.decode('utf-8'))
        self.assertEqual(response_dict['message'], "Project successfully created")
        response = self.client.delete('/api/project/delete/1', headers=headers)
        self.assertEqual(response.status_code, 200)
        response_dict = json.loads(response.data.decode('utf-8'))
        self.assertEqual(response_dict['message'], "Project successfully deleted")


    def test_create_sprint(self):
        """Test if the create new sprint call is working"""
        jwt = self.login('admin', 'admin')        
        payload = {'description': 'Unit test description sprint', 'name': 'Unit test name sprint', 'project_id': 1}
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
        payload = {'description': 'Unit test description sprint', 'name': 'Unit test name sprint', 'project_id': 2}
        response = self.client.put('/api/sprint/new', data=json.dumps(payload), headers=headers)
        self.assertEqual(response.status_code, 200)
        response_dict = json.loads(response.data.decode('utf-8'))
        self.assertEqual(response_dict['message'], "Sprint successfully created")
        response = self.client.get('/api/sprint/44', headers=headers)
        self.assertEqual(response.status_code, 200)
        response_dict = json.loads(response.data.decode('utf-8'))
        self.assertEqual(response_dict['name'], "Unit test name sprint")


    def test_update_sprint_item(self):
        """Test if the sprint update call is working"""
        jwt = self.login('admin', 'admin') 
        payload = {'description': 'Unit test description sprint update', 'name': 'Unit test name sprint update', 'project_id': 3}
        headers = {'content-type': 'application/json', 'Authorization': jwt}
        response = self.client.put('/api/sprint/update/44', data=json.dumps(payload), headers=headers)
        self.assertEqual(response.status_code, 200)
        response_dict = json.loads(response.data.decode('utf-8'))
        self.assertEqual(response_dict['message'], "Sprint successfully updated")
        response = self.client.get('/api/sprint/44', headers=headers)
        self.assertEqual(response.status_code, 200)
        response_dict = json.loads(response.data.decode('utf-8'))
        self.assertEqual(response_dict['name'], "Unit test name sprint update")


    def test_delete_sprint_item(self):
        """Test if the delete project item call is working"""
        jwt = self.login('admin', 'admin') 
        payload = {'description': 'Unit test description sprint', 'name': 'Unit test name sprint', 'project_id': 2}
        headers = {'content-type': 'application/json', 'Authorization': jwt}
        response = self.client.put('/api/sprint/new', data=json.dumps(payload), headers=headers)
        response_dict = json.loads(response.data.decode('utf-8'))
        self.assertEqual(response_dict['message'], "Sprint successfully created")
        response = self.client.delete('/api/sprint/delete/2', headers=headers)
        self.assertEqual(response.status_code, 200)
        response_dict = json.loads(response.data.decode('utf-8'))
        self.assertEqual(response_dict['message'], "Sprint successfully deleted")


    def test_results_sprint(self):
        """Test if the results sprint call is working"""
        jwt = self.login('admin', 'admin')
        payload = {'description': 'Unit test description project', 'name': 'Unit test name project', 'checklist_type': 2, 'version': 'version 1.0'}
        headers = {'content-type': 'application/json', 'Authorization': jwt}
        response = self.client.put('/api/project/new', data=json.dumps(payload), headers=headers)
        self.assertEqual(response.status_code, 200)
        response_dict = json.loads(response.data.decode('utf-8'))
        self.assertEqual(response_dict['message'], "Project successfully created")
        payload = {'description': 'Unit test description sprint', 'name': 'Unit test name sprint', 'project_id': 3}
        response = self.client.put('/api/sprint/new', data=json.dumps(payload), headers=headers)
        self.assertEqual(response.status_code, 200)
        payload = {'questions': [ {'project_id': 3, 'question_id': 1,'result': 'True', 'sprint_id': 2, 'checklist_type': 1},{'project_id': 3, 'question_id': 2,'result': 'True', 'sprint_id': 2, 'checklist_type': 1} ]}
        response = self.client.put('/api/questions/store/1/1', data=json.dumps(payload), headers=headers)
        self.assertEqual(response.status_code, 200)
        response_dict = json.loads(response.data.decode('utf-8'))
        self.assertEqual(response_dict['message'], "Sprint successfully created")
        response = self.client.get('/api/sprint/stats/2', headers=headers)
        self.assertEqual(response.status_code, 200)
        response = self.client.get('/api/sprint/results/2', headers=headers)
        self.assertEqual(response.status_code, 200)
        response_dict = json.loads(response.data.decode('utf-8'))
        response = self.client.get('/api/sprint/results/export/2', headers=headers)
        self.assertEqual(response.status_code, 200)


    def test_delete_project_item_fail(self):
        """Test if the delete project item fail call is working"""
        jwt = self.login('admin', 'admin') 
        headers = {'content-type': 'application/json', 'Authorization': jwt}
        response = self.client.delete('/api/project/delete/1', headers=headers)
        self.assertEqual(response.status_code, 400)


    def test_question_items(self):
        """Test if the get questions item call is working"""
        headers = {'content-type': 'application/json'}
        response = self.client.get('/api/questions/items/1', headers=headers)
        self.assertEqual(response.status_code, 200)
        response_dict = json.loads(response.data.decode('utf-8'))
        self.assertEqual(response_dict['items'][0]['question'], "Authentication Architectural Requirements")


    def test_question_update(self):
        """Test if the update questions item call is working"""
        jwt = self.login('admin', 'admin') 
        payload = {'question': 'Unit test question', 'checklist_type': 1}
        headers = {'content-type': 'application/json', 'Authorization': jwt}
        response = self.client.put('/api/questions/item/update/15', data=json.dumps(payload), headers=headers)
        self.assertEqual(response.status_code, 200)
        response_dict = json.loads(response.data.decode('utf-8'))
        self.assertEqual(response_dict['message'], 'Question successfully updated')


    def test_question_new(self):
        """Test if the new question item call is working"""
        jwt = self.login('admin', 'admin') 
        payload = {'question': 'New Unit test question', 'checklist_type': 1}
        headers = {'content-type': 'application/json', 'Authorization': jwt}
        response = self.client.put('/api/questions/item/new', data=json.dumps(payload), headers=headers)
        self.assertEqual(response.status_code, 200)
        response_dict = json.loads(response.data.decode('utf-8'))
        self.assertEqual(response_dict['message'], 'New Question successfully created')


    def test_question_delete(self):
        """Test if the delete question item call is working"""
        jwt = self.login('admin', 'admin') 
        headers = {'content-type': 'application/json', 'Authorization': jwt}
        response = self.client.delete('/api/questions/item/delete/1', headers=headers)
        self.assertEqual(response.status_code, 200)
        response_dict = json.loads(response.data.decode('utf-8'))
        self.assertEqual(response_dict['message'], "Question successfully deleted")


    def test_auth_protected_call(self):
        """Test if the delete project item fail call is working"""
        payload = {'description': 'Unit test description project', 'name': 'Unit test name project', 'checklist_type': 1, 'version': 'version 1.0'}
        headers = {'content-type': 'application/json', 'Authorization': 'woopwoopwrong'}
        response = self.client.put('/api/project/new', data=json.dumps(payload), headers=headers)
        self.assertEqual(response.status_code, 403)
    

    def test_get_code(self):
        """Test if the get code items call is working"""
        response = self.client.get('/api/code/items/1')
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
        response = self.client.get('/api/code/items/1')
        self.assertEqual(response.status_code, 200)
        response_dict = json.loads(response.data.decode('utf-8'))
        self.assertEqual(response_dict['items'][0]['title'], "Unit test title update")


    def test_create_code(self):
        """Test if the create code items call is working"""
        jwt = self.login('admin', 'admin')        
        payload = {'code_lang': 'test', 'content': 'Unit test content create', 'title': 'Unit test title create'}
        headers = {'content-type': 'application/json', 'Authorization': jwt}
        response = self.client.put('/api/code/new/1', data=json.dumps(payload), headers=headers)
        self.assertEqual(response.status_code, 200)
        response_dict = json.loads(response.data.decode('utf-8'))
        self.assertEqual(response_dict['message'], "Code example item successfully created")
        response = self.client.get('/api/code/items/1')
        self.assertEqual(response.status_code, 200)


    def test_delete_code(self):
        """Test if the delete code item call is working"""
        jwt = self.login('admin', 'admin') 
        headers = {'content-type': 'application/json', 'Authorization': jwt}
        response = self.client.delete('/api/code/delete/100', headers=headers)
        self.assertEqual(response.status_code, 200)
        response_dict = json.loads(response.data.decode('utf-8'))
        self.assertEqual(response_dict['message'], "Code example item successfully deleted")


    def test_get_description_item(self):
        """Test if the description call is working"""
        payload = {"question": "what is xss?", "question_option": 0, "question_lang": "string"}
        headers = {'content-type': 'application/json', 'Accept':'application/json'}
        response = self.client.post('/api/chatbot/question', data=json.dumps(payload), headers=headers)
        self.assertEqual(response.status_code, 200)
        response_dict = json.loads(response.data.decode('utf-8'))
        if settings.GOOGLE == False:
            res = response_dict['options'][0]['answer'][0:29]
            self.assertEqual(res,"Description for XSS injection")


    def test_get_solution_item(self):
        """Test if the solution call is working"""
        payload = {"question": "how to resolve xss?", "question_option": 0, "question_lang": "string"}
        headers = {'content-type': 'application/json', 'Accept':'application/json'}
        response = self.client.post('/api/chatbot/question', data=json.dumps(payload), headers=headers)
        self.assertEqual(response.status_code, 200)
        response_dict = json.loads(response.data.decode('utf-8'))
        if settings.GOOGLE == False:
            res = response_dict['options'][0]['answer'][0:26]
            self.assertEqual(res,"Solution for XSS injection")


    def test_code_item_list(self):
        """Test if the code item is working"""
        payload = {"question": "code for xss filtering?", "question_option": 0, "question_lang": "string"}
        headers = {'content-type': 'application/json', 'Accept':'application/json'}
        response = self.client.post('/api/chatbot/question', data=json.dumps(payload), headers=headers)
        self.assertEqual(response.status_code, 200)
        response_dict = json.loads(response.data.decode('utf-8'))
        if settings.GOOGLE == False:
            self.assertEqual(response_dict['options'][0]['answer'], "Code xss filtering in java")


    def test_no_match(self):
        """Test if the options are working"""
        payload = {"question": "what is bla?", "question_option": 0, "question_lang": "string"}
        headers = {'content-type': 'application/json', 'Accept':'application/json'}
        response = self.client.post('/api/chatbot/question', data=json.dumps(payload), headers=headers)
        self.assertEqual(response.status_code, 200)
        response_dict = json.loads(response.data.decode('utf-8'))
        if settings.GOOGLE == False:
            self.assertEqual(response_dict['options'][0]['answer'], "Please be more specific")


    def test_get_entity2_item(self):
        """Test if the options are working"""
        payload = {"question": "what are security headers?", "question_option": 0, "question_lang": "string"}
        headers = {'content-type': 'application/json', 'Accept':'application/json'}
        response = self.client.post('/api/chatbot/question', data=json.dumps(payload), headers=headers)
        self.assertEqual(response.status_code, 200)
        response_dict = json.loads(response.data.decode('utf-8'))
        if settings.GOOGLE == False:
            self.assertTrue((response_dict['options'][0]['answer'][0:45])==("Description for API responses security header"))


    def test_get_sol_entity2_item(self):
        """Test if the options are working"""
        payload = {"question": "how to solve rest csrf", "question_option": 0, "question_lang": "string"}
        headers = {'content-type': 'application/json', 'Accept':'application/json'}
        response = self.client.post('/api/chatbot/question', data=json.dumps(payload), headers=headers)
        self.assertEqual(response.status_code, 200)
        response_dict = json.loads(response.data.decode('utf-8'))
        if settings.GOOGLE == False:
            self.assertTrue((response_dict['options'][0]['answer'])==("Solution user restriction for sensitive data") or (response_dict['options'][0]['answer'])==("Solution csrf on rest")) 


    def test_code_lang_item2(self):
        """Test if the options are working"""
        payload = {"question": "code example for xss", "question_option": 0, "question_lang": "string"}
        headers = {'content-type': 'application/json', 'Accept':'application/json'}
        response = self.client.post('/api/chatbot/question', data=json.dumps(payload), headers=headers)
        self.assertEqual(response.status_code, 200)
        response_dict = json.loads(response.data.decode('utf-8'))
        if settings.GOOGLE == False:
            self.assertTrue((response_dict['options'][0]['answer'])==("Code encoder") or (response_dict['options'][0]['answer'])==("Code xss filtering") or (response_dict['options'][0]['answer'])==("Code x xss protection header") or (response_dict['options'][0]['answer'])==("Code encoder sql esapi"))


    def test_code_lang_item(self):
        """Test if the options are working"""
        payload = {"question": "code example for code encoder", "question_option": 0, "question_lang": "string"}
        headers = {'content-type': 'application/json', 'Accept':'application/json'}
        response = self.client.post('/api/chatbot/question', data=json.dumps(payload), headers=headers)
        self.assertEqual(response.status_code, 200)
        response_dict = json.loads(response.data.decode('utf-8'))
        if settings.GOOGLE == False:
            self.assertEqual(response_dict['options'][0]['answer'], "Code encoder in php")
         
    
    def test_code_classify_item(self):
        """Test if the code classify is working"""
        payload = {"question": "code example for xss filtering in java", "question_option": 0, "question_lang": "string"}
        headers = {'content-type': 'application/json', 'Accept':'application/json'}
        response = self.client.post('/api/chatbot/question', data=json.dumps(payload), headers=headers)
        self.assertEqual(response.status_code, 200)
        response_dict = json.loads(response.data.decode('utf-8'))
        if settings.GOOGLE == False:
            res = response_dict['options'][0]['answer'][0:23]
            self.assertEqual(res, "Code for  XSS filtering")


    def test_assert_403_project_new(self):
        payload = {'description': 'Unit test description project', 'name': 'Unit test name project', 'checklist_type': 1, 'version': 'version 1.0'}
        headers = {'content-type': 'application/json'}
        response = self.client.put('/api/project/new', data=json.dumps(payload), headers=headers)
        self.assertEqual(response.status_code, 403)


    def test_assert_403_project_delete(self):
        payload = {'test': 'test'}
        headers = {'content-type': 'application/json'}
        response = self.client.delete('/api/project/delete/1', data=json.dumps(payload), headers=headers)
        self.assertEqual(response.status_code, 403)


    def test_assert_403_user_create(self):
        payload = {'email': 'test_user123@owasp.org', 'privilege_id': 1}
        headers = {'content-type': 'application/json'}
        response = self.client.put('/api/user/create', data=json.dumps(payload), headers=headers)
        self.assertEqual(response.status_code, 403)


    def test_assert_400_user_create(self):
        """Test if the login fail create call is working"""
        jwt = self.login('admin', 'admin')
        payload = {'email': 'test_user@owasp.org', 'privilege_id': 2}
        headers = {'content-type': 'application/json', 'Authorization': jwt}
        response = self.client.put('/api/user/create', data=json.dumps(payload), headers=headers)
        self.assertEqual(response.status_code, 200)
        response_dict = json.loads(response.data.decode('utf-8'))
        self.assertEqual(response_dict['email'], "test_user@owasp.org")
        response = self.client.put('/api/user/create', data=json.dumps(payload), headers=headers)
        self.assertEqual(response.status_code, 400)
        response_dict = json.loads(response.data.decode('utf-8'))
        self.assertEqual(response_dict['message'], "User could not be created")


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




class AppTestCase(unittest.TestCase):
    def setUp(self):
        self.change_password = ChangePassword(min_password_length=8)

    def test_length(self):
        result = self.change_password.valid_password('tiny')
        assert 'insufficient length' in result, result

    def test_uppercase(self):
        result = self.change_password.valid_password('alllowercase')
        assert '1 uppercase required' in result, result
        rules = self.change_password.rules
        self.change_password.update_rules(dict(uppercase=22))
        result = self.change_password.valid_password('alllowercase')
        assert '22 uppercase required' in result, result
        self.change_password.update_rules(rules)

    def test_lowercase(self):
        result = self.change_password.valid_password('ALLUPPERCASE')
        assert '1 lowercase required' in result, result
        rules = self.change_password.rules
        self.change_password.update_rules(dict(lowercase=20))
        result = self.change_password.valid_password('ALLUPPERCASE')
        assert '20 lowercase required' in result, result
        self.change_password.update_rules(rules)

    def test_nonumbers(self):
        result = self.change_password.valid_password('NoNumbers')
        assert '1 number required' in result, result
        rules = self.change_password.rules
        self.change_password.update_rules(dict(numbers=2))
        result = self.change_password.valid_password('NoNumbers')
        assert '2 numbers required' in result, result
        self.change_password.update_rules(rules)

    def test_punctuation(self):
        result = self.change_password.valid_password('NoNumbers2')
        assert '1 punctuation required' in result, result
        rules = self.change_password.rules
        self.change_password.update_rules(dict(punctuation=2))
        result = self.change_password.valid_password('NoNumbers2')
        assert '2 punctuations required' in result, result
        self.change_password.update_rules(rules)

    def test_diff_username(self):
        result = self.change_password.valid_password('NoNumbers2!', username='Numbers')
        assert 'insufficient difference from username' in result, result

    def test_simple_passwords(self):
        # has inside
        result = self.change_password.valid_password('jjrudeboyAy2!', username='Numbers')
        assert 'too similar to common password: rudeboy' in result, result
        # has inside but password longer than 2 x known bad password
        result = self.change_password.valid_password('jj--iuerudeboyAy2!', username='Numbers')
        assert 5 == result, result
        # starts with
        result = self.change_password.valid_password('monkey9054343hyAy2!', username='Numbers')
        assert 'too similar to common password: monkey' in result, result

    def test_123(self):
        result = self.change_password.valid_password('ru%d*eboyAy123!', username='Numbers')
        assert 'not enough number complexity, 123 disallowed' in result
        result = self.change_password.valid_password('ru!d%eboyAy789!', username='Numbers')
        assert 'not enough number complexity, 789 disallowed' in result

    def test_wxyz(self):
        test_password = 'ru@de%boyAy432wxyz'
        result = self.change_password.valid_password(test_password, username='Numbers')
        assert 5 == result, result

        self.change_password.update_rules(dict(alphabet_sequence=True))

        result = self.change_password.valid_password(test_password, username='Numbers')
        assert 'insufficient letter complexity, wxyz disallowed' in result, result

        result = self.change_password.valid_password('ru%d$eboyAy432WXYZ!', username='Numbers')
        assert 'insufficient letter complexity, wxyz disallowed' in result, result

    def test_pwned(self):
        rules = self.change_password.rules
        self.change_password.update_rules(
            {'punctuation': 0, 'uppercase': 0, 'lowercase': 0, 'number_sequence': False,
             'username': False, 'numbers': 0, 'username_length': 0, 'username_requires_separators': False,
             'passwords': False, 'keyboard_sequence': False, 'alphabet_sequence': False,
             'long_password_override': 0, 'pwned': True, 'min_password_length': 0})
        # known pwned password
        test_password = 'monkey'
        result = self.change_password.valid_password(test_password, username='Numbers')
        assert 'is a known hacked password' in result, result
        # this should not be pwned
        test_password = '1F6A4068DC0A7ADA930C555C3CE5B35445C:1; 1F7AD9E67E4437D507D2E8E50951889E605:2; 1FA5A0CA12BE10:1'
        result = self.change_password.valid_password(test_password, username='Numbers')
        assert 5 == result, result
        self.change_password.update_rules(rules)

    def test_qwerty(self):
        result = self.change_password.valid_password('ru@deboyAy432qwerty!', username='Numbers')
        assert 5 == result, result

        self.change_password.update_rules(dict(keyboard_sequence=True))

        result = self.change_password.valid_password('rud$e^boyAy432qwerty!', username='Numbers')
        assert 'keyboard sequence found, qwer disallowed' in result, result
        result = self.change_password.valid_password('r!judeboyAy432QWERTY!', username='Numbers')
        assert 'keyboard sequence found, qwer disallowed' in result, result

    def test_long_enough_to_pass_with_bad_stuff(self):
        result = self.change_password.valid_password('monkeyNumbers.rudeboyAy2123!', username='Numbers')
        assert result == 'insufficient difference from username', result
        self.change_password.update_rules(dict(min_password_length=10, long_password_override=2))
        result = self.change_password.valid_password('monkeyNumbers.rudeboyAy2123!', username='Numbers')
        assert result == 5, result

    def test_check_username(self):
        self.change_password.update_rules({'username_length': 4})
        result = self.change_password.valid_username(username='bad')
        assert result == 'User name too short.  4 required', result

    def test_baduser(self):
        result = self.change_password.valid_username(username='baduser.')
        assert result == 'Invalid user name', result

        result = self.change_password.valid_username(username='-baduser')
        assert result == 'Invalid user name', result

        result = self.change_password.valid_username(username='baduser')
        assert result == '', result

        self.change_password.update_rules({'username_requires_separators': 4})
        result = self.change_password.valid_username(username='baduser')
        assert result == '. or - required', result

        result = self.change_password.valid_username(username='good.user')
        assert result == '', result

        result = self.change_password.valid_username(username='good-user')
        assert result == '', result


class ClientAppTestCase(unittest.TestCase):
    def setUp(self):
        app = Flask(__name__, static_url_path='/static')
        app.testing = True
        app.secret_key = 'testing'
        app.config['WTF_CSRF_ENABLED'] = False
        app.route('/change_password', methods=['GET', 'POST'])(self.route_change_password)
        self.change_password = ChangePassword(app=app, min_password_length=8)
        self.app = app.test_client()

    def test_check_password(self):
        result = self.app.post('/flask_change_password/check_password', data=dict(password='tiny'),
                               follow_redirects=True)
        result_text = result.data.decode('utf-8')
        assert 'length' in result_text, result_text

    def test_get_password_page(self):
        result = self.app.get('/change_password')
        assert result.status_code == 200
        result_text = result.data.decode('utf-8')
        assert 'Current Password' in result_text, result_text

    def test_update_password(self):
        new_password = 'Atiny98437fdsjkl---387'
        result = self.app.post('/change_password',
                               data=dict(username='max', old_password='hello', password=new_password,
                                         password2=new_password),
                               follow_redirects=True)

        assert 'ok' == result.data.decode('utf-8'), result.data.decode('utf-8')

    def route_change_password(self):
        title = 'Change Password'
        form = ChangePasswordForm(username='max', changing=True, title=title)
        if request.method == 'POST':
            if form.validate_on_submit():
                valid = self.change_password.verify_password_change_form(form)
                return 'ok'
            else:
                for field, errors in form.errors.items():
                    for error in errors:
                        print(u"Error in the {} field - {}".format(
                            getattr(form, field).label.text,
                            error
                        ))
                return 'failed', 201

        password_template = self.change_password.change_password_template(form)
        return render_template_string('''<h1>{{ title }}</h1> {{ password_template | safe }} ''', title=title,
                                      form=form, password_template=password_template)


if __name__ == '__main__':
    unittest.main()
