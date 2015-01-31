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

class ChecklistPdfModel extends Model{
	
	
		
	public function getContent($date){
		
		$id = $_SESSION['userID'];
		$sql = "
                    
		SELECT
		q.answer,
		q.projectID,
		q.questionID,
		q.userID,
		q.vulnID,
		q.listName,
		q.entryDate,
		v.question,
		v.head,
		vuln.vulnName,
		vuln.vulnDesc,
		vuln.vulnSol,
		vuln.".$_SESSION['ref']." as tech,
		p.projectName,
		p.projectVersion,
		p.projectDesc

		FROM questionlist as q

		JOIN projects as p
		ON q.projectID = p.projectID

		JOIN checklists as v
		ON q.questionID = v.questionID

		JOIN vulnerabilities as vuln
		ON q.vulnID = vuln.vulnID


		WHERE q.answer='no'  AND q.userID=:id AND q.entryDate=:date  ";
	
		$this->_setSql($sql);
		$this->_setParam(array(":date" => $date, ":id" => $id));
		
		$project = $this->getAll($sql);
		
			if (empty($project)){

				return false;
			}

		return $project; 
			
	}
	


}