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

class ChecklistController extends Controller{
	
	public function __construct($model, $action)
	{
		parent::__construct($model, $action);
		$this->_setModel($model);
	}
	
	
	public function summary($projectID){

		try {	 
			// Authentication check
			$this->_checkSession();
			
			$this->_setView('index');
			$this->_view->set('title', 'Security Knowledge Framework:: Checklist summary');
			
		    $checkSum 	  = $this->_model->checklistSum();
		    
			$this->_view->set('checkSum', $checkSum);
			
			$projectIdentifier   = $this->_model->getProjectID($projectID);
			$this->_view->set('projectID', $projectIdentifier);
			
			
			return $this->_view->output();
			 
		} catch (Exception $e) {
			echo "Application error:" . $e->getMessage();
		}
		
	}
	
	
     public function takelist($projectID){
    
    	$this->_checkSession();	
    	    		
        try {
        	
       	 $search = isset($_POST['list']) ? trim($_POST['list']) : NULL;
       

       	 $this->_setView('list');
      	
      	 $results = new ChecklistModel();
	   	 $results->setlistName($search);
       	 $foo = $results->checklistShow();
       
      	  //get identifier for projects again
         $projectIdentifier   = $this->_model->getProjectID($projectID);		
         $this->_view->set('projectID', $projectIdentifier);
         $this->_view->set('checklist', $foo);
         $this->_view->set('title', 'Security Knowledge Framework:: Knowledge Base vulnerabilities');
           
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
			
    	    $foo = $this->_model->getResults();
       
       		$this->_view->set('projectResults', $foo);
         
			return $this->_view->output();
			 
		} catch (Exception $e) {
			echo "Application error:" . $e->getMessage();
		}
		
	}


	 public function checklistInsert($projectID){
       
       // Authentication check
    	$this->_checkSession();
    	 
        if (!isset($_POST['submitList'])){
			header('Location: /login');
			die;
		}
		
		
		// check CSRF token
		$this->_checkCsrf($_POST['token']);
		
		$errors = array();
		$check = true;
		
	//	$listName_ = isset($_POST['listNameAnswer1']) ? trim($_POST['listNameAnswer1']) : NULL;
		
	//	$this ->_model->deleter($listName_);
		
		for($i = 0; $i < 200; $i++){
    		
		$answer 		= isset($_POST['answer'.$i.'']) ? trim($_POST['answer'.$i.'']) : NULL;
		$vulnID 		= isset($_POST['vulnID'.$i.'']) ? trim($_POST['vulnID'.$i.'']) : NULL;
		$questionID 	= isset($_POST['questionID'.$i.'']) ? trim($_POST['questionID'.$i.'']) : NULL;
		$listNameAnswer = isset($_POST['listNameAnswer'.$i.'']) ? trim($_POST['listNameAnswer'.$i.'']) : NULL;
	
	
        if (!$check){
            $this->_setView('list');
            $this->_view->set('title', 'Security Knowledge Framework:: Invalid form data!');
            $this->_view->set('menuActiveProject', "class='active'");
            $this->_view->set('menuActiveProjectNew', "class='active'");
			$this->_view->set('errors', $errors);
			$this->_view->set('formData', $_POST);
			return $this->_view->output();
		}
			
		try {
			$function = new ChecklistModel();
			$function->setAnswer($answer);
			$function->setvulnID($vulnID);
			$function->setquestionID($questionID);
		    $function->setProjectID($projectID);
		    $function->setListAnswer($listNameAnswer);
			$function->storeChecklist();			

						
			$this->_setView('succes');
			$options  = $this->_model->getProjectID($projectID);
			$this->_view->set('option', $options);
			$this->_view->set('title', 'Security Knowledge Framework::  Function is stored!');
			$this->_view->set('menuActiveProject', "class='active'");
			$this->_view->set('menuActiveProjectNew', "class='active'");					
					
		} catch (Exception $e){
		  
            $this->_setView('list');
            $options  = $this->_model->getProjectID($projectID);
			$this->_view->set('option', $options);
            $this->_view->set('title', 'Security Knowledge Framework:: There was an error saving the data!');
            $this->_view->set('formData', $_POST);
			$this->_view->set('saveError', $e->getMessage());
		}
       }//end for
       
       	$this->_setView('succes');
       	$options  = $this->_model->getProjectID($projectID);
		$this->_view->set('option', $options);
       	$this->_view->set('title', 'Security Knowledge Framework:: Checklist was stored succesfull!');
        return $this->_view->output();      
  }
	
	
	public function deleteList($projectID){

		try {	 
			// Authentication check
			$this->_checkSession();
			
			$this->_setView('succesDel');
			$this->_view->set('title', 'Security Knowledge Framework:: Deleted');
				
			$this->_model->deleter($projectID);
			
			
			return $this->_view->output();
			 
		} catch (Exception $e) {
			echo "Application error:" . $e->getMessage();
		}
		
	}
	
	
}
