<?php

# Copyright 2014 Riccardo ten Cate
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

class ProjectController extends Controller{
	
	public function __construct($model, $action)
	{
		parent::__construct($model, $action);
		$this->_setModel($model);
	}
	
	public function index(){

		try {	 
			// Authentication check
			$this->_checkSession();
			$projects = $this->_model->getProjects();
			$this->_view->set('projects', $projects);
			$this->_view->set('menuActiveProject', "class='active'");
			$this->_view->set('menuActiveProjectList', "class='active'");
			$this->_view->set('title', 'Security Knowledge Framework:: Overview of past projects');
			 
			return $this->_view->output();
			 
		} catch (Exception $e) {
			echo "Application error:" . $e->getMessage();
		}
		
	}

	public function newproject(){

		try {
			// Authentication check
			$this->_checkSession();
				
			$this->_view->set('menuActiveProject', "class='active'");
			$this->_view->set('menuActiveProjectNew', "class='active'");
			$this->_view->set('title', 'Security Knowledge Framework:: Create new project');
	
			return $this->_view->output();
	
		} catch (Exception $e) {
			echo "Application error:" . $e->getMessage();
		}
	
	}
	
		public function projectDelete($projectID){

		try {
			// Authentication check
			$this->_checkSession();
			$this ->_model->deleter($projectID);
			$this->_view->set('menuActiveProject', "class='active'");
			$this->_view->set('menuActiveProjectNew', "class='active'");
			$this->_view->set('title', 'Security Knowledge Framework:: Create new project');
		    $this->_setView('succesDel');
		    
		    $projects = $this->_model->getProjects();
			$this->_view->set('projects', $projects);
			return $this->_view->output();
	
		} catch (Exception $e) {
			echo "Application error:" . $e->getMessage();
		}
	
	}
	
    public function step1(){

    	// Authentication check
    	$this->_checkSession();
    	 
        if (!isset($_POST['projectFormSubmit'])){
			header('Location: /project/newproject');
		}
		
		// check CSRF token
		$this->_checkCsrf($_POST['token']);
		
		$errors = array();
		$check = true;
			
		$inputDesc = isset($_POST['inputDesc']) ? trim($_POST['inputDesc']) : NULL;
		$inputName = isset($_POST['inputName']) ? trim($_POST['inputName']) : NULL;
		$inputVersion = isset($_POST['inputVersion']) ? trim($_POST['inputVersion']) : NULL;
			
		if (empty($inputName)){
			$check = false;
			array_push($errors, "Project name is required!");
		}
			
		if (empty($inputVersion)){
			$check = false;
			array_push($errors, "Version is required!");
		}

        if (!$check){
            $this->_setView('newproject');
            $this->_view->set('title', 'Security Knowledge Framework:: Invalid form data!');
            $this->_view->set('menuActiveProject', "class='active'");
            $this->_view->set('menuActiveProjectNew', "class='active'");
			$this->_view->set('errors', $errors);
			$this->_view->set('formData', $_POST);
			return $this->_view->output();
		}
			
		try {
					
			$project = new ProjectModel();
			$project->setProjectDescription($inputDesc);
			$project->setProjectName($inputName);
			$project->setProjectVersion($inputVersion);
			$project->storeProject();
					
			$this->_setView('success');
			$this->_view->set('title', 'Security Knowledge Framework::  Project is stored!');
			$this->_view->set('menuActiveProject', "class='active'");
			$this->_view->set('menuActiveProjectNew', "class='active'");					
					
		} catch (Exception $e){
            $this->_setView('newproject');
            $this->_view->set('title', 'Security Knowledge Framework:: There was an error saving the data!');
            $this->_view->set('menuActiveProject', "class='active'");
            $this->_view->set('menuActiveProjectNew', "class='active'");
            $this->_view->set('formData', $_POST);
			$this->_view->set('saveError', $e->getMessage());
		}

        return $this->_view->output();
    }
    

    
}