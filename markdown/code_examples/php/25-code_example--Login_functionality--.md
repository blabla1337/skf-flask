
Login functionality
-------

**Example:**



		function loginUser($username,$password){
		
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
		
			return $loginUser;
		}
	
		//Do not forget to hash,salt and stretch the passwords!





	