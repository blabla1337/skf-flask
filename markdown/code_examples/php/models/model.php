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

//error_reporting(0);

class Model{
	
	protected $_db;
	protected $_sql;
	protected $_sqlParam;
	
	public function __construct(){
		$this->_db = Db::init();
	}
	
	protected function _setSql($sql){
		$this->_sql = $sql;
	}

	protected function _setParam($params){
		$this->_sqlParam = $params;
	}
	
	
	public function getAll($data = null){
		
		if (!$this->_sql){
			throw new Exception("No SQL query!");
		}
		
		$sth = $this->_db->prepare($this->_sql);
		
		foreach ($this->_sqlParam as $key => $value) {
			$sth->bindValue($key,$value);
		}
		
		$sth->execute();
		return $sth->fetchAll();
	}
	
	
	public function getRow($data = null){
		
		if (!$this->_sql){
			throw new Exception("No SQL query!");
		}
		
		$sth = $this->_db->prepare($this->_sql);
		
		foreach ($this->_sqlParam as $key => $value) {
		$sth->bindValue($key,$value);
		}
		$sth->execute();
		return $sth->fetch();
	}
	
	
	
		public function editRow($data = null){
		
		if (!$this->_sql){
			throw new Exception("No SQL query!");
		}
		
		$sth = $this->_db->prepare($this->_sql);
		
		foreach ($this->_sqlParam as $key => $value) {
		$sth->bindValue($key,$value);
		}
		
		$sth->execute();
		return $sth->rowCount();
	}
	
	

	
}