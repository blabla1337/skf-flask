 Privilege based authentication
-------

**Example:**
   	
   	
   	<?php
   	
   	/*
    For privilege based authentication we need an extra tabel in your database in order to write the users privileges to.

    TABLE users
    ---------------------------------------------------------------------------------    
    | userID | userName | password | privilegeID |    access	| AggregrateControl	|
    ---------------------------------------------------------------------------------   
    |   1	 | Admin	| Csdar323 |	  1		 | 	   TRUE		|		2336		|
    ---------------------------------------------------------------------------------   	
    |	2	 | User		| Adf4fsv  |	  2		 |	   FALSE	|		 0			|
    ---------------------------------------------------------------------------------   
    |	3	 | Guest	| dff4fKr  |	  3		 |	   TRUE		|		135			|
    ---------------------------------------------------------------------------------   

    TABLE privileges
    ----------------------------------   
    | privilegeID | privilege 		 | 
    ----------------------------------
    |     1	 	  | edit:read:delete |
    ----------------------------------
    |	  2	 	  | edit:read		 |
    ----------------------------------
    |	  3	 	  | read			 |
    ----------------------------------

    Now instead of using roles in sessions we rather want to assign privileges to users 
    by means of a Database-Based Authentication system. 
    Now we can easily assign a user certain privileges for him to access.
    */
    
   	class privilege{
		//Here is the isAuthorized function in which we check whether the iser is permitted to do the action
		public function isAutorized($ispermitted){
			
			//we make object of logging class for our logging methods also for db connection
			include("classes.php");
			
			$logging = new logging();
			$con 	 = new database();
			
			$db = $con->connection();
			
			//We select the privilege from the database
			$stmt = $db->prepare("
				SELECT a.username, a.password, a.privilegeID, b.privilegeID, b.privilege   
					FROM users as a
						JOIN privileges as b
							ON a.projectID = b.projectID
								WHERE a.userID = :id and b.access='TRUE'");
																				
			$stmt->execute(array(':id' => $_SESSION['userID']));
			$rows = $stmt->fetchAll(PDO::FETCH_ASSOC);
			
			foreach($rows as value){
				$privilege = $value['privilege'];
			}
			
			//We first explode the value's to see how much parts the arrays consists of
			$permission    = explode(":", $privilege); 
			$authorization = explode(":", $ispermitted); // $ispermitted
		
			//Then we count the authorization array
			$count     = count($authorization);
			$counthits = 0; 
		
			/*
			We check the permissions against the ispermitted value to see how many times
			they match. whenever they match we count the hits
			*/
			foreach($permission as $value){
				if(preg_match('/'.$value.'/', $ispermitted)){
					$counthits++;
				}
			}
		
			/*
			Whenever the counts hitted are greater or equal to the needed permissions
			we now know we deserved acces to the part of the system.
			*/
			if($counthits >= $count){
		
				//Log that the user had sufficient privileges:
				$logging->setLog($_SESSION['userID'],"User was privileged!", "SUCCESS", 
				date("d-m-y"), $privelige, "NULL");
				
				return true;
			}else{
			
				//Log that the user had insufficient privileges:
				$logging->setLog($_SESSION['userID'],"User was not privileged!", "FAIL", 
				date(dd-mm-yyyy), $privelige, "HIGH");
			
				/*
				Set counter; if counter hits 3, the user's session must be terminated.
				After 3 session terminations the user's acount must be blocked.
				Given the high threat level, there will be immediate session termination.
				in this case the user tried to manipulate the application operation in order to do things he is not
				privileged to, imidiate session termination will follow!
				*/
			
				$logging->setCounter(3);
			
				return false;
		 	}
		}	
	} 
	
	?>
	   
	/*
    This is how you enforce the permissions in your application
    We define the roles we want the user to suffice
    */
    
    if(isAuthorized("edit:read:delete") === true){
        //Do your operation
    }

	
	/*
    if ever there are new 'roles' added to the system you can easily asign them the needed privileges without 
    having to add new roles throughought your entire system. This system takes a little more planning up ahead but 
    it enforces higher level of security.
    */
    ?>