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

class ChecklistPdfController extends Controller{
	
	public function __construct($model, $action)
	{
		parent::__construct($model, $action);
		$this->_setModel($model);
	}
	
	public function index(){

		try {	 
			// Authentication check
			$this->_checkSession();

			$this->_view->set('title', 'Security Knowledge Framework:: Edit options');
			 
			return $this->_view->output();
			 
		} catch (Exception $e) {
			echo "Application error:" . $e->getMessage();
		}
		
	}

	
	public function checklists($date){

		try {	 
			// Authentication check
			$this->_checkSession();
			$this->_setView('index');
			
			$options  = $this->_model->getContent($date);
			
			$this->_view->set('func', $options);
			$this->_view->set('title', 'Security Knowledge Framework:: Edit options');
			
				if(!$options){
					$this->_setView('alt');
				}
			
			return $this->_view->output();
			 
		} catch (Exception $e) {
			echo "Application error:" . $e->getMessage();
		}
		
	}
	
 
}