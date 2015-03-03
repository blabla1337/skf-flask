
Logout function
-------

**Example:**



    	 <?php
	/*
	By this manner the logout functionality revokes the complete session.
	*/ 

	 function deleteLogin(){

		session_start();
		session_destroy();
	}

	?>


	