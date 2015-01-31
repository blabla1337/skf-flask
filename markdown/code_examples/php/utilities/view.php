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

class View{
	
	protected $_file;
	protected $_data = array();
	
	public function __construct($file){
		$this->_file = $file;
	}
    
	public function set($key, $value){
		$this->_data[$key] = $value;
	}
	
	public function get($key){
   		return $this->_data[$key];
  	}
	
	public function output(){
		
		if (!file_exists($this->_file)){
			throw new Exception("View " . $this->_file . " doesn't exist.");
		}
		
		extract($this->_data);
		ob_start();
		include($this->_file);
		$output = ob_get_contents();
		ob_end_clean();
		echo $output;
	}
}