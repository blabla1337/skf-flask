<?php

# Copyright 2014 Riccardo ten Cate


class getID extends Model{

    public function ProjectID($projectID){
		
		$id = $_SESSION['userID'];
		
		$sql = "SELECT * FROM projects where projectID=:projectID AND userID=:userID ";
	
		$this->_setSql($sql);
		$this->_setParam(array(":projectID" => $projectID, ":userID" => $id));
		
		$project = $this->getAll($sql);
		
		if (empty($project)){
			return false;
			
		}

		return $project; 
		
	}

}