
Logout function
-------

**Example:**



    	 <?php
	/*
	This way, the logout functionality will revoke the complete session:
	*/ 

	 function deleteLogin(){

		session_start();
		session_destroy();
	}

	?>


	
