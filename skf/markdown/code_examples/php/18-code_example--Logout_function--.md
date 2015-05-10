
Logout function
-------

**Example:**



    <?php
	
	/*
	This way, the logout functionality will revoke the complete session:
	*/ 

	function deleteLogin(){

		//We first want to log the user logging out.
		setLog($_SESSION['userID'],"User logout", "SUCCESS", date(dd-mm-yyyy), $privelige, "NULL");
		
		//We empty his authentication session
		$_SESSION['Authenticated'] = "";
		
		//Than we destroy the entire session
		session_start();
        session_regenerate_id(true);
		session_destroy();
	}

	?>


	
