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

class codeController extends Controller{
	
	public function __construct($model, $action)
	{
		parent::__construct($model, $action);
		$this->_setModel($model);
	}
	
	
	public function lang($lang){
	
		if($lang != 'php'  &&  $lang != 'java')
		{
	 		die; 
	 		header('location:/login');
		}

		if($lang == 'php')
		{
			session_start();
			$_SESSION['ref'] = 'php';	
			header('location:/dashboard');
		}
		
		if($lang == 'java')
		{
			session_start();
			$_SESSION['ref'] = 'java';	
			header('location:/dashboard');
		}
	}
		
	
	public function examples(){

		try {	 
			// Authentication check
			$this->_checkSession();
			
			$this->_setView('exam');
			$this->_view->set('title', 'Security Knowledge Framework:: PHP code examples');
			
		    $examples   = $this->_model->getCodeExample();
		    
			$this->_view->set('exam', $examples);
						
			return $this->_view->output();
			 
		} catch (Exception $e) {
			echo "Application error:" . $e->getMessage();
		}
		
	}
	
     public function search()
    {
        try {
        	
       $this->_checkSession();	
       $search = isset($_POST['search']) ? trim($_POST['search']) : NULL;
       
	   $this->_setView('search');
          	
       $results = new CodeModel();
	   $results->setSearch($search);
       $foo = $results->searchValue();
       
       $this->_view->set('code', $foo);
       $this->_view->set('title', 'Security Knowledge Framework:: Knowledge Base vulnerabilities');
           
       return $this->_view->output();
             
        } catch (Exception $e) {
            echo "Application error:" . $e->getMessage();
        }
    }
    
    	public function inserter(){

		try {	 
			// Authentication check
			$this->_checkSession();
			
			$this->_setView('foo');
			$this->_view->set('title', 'Security Knowledge Framework:: PHP code examples');
			
		    $examples   = $this->_model->getCodeExample();
		    
			$this->_view->set('exam', $examples);
						
			return $this->_view->output();
			 
		} catch (Exception $e) {
			echo "Application error:" . $e->getMessage();
		}
		
	}
	
	
}
