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

class FunctionController extends Controller{
	
	public function __construct($model, $action){
		parent::__construct($model, $action);
		$this->_setModel($model);
	}
	
	public function index(){
		try {	 
			// Authentication check
			$this->_checkSession();
			$this->_view->set('title', 'Security Knowledge Framework:: Edit options');
	
			return $this->_view->output();
			 
			}catch (Exception $e) {
				echo "Application error:" . $e->getMessage();
			}
		}

	
	
	public function addFunctions($projectID){
		 try {	 
				
			// Authentication check
			               $this->_checkSession();
			$options     = $this->_model->getFunction($projectID);
			$dropdown    = $this->_model->getTechniques();
			$projectid   = $this->_model->getProjectID($projectID);
			$this->_view->set('projectID', $projectid);
			
			$this->_view->set('projects', $options);
			$this->_view->set('dropdown', $dropdown);
			$this->_view->set('title', 'Security Knowledge Framework:: Edit options');
			 
			return $this->_view->output();
			 
			} catch (Exception $e) {
				echo "Application error:" . $e->getMessage();
			}	
	}
	
	
	public function results(){

		try {	 
			// Authentication check
			$this->_checkSession();
			
			$this->_setView('result');
			$this->_view->set('title', 'Security Knowledge Framework:: Checklist summary');
			
		    $result = $this->_model->getResults();
		    
			$this->_view->set('projectResults', $result);
					
			return $this->_view->output();
			 
		} catch (Exception $e) {
			echo "Application error:" . $e->getMessage();
		}
		
	}
	
	
	public function insertFunctions($projectID){
       
       // Authentication check
    	$this->_checkSession();
    	 
        	if (!isset($_POST['submit'])){
				header('Location: /show/addFunctions');
			}
				
		// check CSRF token
		$this->_checkCsrf($_POST['token']);
		
		$errors = array();
		$check = true;
		
			for($i = 0; $i < 100 -1   ; $i++ ){
    		
			$functionName = isset($_POST['functionName']) ? trim($_POST['functionName']) : NULL;
			$functionDesc = isset($_POST['functionDesc']) ? trim($_POST['functionDesc']) : NULL;
			$tech = isset($_POST['tech'.$i.'']) ? trim($_POST['tech'.$i.'']) : NULL;
				
				if (empty($functionDesc)){
					$check = false;
					array_push($errors, "Function description is required!");
				}
		
				if (empty($functionName)){
					$check = false;
					array_push($errors, "Function name is required!");
				}
		
				if (!$check){
			
					$this->_setView('addFunctions');
			
					$options     = $this->_model->getFunction($projectID);
					$dropdown    = $this->_model->getTechniques();
					$projectid   = $this->_model->getProjectID($projectID);
					$this->_view->set('projects', $options);
					$this->_view->set('dropdown', $dropdown);
					$this->_view->set('projectID', $projectid);
			
					$this->_view->set('title', 'Security Knowledge Framework:: Invalid form data!');
					$this->_view->set('menuActiveProject', "class='active'");
					$this->_view->set('menuActiveProjectNew', "class='active'");
					$this->_view->set('errors', $errors);
					$this->_view->set('formData', $_POST);
					return $this->_view->output();
				}
			
			try {

				$function = new FunctionModel();
				$function->setFunctionName($functionName);
				$function->setFunctionDesc($functionDesc);
				$function->setTech($tech);
				$function->setProjectID($projectID);
				$function->storeFunction();
			
				$this->_setView('succes');
				$options  = $this->_model->getProjectID($projectID);
				$this->_view->set('option', $options);
				$this->_view->set('title', 'Security Knowledge Framework::  Function is stored!');
				$this->_view->set('menuActiveProject', "class='active'");
				$this->_view->set('menuActiveProjectNew', "class='active'");					
					
				} catch (Exception $e){
			   // var_dump($e);
					$this->_setView('addFunctions');
					$this->_view->set('title', 'Security Knowledge Framework:: There was an error saving the data!');
					$this->_view->set('formData', $_POST);
					$this->_view->set('saveError', $e->getMessage());
				}
       }//end for
       
    	$this->_setView('succes');
    	$options  = $this->_model->getProjectID($projectID);
		$this->_view->set('option', $options);
    	return $this->_view->output();
        
	}
 
	
	public function deleteFunction($function){

		try {	 
			// Authentication check
			$this->_checkSession();
			$this->_setView('succesDel');
			$this->_model->deleter($function);	
			$this->_view->set('title', 'Security Knowledge Framework:: Edit options');
			
			return $this->_view->output();
			 
			} catch (Exception $e) {
				echo "Application error:" . $e->getMessage();
			}
		
	}
 
}//endclass
