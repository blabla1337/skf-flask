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
 
class KnowledgeController extends Controller
{
    public function __construct($model, $action)
    {
        parent::__construct($model, $action);
        $this->_setModel($model);
    }
     
    public function index()
    {
        try {
        	
        	// Authentication check        	         	     
            $this->_checkSession();
            $vulnerabilities = $this->_model->getKnowledgeBase();
            $this->_view->set('vulnerabilities', $vulnerabilities);
            $this->_view->set('menuActiveKnowledge', "class='active'");
            $this->_view->set('title', 'Security Knowledge Framework:: Knowledge Base vulnerabilities');
             
            return $this->_view->output();
             
        } catch (Exception $e) {
            echo "Application error:" . $e->getMessage();
        }
    }
     
    // Add THIS
    public function details($vulnerabilityId)
    {
        try {
             
        	// Authentication check
        	$this->_checkSession();
            $vulnerability = $this->_model->getVulnerabilityById((int)$vulnerabilityId);
             
            if ($vulnerability)
            {
                $this->_view->set('vulnName', $vulnerability['vulnName']);
                $this->_view->set('vulnDesc', $vulnerability['vulnDesc']);
                $this->_view->set('vulnSol', $vulnerability['vulnSol']);
            }
            else
            {
                $this->_view->set('title', 'Invalid vulnerability ID');
                $this->_view->set('noVulnerability', true);
            }
             
            return $this->_view->output();
              
        } catch (Exception $e) {
            echo "Application error:" . $e->getMessage();
        }
    }
    // End


     public function search(){
        try {
        	
       $this->_checkSession();	
       $search = isset($_POST['search']) ? trim($_POST['search']) : NULL;
       

       $this->_setView('search');
      	
       $results = new KnowledgeModel();
	   $results->setSearch($search);
       $foo = $results->searchValue();
       
       $this->_view->set('vulnerabilities', $foo);
       $this->_view->set('title', 'Security Knowledge Framework:: Knowledge Base vulnerabilities');
           
       return $this->_view->output();
             
        } catch (Exception $e) {
            echo "Application error:" . $e->getMessage();
        }
    }


    

}