<?php

# Copyright 2014 Riccardo ten Cate

//nog even afmaken

class CoverModelImage extends Model{
	
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
		
		$sql = "DELETE FROM projects where projectID=:id AND userID=".$id." ";
	
		$this->_setSql($sql);
		$this->_setParam(array(":id" => $projectID));

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