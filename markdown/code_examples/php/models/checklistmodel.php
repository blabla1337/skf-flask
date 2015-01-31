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

 require_once("helpclasses/class.getid.php");

class ChecklistModel extends Model{
	
	
	private $_answer;
	private $_projectID;
	private $_userID;
	private $_vulnID;
	private $_questionID;
	private $_listAnswer;
	

	public function setAnswer($answer){
	$this->_answer = $answer;
	
	}
	
	public function setQuestionID($questionID){
	$this->_questionID = $questionID;
	
	}
	
	public function setVulnID($vulnID){
		$this->_vulnID = $vulnID;
	}
	
	public function setProjectID($projectID){
		$this->_projectID = $projectID;
	}
	
	public function setUserID($userID){
		$this->_userID = $userID;
	}
	
	public function setListAnswer($listAnswer){
		$this->_listAnswer = $listAnswer;
	}
	public function setListName($listName){
		$this->_listName = $listName;
	}
	
	
	
	public function checklistShow(){
		
		$sql = "SELECT * FROM checklists WHERE listName=:name";
		$this->_setParam(array(":name" => $this -> _listName));
		$this->_setSql($sql);
		
		$list = $this->getAll($sql);
		
			if (empty($list)){
				return false;
			}

		return $list; 
		
	}
	
		public function checklistResults(){
		
		$sql = "SELECT * FROM questions  GROUP BY listName";
		$this->_setParam(array(":id" => $_SESSION['userID']));
		$this->_setSql($sql);
		
		$result = $this->getAll($sql);
		
			if (empty($result)){
				return false;
			}

		return $result; 
		
	}
	
	
	public function checklistSum(){
		
		$sql = "SELECT * FROM checklists GROUP BY listName";
	
		$this->_setSql($sql);
		
		$list = $this->getAll($sql);
		
			if (empty($list)){
				return false;
			}

		return $list; 
		
	}
	
	
	public function storeChecklist(){
	
			$sql = "INSERT INTO questionlist 
			(answer, projectID, questionID, userID, vulnID, listName)
 			VALUES 
 			(?, ?, ?, ?, ?, ?)";
		
		$data = array(
			$this->_answer,
			$this->_projectID,
			$this->_questionID,
			$_SESSION['userID'],
			$this->_vulnID,
			$this->_listAnswer
			

		);
			$sth = $this->_db->prepare($sql);
			
			return $sth->execute($data);		
	}
	

	public function deleter($function){
		
		$id = $_SESSION['userID'];
		
		$sql = "DELETE FROM questionlist where entryDate=:name  AND userID=:id";
	
		$this->_setSql($sql);
		$this->_setParam(array(":name" => $function, ":id" => $id));

		$parameters = $this->editRow($sql);
		
			if (empty($parameters)){
				return false;
			}
		
		return $parameters; 
			
	}
				

	
    
    public function getResults(){
		$id = $_SESSION['userID'];
        $sql = "
                    
		SELECT q.answer,
		q.projectID,
		q.questionID,
		q.userID,
		q.vulnID,
		q.listName,
		q.entryDate,
		p.projectName,
		p.projectVersion,
		p.projectDesc,
		p.userID

		FROM questionlist as q

		JOIN projects as p
		ON q.projectID = p.projectID


		WHERE p.userID=:id GROUP BY q.listName, q.entryDate ORDER BY p.projectName ASC                 
                ";
         
        $this->_setSql($sql);
        $this->_setParam(array(":id" => $id));
        $result = $this->getAll();
        
        if (empty($result))
        {
        
            return false;

        }
         
        return $result;
    }
        
        
        
   public function getProjectID($page){
	   $show = new getID();
       $result = $show ->projectID($page);
        
	   return $result;
	}
	
	

}
