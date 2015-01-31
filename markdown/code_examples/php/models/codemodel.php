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

class codeModel extends Model{
	
	
	private $_search;
	
	public function setSearch($search){
		$this->_search = $search;
	}
	
	
	public function getCodeExample(){
		
		$sql = "SELECT * FROM code_example where lang=:lang";
	
		$this->_setSql($sql);
		$this->_setParam(array(":lang" => $_SESSION['ref']));
		
		$project = $this->getAll($sql);
		
		if (empty($project)){
			return false;
			
		}

		return $project; 
		
	}
	
	
	
	public function searchValue(){
	
        $sql = "SELECT
                    *
                FROM
                    code_example
                WHERE lang=:lang AND codeName LIKE CONCAT('%', :search, '%')";
         
		$this->_setSql($sql);
		$this->_setParam(array(":lang" => $_SESSION['ref'], ":search" => $this->_search));
		
		$project = $this->getAll($sql);
		
		if (empty($project)){
			return false;
			
		}

		return $project; 
		
	}
	
	
}
