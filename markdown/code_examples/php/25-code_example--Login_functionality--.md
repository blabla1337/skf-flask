
Debug Enabling
-------

**Example:**

    <?php

    /*

    For privilege based authentication we need an extra tabel in your database in order to write the users privileges to.

    TABLE users
    -------------------------------------------------------------    
    | userID | userName | password | privilegeID |    access	|
    -------------------------------------------------------------  
    |   1	 | Admin	| Csdar323 |	  1		 | 	   TRUE		|
    -------------------------------------------------------------  	
    |	2	 | User		| Adf4fsv  |	  2		 |	   FALSE	|
    -------------------------------------------------------------  
    |	3	 | Guest	| dff4fKr  |	  3		 |	   TRUE		|
    -------------------------------------------------------------  

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

        if(!preg_match("/^[^a-zA-Z0-9_\-]/", $username))
        {       
            //Set a log for whenever there is unexpected userinput with a threat level 
            setLog("null","invalid expected input", "FAIL", date(dd-mm-yyyy), "null", "HIGH"); 
        } 

        /*
        We also want to make sure the user access is TRUE, if not, it means the user was blocked
        for attempting to hack the application
        */

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
    
            //Than we validate the password, if the validation is true than we set the sessions
            if($this->ValidatePassword($loginUser['password'], $password) === true)
            {

                session_start();

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

    //Now we can verify if the user is privileged to perform certain actions
    if($loginUser['privilege'] == "edit:read:delete")
    {
        //We now show the user full possible options
    }

    if($loginUser['privilege'] == "edit:read")
    {
        //We now show the user limited options
    }

    if($loginUser['privilege'] == "edit")
    {
        //We now show the user text only
    }

    /*
    if ever there are new 'roles' added to the system you can easily asign them the needed privileges without 
    having to add new roles throughought your entire system. This system takes a little more planning up ahead but 
    it enforces higher level of security.
    */

    ?>