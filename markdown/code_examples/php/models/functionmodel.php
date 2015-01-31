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

class FunctionModel extends Model{
	
	
    private $_parameter;
	private $_functionName;
	private $_functionDesc;
	private $_tech;
	private $_projectID;
	private $userID;

	
	
	public function setParameterName($parametername){
		$this->_parameterName = $parametername;
	}
	
	public function setFunctionName($functionname){
	$this->_functionName = $functionname;
	}
	
	public function setFunctionDesc($functiondesc){
		$this->_functionDesc = $functiondesc;
	}
	
	public function setTech($tech){
		$this->_tech = $tech;
	}
	
	public function setProjectID($projectID){
		$this->_projectID = $projectID;
	}
	
	public function setUserID($userID){
		$this->_userID = $userID;
	}
		
		
	
	public function getFunction($projectID){
		
		$id = $_SESSION['userID'];
		
		$sql = "SELECT 

			p.paramID,
			p.functionName,
			p.functionDesc,
			p.tech,
			p.projectID, 
			p.entryDate,
			p.userID, 
			p.techVuln,
			pr.projectID,
			pr.projectName,
			pr.projectVersion,
			pr.projectDesc,
			pr.timestamp,
			t.techID,
			t.techName,
			t.vulnID,
			vuln.vulnName,
			vuln.vulnDesc,
			vuln.vulnSol
		

			FROM parameters as p

			JOIN projects as pr
				ON p.projectID = pr.projectID

			JOIN techhacks as t
				ON p.tech = t.techID

			JOIN vulnerabilities as vuln
				ON t.vulnID = vuln.vulnID


			WHERE p.projectID=:projectID AND p.userID=:id group by p.tech ";
	
		$this->_setSql($sql);
		$this->_setParam(array(":projectID" => $projectID, ":id" => $id));
		
		$parameters = $this->getAll($sql);
		
		if (empty($parameters)){
			return false;
			
		}
		return $parameters; 
		
	}
	
	
	public function deleter($function){
		
		$id = $_SESSION['userID'];
		
		$sql = "DELETE FROM parameters where functionName=:name  AND userID=:id";
	
		$this->_setSql($sql);
		$this->_setParam(array(":name" => $function, ":id" => $id));

		$parameters = $this->editRow($sql);
		
		if (empty($parameters)){
			return false;
			
		}
		return $parameters; 

				
	}
	
	
	public function getTechniques(){
		
		$sql = "SELECT * FROM techhacks ";
		$this->_setSql($sql);
		
		$techhacks = $this->getAll($sql);
		
		if (empty($techhacks)){
			return false;
			
		}
		return $techhacks; 
		
	}
	
    public function getResults()
    {
    
    	$id = $_SESSION['userID'];

        $sql = "
        
        SELECT p.projectName, p.projectID, p.projectDesc, p.projectVersion, p.userID,
        par.paramID, par.functionName, par.tech, par.projectID, par.userID 
        
        from projects as p 
        
        join
        
        parameters as par
        on 
        p.projectID = par.projectID
         
         
         WHERE p.userID=:id GROUP BY p.projectVersion
                  
                ";
         
        $this->_setSql($sql);
        $this->_setParam(array( ":id" => $id));
        $searchResult = $this->getAll();
        
        if (empty($searchResult))
        {
            return false;

        }
         
        return $searchResult;
    }
	
	
	public function storeFunction(){
		
		
		$sql = "INSERT INTO parameters 
					(functionName, tech, projectID, userID, functionDesc)
 				VALUES 
 					(?, ?, ?, ?, ?)";
		
		$data = array(
			
			$this->_functionName,
			$this->_tech,
			$this->_projectID,
			$_SESSION['userID'],
			$this->_functionDesc
		);

			$sth = $this->_db->prepare($sql);
		return $sth->execute($data);
		
	
	}
	
	public function getProjectID($page){
	   $show = new getID();
       $result = $show ->projectID($page);
        
	   return $result;
	}
	
	

}