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

class ProjectModel extends Model{
	
	private $_projectName;
	private $_projectVersion;
	private $_projectDescription;
	
	public function setProjectName($projectname){
		$this->_projectName = $projectname;
	}
	
	public function setProjectVersion($version){
		$this->_projectVersion = $version;
	}
	
	public function setProjectDescription($description){
		$this->_projectDescription = $description;
	}
	

	
	public function getProjects(){
		
		$sql = "SELECT * FROM projects where userID=:id";
		
		$this->_setSql($sql);
		$this->_setParam(array(":id" => $_SESSION['userID']));
		
		$userProjects = $this->getAll($sql);
		
		if (empty($userProjects)){
			return false;
		}
		return $userProjects;
	}
	
	
	public function deleter($projectID){
		
		$id = $_SESSION['userID'];
		
		$sql = "DELETE FROM projects where projectID=:id AND userID=:userid ";
	
		$this->_setSql($sql);
		$this->_setParam(array(":id" => $projectID, ":userid" => $id));

		$parameters = $this->editRow($sql);
		
		if (empty($parameters)){
			return false;
			
		}
		return $parameters; 

				
	} 

	
	public function storeProject(){
		
		session_start();
		
		$sql = "INSERT INTO projects 
					(projectName, projectVersion, projectDesc, userID)
 				VALUES 
 					(?, ?, ?, ?)";
		
		$data = array(
			$this->_projectName,
			$this->_projectVersion,
			$this->_projectDescription,
			$_SESSION['userID']
		
		);
		
		$sth = $this->_db->prepare($sql);
		return $sth->execute($data);
	}
	
	
	
	
}