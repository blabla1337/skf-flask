
Logout function
-------

**Example:**



		/*
		By this manner the logout functionality revokes the complete session.
		*/ 

		 function deleteLogin(){

			session_start();
			session_destroy();
		}




	