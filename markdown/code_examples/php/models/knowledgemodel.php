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
 
class KnowledgeModel extends Model
{
	
	private $_search;
	
	public function setSearch($search){
		$this->_search = $search;
	}
	
	
    public function getKnowledgeBase()
    {
        $sql = "SELECT
                    *
                FROM
                    vulnerabilities
                ORDER BY vulnID ASC";
         
        $this->_setSql($sql);
        $vulnDetails = $this->getAll();
         
        if (empty($vulnDetails))
        {
            return false;
        }
         
        return $vulnDetails;
    }
     
    public function getVulnerabilityById($id)
    {
        $sql = "SELECT
                    *
                FROM
                    vulnerabilities
                WHERE
                    vulnID = :id";
         
        $this->_setSql($sql);
        $this->_setParam(array(":id" => $id));
        
        $vulnDetails = $this->getRow($sql);
         
        if (empty($vulnDetails))
        {
            return false;
        }
         
        return $vulnDetails;
    }
    
    
    public function searchValue()
    {
        $sql = "SELECT
                    *
                FROM
                    vulnerabilities
                WHERE vulnName LIKE CONCAT('%', :search, '%')";
         
        $this->_setSql($sql);
        $this->_setParam(array(":search" => $this->_search));
        
        $search = $this->getRow($sql);
        
        if (empty($search))
        {
            return false;
        }
         
        return $search;
    }
    
    
    
}