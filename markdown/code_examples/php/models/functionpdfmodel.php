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

class FunctionPdfModel extends Model{
	
	
		
	public function getContent($projectID){
		
		$id = $_SESSION['userID'];
		
		$sql = "
			SELECT 

			p.paramID,
			p.functionName,
			p.functionDesc,
			p.tech,
			p.projectID, 
			p.userID, 
			p.techVuln,
			p.entryDate,
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
			vuln.".$_SESSION['ref']." as tech,
			vuln.vulnSol
			

			FROM parameters as p

			JOIN projects as pr
				ON p.projectID = pr.projectID

			JOIN techhacks as t
				ON p.tech = t.techID

			JOIN vulnerabilities as vuln
				ON t.vulnID = vuln.vulnID


			WHERE p.projectID=:projectID AND p.userID=:id GROUP BY vuln.vulnID ";
	
	$this->_setSql($sql);
	$this->_setParam(array(":projectID" => $projectID, ":id" => $id));
		
	$project = $this->getAll($sql);
		
	if (empty($project))
	{

		return false;
	}

		return $project; 
			
	}
	


}
