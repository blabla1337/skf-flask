import unittest, sys, time, skf
from skf import settings
from skf.db_tools import init_db, connect_db
from skf.app import app
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC

class SKFClickThrough(unittest.TestCase):

    @classmethod
    def setUp(self):
        self.client = app.test_client()
        with app.app_context():
            init_db(True)
            settings.TESTING = True
        self.driver = webdriver.Chrome()
        driver = self.driver
        driver.get("http://localhost:4200")
        username = driver.find_element_by_name("username")
        password = driver.find_element_by_name("password")
        username.send_keys("admin")
        password.send_keys("admin")
        password.send_keys(Keys.RETURN)


    """
    ////////////////////////////////////////////////////////////////////////////////////
    Test create new project + sprints
    ////////////////////////////////////////////////////////////////////////////////////
    """


    def test_a_create_project(self):
        """Test project create page"""
        driver = self.driver
        wait = WebDriverWait(driver, 10)
        input = wait.until(EC.visibility_of_element_located((By.ID, "1")))
        input.click()     
        driver.find_element_by_link_text('New Project').click()
        input.click()
        checklist = Select(driver.find_element_by_id("question"))
        checklist.select_by_index(2)
        time.sleep(1)
        input = wait.until(EC.visibility_of_element_located((By.ID, "checklist")))
        input.click()
        time.sleep(1)
        inputName = driver.find_element_by_id("inputName")
        inputName.send_keys("test project")
        inputVersion = driver.find_element_by_id("inputVersion")
        inputVersion.send_keys("test v1.1")
        inputDesc = driver.find_element_by_id("inputDesc")
        inputDesc.send_keys("test description project")
        input = driver.find_element_by_xpath("//i[contains(@class, 'fa fa-arrow-right')]")
        input.click()
        checklist = Select(driver.find_element_by_id("pre_dev_answer1"))
        checklist.select_by_index(1)
        input = driver.find_element_by_xpath("//i[contains(@class, 'fa fa-arrow-right 3')]")
        input.click()
        sprintName = driver.find_element_by_id("sprintName")
        sprintName.send_keys("test sprint")
        sprintDescription = driver.find_element_by_id("sprintDescription")
        sprintDescription.send_keys("test sprint description")
        input = driver.find_element_by_xpath("//i[contains(@class, 'fa fa-arrow-right 4')]")
        input.click()
        sprint = Select(driver.find_element_by_id("sprint_answer1"))
        sprint.select_by_index(2)
        input = driver.find_element_by_xpath("//i[contains(@class, 'fa fa-arrow-right 5')]")
        input.click()
        time.sleep(1)
        input = driver.find_element_by_xpath("//i[contains(@class, 'fa fa-check')]")
        input.click()
        input = wait.until(EC.visibility_of_element_located((By.ID, "view1")))
        input.click()
        time.sleep(3)
        assert "1.1 test content checklist item 1" in driver.page_source


    def test_a_project_list(self):
        """Test project list page"""
        driver = self.driver
        wait = WebDriverWait(driver, 10)
        input = wait.until(EC.visibility_of_element_located((By.ID, "1")))
        input.click()     
        driver.find_element_by_link_text('New Project').click()
        input.click()
        checklist = Select(driver.find_element_by_id("question"))
        checklist.select_by_index(2)
        time.sleep(1)
        input = wait.until(EC.visibility_of_element_located((By.ID, "checklist")))
        input.click()
        time.sleep(1)
        inputName = driver.find_element_by_id("inputName")
        inputName.send_keys("test project")
        inputVersion = driver.find_element_by_id("inputVersion")
        inputVersion.send_keys("test v1.1")
        inputDesc = driver.find_element_by_id("inputDesc")
        inputDesc.send_keys("test description project")
        input = driver.find_element_by_xpath("//i[contains(@class, 'fa fa-arrow-right')]")
        input.click()
        checklist = Select(driver.find_element_by_id("pre_dev_answer1"))
        checklist.select_by_index(1)
        input = driver.find_element_by_xpath("//i[contains(@class, 'fa fa-arrow-right 3')]")
        input.click()
        sprintName = driver.find_element_by_id("sprintName")
        sprintName.send_keys("test sprint")
        sprintDescription = driver.find_element_by_id("sprintDescription")
        sprintDescription.send_keys("test sprint description")
        input = driver.find_element_by_xpath("//i[contains(@class, 'fa fa-arrow-right 4')]")
        input.click()
        sprint = Select(driver.find_element_by_id("sprint_answer1"))
        sprint.select_by_index(2)
        input = driver.find_element_by_xpath("//i[contains(@class, 'fa fa-arrow-right 5')]")
        input.click()
        time.sleep(1)
        input = driver.find_element_by_xpath("//i[contains(@class, 'fa fa-check')]")
        input.click()
        time.sleep(3)
        input = wait.until(EC.visibility_of_element_located((By.ID, "1")))
        input.click()     
        driver.find_element_by_link_text('List Projects').click()
        input.click()
        time.sleep(3)
        assert "3" in driver.page_source


    def test_a_project_and_sprint(self):
        """Test project sprint page"""
        driver = self.driver
        wait = WebDriverWait(driver, 10)
        input = wait.until(EC.visibility_of_element_located((By.ID, "1")))
        input.click()     
        driver.find_element_by_link_text('New Project').click()
        input.click()
        checklist = Select(driver.find_element_by_id("question"))
        checklist.select_by_index(2)
        time.sleep(1)
        input = wait.until(EC.visibility_of_element_located((By.ID, "checklist")))
        input.click()
        time.sleep(1)
        inputName = driver.find_element_by_id("inputName")
        inputName.send_keys("test project")
        inputVersion = driver.find_element_by_id("inputVersion")
        inputVersion.send_keys("test v1.1")
        inputDesc = driver.find_element_by_id("inputDesc")
        inputDesc.send_keys("test description project")
        input = driver.find_element_by_xpath("//i[contains(@class, 'fa fa-arrow-right')]")
        input.click()
        checklist = Select(driver.find_element_by_id("pre_dev_answer1"))
        checklist.select_by_index(1)
        input = driver.find_element_by_xpath("//i[contains(@class, 'fa fa-arrow-right 3')]")
        input.click()
        sprintName = driver.find_element_by_id("sprintName")
        sprintName.send_keys("test sprint")
        sprintDescription = driver.find_element_by_id("sprintDescription")
        sprintDescription.send_keys("test sprint description")
        input = driver.find_element_by_xpath("//i[contains(@class, 'fa fa-arrow-right 4')]")
        input.click()
        sprint = Select(driver.find_element_by_id("sprint_answer1"))
        sprint.select_by_index(2)
        input = driver.find_element_by_xpath("//i[contains(@class, 'fa fa-arrow-right 5')]")
        input.click()
        time.sleep(1)
        input = driver.find_element_by_xpath("//i[contains(@class, 'fa fa-check')]")
        input.click()
        time.sleep(3)
        input = wait.until(EC.visibility_of_element_located((By.ID, "1")))
        input.click()     
        time.sleep(3)
        input = driver.find_element_by_xpath("//i[contains(@class, 'fa fa-cog')]")
        input.click()
        sprintName = driver.find_element_by_id("sprintName")
        sprintName.send_keys("test sprint new")
        sprintDescription = driver.find_element_by_id("sprintDescription")
        sprintDescription.send_keys("test sprint desc new")
        input = wait.until(EC.visibility_of_element_located((By.ID, "create-sprint")))
        input.click()
        sprint = Select(driver.find_element_by_id("sprint_answer2"))
        sprint.select_by_index(1)
        input = wait.until(EC.visibility_of_element_located((By.ID, "store-sprint")))
        input.click()
        time.sleep(10)
        assert "2" in driver.page_source


    def test_a_delete_project(self):
        """Test project delete page"""
        driver = self.driver
        wait = WebDriverWait(driver, 10)
        input = wait.until(EC.visibility_of_element_located((By.ID, "1")))
        input.click()     
        driver.find_element_by_link_text('New Project').click()
        input.click()
        checklist = Select(driver.find_element_by_id("question"))
        checklist.select_by_index(2)
        time.sleep(1)
        input = wait.until(EC.visibility_of_element_located((By.ID, "checklist")))
        input.click()
        time.sleep(1)
        inputName = driver.find_element_by_id("inputName")
        inputName.send_keys("test project")
        inputVersion = driver.find_element_by_id("inputVersion")
        inputVersion.send_keys("test v1.1")
        inputDesc = driver.find_element_by_id("inputDesc")
        inputDesc.send_keys("test description project")
        input = driver.find_element_by_xpath("//i[contains(@class, 'fa fa-arrow-right')]")
        input.click()
        checklist = Select(driver.find_element_by_id("pre_dev_answer1"))
        checklist.select_by_index(1)
        input = driver.find_element_by_xpath("//i[contains(@class, 'fa fa-arrow-right 3')]")
        input.click()
        sprintName = driver.find_element_by_id("sprintName")
        sprintName.send_keys("test sprint")
        sprintDescription = driver.find_element_by_id("sprintDescription")
        sprintDescription.send_keys("test sprint description")
        input = driver.find_element_by_xpath("//i[contains(@class, 'fa fa-arrow-right 4')]")
        input.click()
        sprint = Select(driver.find_element_by_id("sprint_answer1"))
        sprint.select_by_index(2)
        input = driver.find_element_by_xpath("//i[contains(@class, 'fa fa-arrow-right 5')]")
        input.click()
        time.sleep(1)
        input = driver.find_element_by_xpath("//i[contains(@class, 'fa fa-check')]")
        input.click()
        time.sleep(3)
        input = wait.until(EC.visibility_of_element_located((By.ID, "1")))
        input.click()     
        driver.find_element_by_link_text('List Projects').click()
        input.click()
        time.sleep(3)
        input = wait.until(EC.visibility_of_element_located((By.ID, "delete-button")))
        input.click()
        time.sleep(3)
        delete = driver.find_element_by_id("delete")
        delete.send_keys("DELETE")
        input = wait.until(EC.visibility_of_element_located((By.ID, "submit")))
        input.click()
        time.sleep(1)
        assert "test project" not in driver.page_source

        
    """
    ////////////////////////////////////////////////////////////////////////////////////
    Test user creation, granting and revoking
    ////////////////////////////////////////////////////////////////////////////////////
    """


    def test_a_create_user(self):
        """Test user create page"""
        driver = self.driver
        wait = WebDriverWait(driver, 10)
        input = wait.until(EC.visibility_of_element_located((By.ID, "2")))
        input.click()     
        driver.find_element_by_link_text('Add users').click()
        input.click()
        kbTitle = driver.find_element_by_id("email")
        kbTitle.send_keys("test@localhost")
        time.sleep(1)
        priv = Select(driver.find_element_by_name("privilegeSelected"))
        priv.select_by_index(0)
        time.sleep(1)
        input = wait.until(EC.visibility_of_element_located((By.ID, "createUser")))
        input.click()
        time.sleep(5)
        assert "Authorization token" in driver.page_source


    def test_a_first_login_user(self):
        """Test user first login page"""
        driver = self.driver
        wait = WebDriverWait(driver, 10)
        input = wait.until(EC.visibility_of_element_located((By.ID, "2")))
        input.click()     
        driver.find_element_by_link_text('Add users').click()
        input.click()
        kbTitle = driver.find_element_by_id("email")
        kbTitle.send_keys("test@localhost")
        time.sleep(1)
        priv = Select(driver.find_element_by_name("privilegeSelected"))
        priv.select_by_index(0)
        time.sleep(1)
        input = wait.until(EC.visibility_of_element_located((By.ID, "createUser")))
        input.click()
        time.sleep(1)
        raw_string = driver.find_element_by_xpath("//div[@class='alert alert-warning']/p").text
        split_string = raw_string.split(" ")
        user_id = split_string[6]
        access_token = split_string[8]
        input = wait.until(EC.visibility_of_element_located((By.ID, "user-profile")))
        input.click()
        input = wait.until(EC.visibility_of_element_located((By.ID, "user-logout")))
        input.click()        
        time.sleep(2)
        driver.find_element_by_link_text('first-login').click()
        userID = driver.find_element_by_id("userID")
        userID.send_keys(user_id)
        token = driver.find_element_by_id("token")
        token.send_keys(access_token)
        email = driver.find_element_by_id("email")
        email.send_keys("test@localhost")
        username = driver.find_element_by_id("username")
        username.send_keys("foobar")
        password = driver.find_element_by_id("password")
        password.send_keys("12345Pass")
        repassword = driver.find_element_by_id("repassword")
        repassword.send_keys("12345Pass")
        input = wait.until(EC.visibility_of_element_located((By.ID, "create")))
        input.click()
        driver.get("http://localhost:4200")
        username = driver.find_element_by_name("username")
        password = driver.find_element_by_name("password")
        username.send_keys("foobar")
        password.send_keys("12345Pass")
        password.send_keys(Keys.RETURN)
        time.sleep(2)
        assert "Projects" in driver.page_source


    def test_a_revoke_user(self):
        """Test user revoke page"""
        driver = self.driver
        wait = WebDriverWait(driver, 10)
        input = wait.until(EC.visibility_of_element_located((By.ID, "2")))
        input.click()     
        driver.find_element_by_link_text('Manage users').click()
        input.click()
        input = wait.until(EC.visibility_of_element_located((By.ID, "revoke-access0")))
        input.click()
        time.sleep(1)
        revoke = driver.find_element_by_id("revoke")
        revoke.send_keys("REVOKE")
        input = wait.until(EC.visibility_of_element_located((By.ID, "submit")))
        input.click()
        time.sleep(1)
        input = wait.until(EC.visibility_of_element_located((By.ID, "user-profile")))
        input.click()
        input = wait.until(EC.visibility_of_element_located((By.ID, "user-logout")))
        input.click()        
        time.sleep(2)
        username = driver.find_element_by_name("username")
        password = driver.find_element_by_name("password")
        username.send_keys("admin")
        password.send_keys("admin")
        password.send_keys(Keys.RETURN)
        time.sleep(2)
        assert "Wrong username/password combination!" in driver.page_source


    """
    ////////////////////////////////////////////////////////////////////////////////////
    Test knowledge base + code example search + update/add knowledge base item
    ////////////////////////////////////////////////////////////////////////////////////
    """

    def test_a_code_example_search(self):
        """Test search code example page"""
        driver = self.driver
        wait = WebDriverWait(driver, 10)
        input = wait.until(EC.visibility_of_element_located((By.ID, "6")))
        input.click()
        input = wait.until(EC.visibility_of_element_located((By.ID, "search")))
        input.click()
        searchKB = driver.find_element_by_name("search")
        searchKB.send_keys("2")
        driver.find_element_by_link_text('test php content code item 2').click()
        input.click()
        time.sleep(1)
        assert "test php content code item 2" in driver.page_source


    def test_a_knowledge_base_search(self):
        """Test search knowledge base page"""
        driver = self.driver
        wait = WebDriverWait(driver, 10)
        input = wait.until(EC.visibility_of_element_located((By.ID, "5")))
        input.click()
        input = wait.until(EC.visibility_of_element_located((By.ID, "search")))
        input.click()
        searchKB = driver.find_element_by_name("search")
        searchKB.send_keys("4")
        driver.find_element_by_link_text('test title kb item 4').click()
        input.click()
        time.sleep(1)
        assert "test content kb item 4" in driver.page_source


    def aaaaaaaaa(self):
        """Test update knowledge base item page"""
        driver = self.driver
        wait = WebDriverWait(driver, 10)
        input = wait.until(EC.visibility_of_element_located((By.ID, "5")))
        input.click()
        input = wait.until(EC.visibility_of_element_located((By.ID, "search")))
        input.click()
        searchKB = driver.find_element_by_name("search")
        searchKB.send_keys("4")
        driver.find_element_by_link_text('test title kb item 4').click()
        input.click()
        time.sleep(1)
        input = wait.until(EC.visibility_of_element_located((By.ID, "update")))
        input.click()
        time.sleep(2)
        kbTitle = driver.find_element_by_id("inputTitle")
        kbTitle.send_keys("update")
        time.sleep(1)
        input = wait.until(EC.visibility_of_element_located((By.ID, "update-button")))
        input.click()
        time.sleep(2)
        assert "test title kb item 4 update" in driver.page_source


    def test_a_add_knowledge_base_item(self):
        """Test add new knowledge base item page"""
        driver = self.driver
        wait = WebDriverWait(driver, 10)
        input = wait.until(EC.visibility_of_element_located((By.ID, "5")))
        input.click()
        input = wait.until(EC.visibility_of_element_located((By.ID, "add")))
        input.click()
        time.sleep(2)
        kbTitle = driver.find_element_by_id("inputTitle")
        kbTitle.send_keys("new kb item")
        time.sleep(1)
        kbContent = driver.find_element_by_id("inputContent")
        kbContent.send_keys("new kb content")
        time.sleep(1)
        input = wait.until(EC.visibility_of_element_located((By.ID, "submit-button")))
        input.click()
        time.sleep(2)
        assert "new kb item" in driver.page_source


    """
    ////////////////////////////////////////////////////////////////////////////////////
    Test the dashboard icon links
    ////////////////////////////////////////////////////////////////////////////////////
    """
    

    def test_a_dashboard_icon_link_to_checklist(self):
        """Test Dashboard Icon button to checklist"""
        driver = self.driver
        wait = WebDriverWait(driver, 10)
        input = wait.until(EC.visibility_of_element_located((By.ID, "checklist-icon")))
        input.click()
        assert "Security checklists" in driver.page_source


    def test_b_dashboard_icon_link_to_project_list(self):
        """Test Dashboard Icon button to projects"""
        driver = self.driver
        wait = WebDriverWait(driver, 10)
        input = wait.until(EC.visibility_of_element_located((By.ID, "project-list-icon")))
        input.click()
        assert "All projects" in driver.page_source


    def test_c_dashboard_icon_link_to_code_example(self):
        """Test Dashboard Icon button to code examples"""
        driver = self.driver
        wait = WebDriverWait(driver, 10)
        input = wait.until(EC.visibility_of_element_located((By.ID, "code-examples-icon")))
        input.click()
        assert "Code examples" in driver.page_source


    def test_d_dashboard_icon_link_to_knowledge_base(self):
        """Test Dashboard Icon button to knowledge base items"""
        driver = self.driver
        wait = WebDriverWait(driver, 10)
        input = wait.until(EC.visibility_of_element_located((By.ID, "knowledgebase-icon")))
        input.click()
        assert "Knowledge Base" in driver.page_source


    """
    ////////////////////////////////////////////////////////////////////////////////////
    Test creating/deleting a checklist
    ////////////////////////////////////////////////////////////////////////////////////
    """


    def test_e_checklist_new_checklist_flow(self):
        """Test manage checklist ad new checklist"""
        driver = self.driver
        wait = WebDriverWait(driver, 10)
        input = wait.until(EC.visibility_of_element_located((By.PARTIAL_LINK_TEXT, "Checklist options")))
        input.click()
        input = wait.until(EC.visibility_of_element_located((By.ID, "checklist-summary")))
        input.click()
        input = wait.until(EC.visibility_of_element_located((By.ID, "add-new-checklist")))
        input.click()
        checklistType = driver.find_element_by_name("checklistType")
        checklistDescription = driver.find_element_by_name("checklistDescription")
        checklistType.send_keys("selenium-stored-checklist")
        checklistDescription.send_keys("selenium-stored-checklist")
        input = wait.until(EC.visibility_of_element_located((By.ID, "store-checklist")))
        input.click()
        time.sleep(2)
        assert "selenium-stored-checklist" in driver.page_source
    

    def test_f_checklist_delete_checklist_flow(self):
        """Test manage checklist delete item"""
        driver = self.driver
        wait = WebDriverWait(driver, 10)     
        input = wait.until(EC.visibility_of_element_located((By.PARTIAL_LINK_TEXT, "Checklist options")))
        input.click()
        input = wait.until(EC.visibility_of_element_located((By.ID, "checklist-summary")))
        input.click()
        input = wait.until(EC.element_to_be_clickable((By.ID, 'delete-checklist1')))
        input.click()
        time.sleep(2)        
        delete = driver.find_element_by_name("delete")
        delete.send_keys("DELETE")
        input = wait.until(EC.visibility_of_element_located((By.ID, "delete-checklist-finalized")))
        input.click()
        time.sleep(2)
        assert "filled-checklist-for-testing" not in driver.page_source


    """
    ////////////////////////////////////////////////////////////////////////////////////
    Test creating/deleting/updating checklist items
    ////////////////////////////////////////////////////////////////////////////////////
    """


    def test_g_test_back_button_create_checklist_items(self):
        """Test manage checklist create new item's back button"""
        driver = self.driver
        wait = WebDriverWait(driver, 10)
        input = wait.until(EC.visibility_of_element_located((By.PARTIAL_LINK_TEXT, "Checklist options")))
        input.click()
        input = wait.until(EC.visibility_of_element_located((By.ID, "checklist-summary")))
        input.click()
        input = wait.until(EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT, "empty-checklist-for-testing")))
        input.click()
        input = wait.until(EC.visibility_of_element_located((By.ID, "checklist-add-new-icon")))
        input.click()
        input = wait.until(EC.visibility_of_element_located((By.ID, "back-button")))
        input.click()
        time.sleep(2)
        assert "Manage your checklists!" in driver.page_source


    def test_h_create_new_checklist_item_flow(self):
        """Test manage checklist create new checklist item"""
        driver = self.driver
        wait = WebDriverWait(driver, 10)
        input = wait.until(EC.visibility_of_element_located((By.PARTIAL_LINK_TEXT, "Checklist options")))
        input.click()
        input = wait.until(EC.visibility_of_element_located((By.ID, "checklist-summary")))
        input.click()
        input = wait.until(EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT, "empty-checklist-for-testing")))
        input.click()
        input = wait.until(EC.visibility_of_element_located((By.ID, "checklist-add-new-icon")))
        input.click()
        input = wait.until(EC.visibility_of_element_located((By.ID, "add-new-checklist-item")))
        input.click()
        wait.until(EC.visibility_of_element_located((By.ID, "insert-new-checklist-item")))
        checklistID = driver.find_element_by_name("checklistID")
        checklistID.send_keys("1.1")
        content = driver.find_element_by_name("content")
        content.send_keys("Control content")       
        input = wait.until(EC.visibility_of_element_located((By.ID, "select-knowledge-base-item")))
        input.click()
        time.sleep(1)
        input = driver.find_element_by_xpath("//*[contains(text(),'test title kb item 1')]")
        input.click()
        input = wait.until(EC.visibility_of_element_located((By.ID, "select-question-pre-id")))
        input.click()
        time.sleep(1)
        input = driver.find_element_by_xpath("//*[contains(text(),'test-question-pre')]")
        input.click()
        input = wait.until(EC.visibility_of_element_located((By.ID, "select-question-sprint-id")))
        input.click()
        time.sleep(1)
        input = driver.find_element_by_xpath("//*[contains(text(),'test-question-sprint')]")
        input.click()
        select = Select(driver.find_element_by_id('select-include-first'))
        select.select_by_visible_text('true')
        select = Select(driver.find_element_by_id('select-include-always'))
        select.select_by_visible_text('true')
        input = wait.until(EC.visibility_of_element_located((By.ID, "insert-new-checklist-item")))
        input.click()
        input = wait.until(EC.visibility_of_element_located((By.PARTIAL_LINK_TEXT, "Checklist options")))
        time.sleep(2)
        assert "Control content" in driver.page_source


    def test_i_update__checklist_item_flow(self):
        """Test manage checklist update checklist item"""
        driver = self.driver
        wait = WebDriverWait(driver, 10)
        input = wait.until(EC.visibility_of_element_located((By.PARTIAL_LINK_TEXT, "Checklist options")))
        input.click()
        input = wait.until(EC.visibility_of_element_located((By.ID, "checklist-summary")))
        input.click()
        input = wait.until(EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT, "filled-checklist-for-testing")))
        input.click()
        input = wait.until(EC.visibility_of_element_located((By.ID, "checklist-add-new-icon")))
        input.click()
        input = wait.until(EC.visibility_of_element_located((By.PARTIAL_LINK_TEXT, "1.1")))
        input.click()
        input = wait.until(EC.visibility_of_element_located((By.ID, "edit-checklist-item-content")))
        input.click()
        time.sleep(5)
        content = driver.find_element_by_name("content")
        content.clear()
        content.send_keys("Updated control content")
        input = wait.until(EC.visibility_of_element_located((By.ID, "update-checklist-control")))
        input.click()
        time.sleep(2)
        assert "Updated control content" in driver.page_source
    

    def test_j_delete__checklist_item_flow(self):
        """Test manage checklist delete checklist item"""
        driver = self.driver
        wait = WebDriverWait(driver, 10)
        input = wait.until(EC.visibility_of_element_located((By.PARTIAL_LINK_TEXT, "Checklist options")))
        input.click()
        input = wait.until(EC.visibility_of_element_located((By.ID, "checklist-summary")))
        input.click()
        input = wait.until(EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT, "filled-checklist-for-testing")))
        input.click()
        input = wait.until(EC.visibility_of_element_located((By.ID, "checklist-add-new-icon")))
        input.click()
        input = wait.until(EC.visibility_of_element_located((By.PARTIAL_LINK_TEXT, "1.1")))
        input.click()
        input = wait.until(EC.visibility_of_element_located((By.ID, "edit-checklist-item-content")))
        input.click()
        time.sleep(3)
        input = wait.until(EC.visibility_of_element_located((By.ID, "show-delete-modal")))
        input.click()
        delete = driver.find_element_by_name("delete")
        delete.send_keys("DELETE")
        input = wait.until(EC.visibility_of_element_located((By.ID, "delete-checklist-item-finalized")))
        input.click()
        time.sleep(2)
        assert "Updated control content" not in driver.page_source
      

    """
    ////////////////////////////////////////////////////////////////////////////////////
    Test creating/deleting/updating pre-development questions
    ////////////////////////////////////////////////////////////////////////////////////
    """


    def test_k_add__pre_question_flow(self):
        """Test manage checklist add new pre question"""
        driver = self.driver
        wait = WebDriverWait(driver, 10)
        input = wait.until(EC.visibility_of_element_located((By.PARTIAL_LINK_TEXT, "Checklist options")))
        input.click()
        input = wait.until(EC.visibility_of_element_located((By.ID, "checklist-summary")))
        input.click()
        input = wait.until(EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT, "empty-checklist-for-testing")))
        input.click()
        input = wait.until(EC.visibility_of_element_located((By.ID, "questionnaire-pre-icon")))
        input.click()
        input = wait.until(EC.visibility_of_element_located((By.ID, "add-question-modal")))
        input.click()
        content = driver.find_element_by_name("questionName")
        content.send_keys("selenium-added-question")
        input = wait.until(EC.visibility_of_element_located((By.ID, "add-new-question")))
        input.click()
        time.sleep(2)
        Select(driver.find_element_by_id('select-question'))
        time.sleep(2)
        assert "selenium-added-question" in driver.page_source
    

    def test_l_update__pre_question_flow(self):
        """Test manage checklist update pre question"""
        driver = self.driver
        wait = WebDriverWait(driver, 10)
        input = wait.until(EC.visibility_of_element_located((By.PARTIAL_LINK_TEXT, "Checklist options")))
        input.click()
        input = wait.until(EC.visibility_of_element_located((By.ID, "checklist-summary")))
        input.click()
        input = wait.until(EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT, "filled-checklist-for-testing")))
        input.click()
        input = wait.until(EC.visibility_of_element_located((By.ID, "questionnaire-pre-icon")))
        input.click()
        time.sleep(2)
        select = Select(driver.find_element_by_id('select-question'))
        select.select_by_visible_text('test-question-pre')
        input = wait.until(EC.visibility_of_element_located((By.ID, "update-question-modal")))
        input.click()
        content = driver.find_element_by_name("questionName")
        content.send_keys("selenium-updated-question")
        input = wait.until(EC.visibility_of_element_located((By.ID, "update-question")))
        input.click()
        time.sleep(2)
        Select(driver.find_element_by_id('select-question'))
        time.sleep(2)
        assert "selenium-updated-question" in driver.page_source
    

    def test_m_delete__pre_question_flow(self):
        """Test manage checklist delete pre question"""
        driver = self.driver
        wait = WebDriverWait(driver, 10)
        input = wait.until(EC.visibility_of_element_located((By.PARTIAL_LINK_TEXT, "Checklist options")))
        input.click()
        input = wait.until(EC.visibility_of_element_located((By.ID, "checklist-summary")))
        input.click()
        input = wait.until(EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT, "filled-checklist-for-testing")))
        input.click()
        input = wait.until(EC.visibility_of_element_located((By.ID, "questionnaire-pre-icon")))
        input.click()
        time.sleep(2)
        select = Select(driver.find_element_by_id('select-question'))
        time.sleep(2)
        select.select_by_visible_text('test-question-pre')
        input = wait.until(EC.visibility_of_element_located((By.ID, "delete-question-modal")))
        input.click()
        time.sleep(2)
        content = driver.find_element_by_name("delete")
        content.send_keys("DELETE")
        input = wait.until(EC.visibility_of_element_located((By.ID, "delete-question")))
        input.click()
        time.sleep(2)
        assert "test-question-pre" not in driver.page_source  


    """
    ////////////////////////////////////////////////////////////////////////////////////
    Test correlating controls to pre-development questions
    ////////////////////////////////////////////////////////////////////////////////////
    """


    def test_n_correlate__pre_question_flow(self):
        """Test manage checklist correlate pre question"""
        driver = self.driver
        wait = WebDriverWait(driver, 10)
        input = wait.until(EC.visibility_of_element_located((By.PARTIAL_LINK_TEXT, "Checklist options")))
        input.click()
        input = wait.until(EC.visibility_of_element_located((By.ID, "checklist-summary")))
        input.click()
        input = wait.until(EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT, "filled-checklist-for-testing")))
        input.click()
        input = wait.until(EC.visibility_of_element_located((By.ID, "questionnaire-pre-icon")))
        input.click()
        time.sleep(2)
        select = Select(driver.find_element_by_id('select-question'))
        select.select_by_visible_text('test-question-pre')
        time.sleep(2)
        input = driver.find_element_by_xpath("//*[contains(text(), '1.1')]")
        input.click()
        time.sleep(20)
        compare = wait.until(EC.visibility_of_element_located((By.ID, "checklist-correlated0"))).text
        print(compare)
        assert "1.4" in compare


    def test_o_test__pre_question_back_button(self):
        """Test manage checklist pre question back button"""
        driver = self.driver
        wait = WebDriverWait(driver, 10)
        input = wait.until(EC.visibility_of_element_located((By.PARTIAL_LINK_TEXT, "Checklist options")))
        input.click()
        input = wait.until(EC.visibility_of_element_located((By.ID, "checklist-summary")))
        input.click()
        input = wait.until(EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT, "empty-checklist-for-testing")))
        input.click()
        input = wait.until(EC.visibility_of_element_located((By.ID, "questionnaire-pre-icon")))
        input.click()
        input = wait.until(EC.visibility_of_element_located((By.ID, "back-button")))
        input.click()
        time.sleep(2)
        assert "Manage your checklists!" in driver.page_source


    """
    ////////////////////////////////////////////////////////////////////////////////////
    Test creating/deleting/updating post-development questions
    ////////////////////////////////////////////////////////////////////////////////////
    """


    def test_p_add__sprint_question_flow(self):
        """Test manage checklist add new sprint question"""
        driver = self.driver
        wait = WebDriverWait(driver, 10)
        input = wait.until(EC.visibility_of_element_located((By.PARTIAL_LINK_TEXT, "Checklist options")))
        input.click()
        input = wait.until(EC.visibility_of_element_located((By.ID, "checklist-summary")))
        input.click()
        input = wait.until(EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT, "empty-checklist-for-testing")))
        input.click()
        input = wait.until(EC.visibility_of_element_located((By.ID, "questionnaire-sprint-icon")))
        input.click()
        input = wait.until(EC.visibility_of_element_located((By.ID, "add-question-modal")))
        input.click()
        content = driver.find_element_by_name("questionName")
        content.send_keys("selenium-added-question")
        input = wait.until(EC.visibility_of_element_located((By.ID, "add-new-question")))
        input.click()
        time.sleep(2)
        Select(driver.find_element_by_id('select-question'))
        time.sleep(2)
        assert "selenium-added-question" in driver.page_source


    def test_q_update__sprint_question_flow(self):
        """Test manage checklist update sprint question"""
        driver = self.driver
        wait = WebDriverWait(driver, 10)
        input = wait.until(EC.visibility_of_element_located((By.PARTIAL_LINK_TEXT, "Checklist options")))
        input.click()
        input = wait.until(EC.visibility_of_element_located((By.ID, "checklist-summary")))
        input.click()
        input = wait.until(EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT, "filled-checklist-for-testing")))
        input.click()
        input = wait.until(EC.visibility_of_element_located((By.ID, "questionnaire-sprint-icon")))
        input.click()
        time.sleep(2)
        select = Select(driver.find_element_by_id('select-question'))
        select.select_by_visible_text('test-question-sprint')
        input = wait.until(EC.visibility_of_element_located((By.ID, "update-question-modal")))
        input.click()
        content = driver.find_element_by_name("questionName")
        content.send_keys("selenium-updated-question")
        input = wait.until(EC.visibility_of_element_located((By.ID, "update-question")))
        input.click()
        time.sleep(2)
        Select(driver.find_element_by_id('select-question'))
        time.sleep(2)
        assert "selenium-updated-question" in driver.page_source


    def test_r_delete__sprint_question_flow(self):
        """Test manage checklist delete sprint question"""
        driver = self.driver
        wait = WebDriverWait(driver, 10)
        input = wait.until(EC.visibility_of_element_located((By.PARTIAL_LINK_TEXT, "Checklist options")))
        input.click()
        input = wait.until(EC.visibility_of_element_located((By.ID, "checklist-summary")))
        input.click()
        input = wait.until(EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT, "empty-checklist-for-testing")))
        input.click()
        input = wait.until(EC.visibility_of_element_located((By.ID, "questionnaire-sprint-icon")))
        input.click()
        time.sleep(2)
        select = Select(driver.find_element_by_id('select-question'))
        select.select_by_visible_text('test-question-sprint')
        input = wait.until(EC.visibility_of_element_located((By.ID, "delete-question-modal")))
        input.click()
        time.sleep(2)
        content = driver.find_element_by_name("delete")
        content.send_keys("DELETE")
        input = wait.until(EC.visibility_of_element_located((By.ID, "delete-question")))
        input.click()
        time.sleep(2)
        assert "test-question-sprint" not in driver.page_source  

    
    """
    ////////////////////////////////////////////////////////////////////////////////////
    Test correlating controls to post-development questions
    ////////////////////////////////////////////////////////////////////////////////////
    """   


    def test_s_correlate__sprint_question_flow(self):
        """Test manage checklist correlate sprint question"""
        driver = self.driver
        wait = WebDriverWait(driver, 10)
        input = wait.until(EC.visibility_of_element_located((By.PARTIAL_LINK_TEXT, "Checklist options")))
        input.click()
        input = wait.until(EC.visibility_of_element_located((By.ID, "checklist-summary")))
        input.click()
        input = wait.until(EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT, "filled-checklist-for-testing")))
        input.click()
        input = wait.until(EC.visibility_of_element_located((By.ID, "questionnaire-sprint-icon")))
        input.click()
        time.sleep(2)
        select = Select(driver.find_element_by_id('select-question'))
        select.select_by_visible_text('test-question-sprint')
        time.sleep(2)
        input = driver.find_element_by_xpath("//*[contains(text(), '1.1')]")
        input.click()
        time.sleep(2)
        compare = wait.until(EC.visibility_of_element_located((By.ID, "checklist-correlated0"))).text
        assert "1.1" in compare


    def test_t_test__sprint_question_back_button(self):
        """Test manage checklist sprint question back button"""
        driver = self.driver
        wait = WebDriverWait(driver, 10)
        input = wait.until(EC.visibility_of_element_located((By.PARTIAL_LINK_TEXT, "Checklist options")))
        input.click()
        input = wait.until(EC.visibility_of_element_located((By.ID, "checklist-summary")))
        input.click()
        input = wait.until(EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT, "empty-checklist-for-testing")))
        input.click()
        input = wait.until(EC.visibility_of_element_located((By.ID, "questionnaire-sprint-icon")))
        input.click()
        input = wait.until(EC.visibility_of_element_located((By.ID, "back-button")))
        input.click()
        time.sleep(2)
        assert "Manage your checklists!" in driver.page_source


    @classmethod
    def tearDown(self):
        self.driver.close()


if __name__ == '__main__':
    unittest.main()

    
