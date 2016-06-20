
Login functionality
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

    public function loginUser($username,$password)
    {

        /* 
        You must log invalud userinput in order to detect a possible attack on your login form
        In this example the expexted input is "a-Z/0-9 - _"
        */ 

        if(preg_match("/[^a-zA-Z0-9]/", $username))
        {       
            //Set a log for whenever there is unexpected userinput with a threat level 
            setLog("null","invalid expected input", "FAIL", date(dd-mm-yyyy), "null", "HIGH"); 
        } 

        /*
        We also want to make sure the user access is TRUE, if not, it means the user was blocked
        for attempting to hack the application
        */

	    //After successful validation we want to log that username was validated successfully:
		setLog($_SESSION['userID'],"Username return true", "SUCCESS", date(dd-mm-yyyy), $privelige, "NULL");

        //PDO prepared statement in order to prevent SQL injections
        $sql = "
            SELECT a.username, a.password, a.privilegeID, b.privilegeID, b.privilege   
                FROM users as a
                    JOIN privileges as b
                        ON a.projectID = b.projectID
                            WHERE a.username = :username and b.access='TRUE' ";

        $this->_setSql($sql);

        //We than bind the parameters in order to prevent SQL injection		
        $this->_setParam(array(":username" => $username));
        $loginUser = $this->getRow($sql);
    
    		/*
            Than we validate the password, if the validation is true than we set the sessions
            For more detailed information on password validation check please look into the
            Password storage(salting/stretching/hashing) in the knowledgebase for more information.
            */
            if($this->ValidatePassword($loginUser['password'], $password) === true)
            {
				
				//After successful validation we want to log that Password was validated successfully:
				setLog($_SESSION['userID'],"Password return true", "SUCCESS", date(dd-mm-yyyy), $privelige, "NULL");
                
                session_start();

                //Change the session id on login
			    session_regenerate_id(true);

                //Here we set a session to see if the user is authenticated throughought the system
                $_SESSION['access']   = "active";

                /*
                The userID in a session variable to use as an identifier to prevent a user reading
                into unauthorised data, See Identifier-based authorization for more information and
                code examples.
                */
                $_SESSION['userID']   = $loginUser['id'];

                //The CSRF token is set here by an aproved random number generator
                $_SESSION['csrf'] = base64_encode(openssl_random_pseudo_bytes(128));

                //if all is ok we return loginUser values
                return $loginUser;
            }
    }

    /*
    This is how you enforce the permissions in your application
    We define the roles we want the user to suffice
    */
    
    if(isAuthorized("edit:read:delete") === true){
        //Do your operation
    }


    //Here is the isAuthorized function in which we check whether the iser is permitted to do the action
    function isAutorized($ispermitted){

        //We check the database value in order to verify if we are permitted to do the action
        if($loginUser['permissions'] == $ispermitted)
        {	
       	 	//Log that the user had sufficient privileges:
			setLog($_SESSION['userID'],"User was privileged!", "SUCCESS", date(dd-mm-yyyy), $privelige, "NULL");
            return true;
        }else{
            
            //Log that the user had insufficient privileges:
			setLog($_SESSION['userID'],"User was not privileged!", "FAIL", date(dd-mm-yyyy), $privelige, "HIGH");
			
			/*
			Set counter; if counter hits 3, the user's session must be terminated.
			After 3 session terminations the user's acount must be blocked.
			Given the high threat level, there will be immediate session termination.
			in this case the user tried to manipulate the application operation in order to do things he is not
			privileged to, imidiate session termination will follow!
			*/
			
			setCounter(3);
			
            return false;
        }
    }

    /*
    if ever there are new 'roles' added to the system you can easily asign them the needed privileges without 
    having to add new roles throughought your entire system. This system takes a little more planning up ahead but 
    it enforces higher level of security.
    */

    ?>