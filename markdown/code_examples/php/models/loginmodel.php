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

class LoginModel extends Model{
	
	public function loginUser($username,$password){
		
		$sql = "SELECT * FROM members WHERE username = :username";
		
		$this->_setSql($sql);
		
		$this->_setParam(array(":username" => $username));
		$loginUser = $this->getRow($sql);
				
		if($this->ValidatePassword($loginUser['password'], $password) === true){

			session_start();
			
			$_SESSION['ip'] = $_SERVER['REMOTE_ADDR'];
			$_SESSION['access'] = "active";
			$_SESSION['userID'] = $loginUser['username_id'];
			$_SESSION['csrf'] = base64_encode(openssl_random_pseudo_bytes(128));
			return $loginUser;
   		}
		
		
	}
	
	//Takes a password and returns the salted hash
	//returns - the hash of the password
	function HashPassword($password){
		
	    $salt = bin2hex(mcrypt_create_iv(32, MCRYPT_DEV_URANDOM)); //get 256 random bits in hex
	    $hash = hash("sha256", $salt . $password); //prepend the salt, then hash
	    //store the salt and hash in the same string, so only 1 DB column is needed
	    $final = $salt . $hash;
	    return $final;
	}
	
	//Validates a password
	//returns true if match correct
	function ValidatePassword($correctHash, $password){
		
	    $salt = substr($correctHash, 0, 64); //get the salt from the front of the hash
	    $validHash = substr($correctHash, 64, 64); //the SHA256
	    $testHash = hash("sha256", $salt . $password); //hash the password being tested
	
	    //if the hashes are exactly the same, the password is valid
	    return $testHash === $validHash;
	}
}

