
Identifier-based authorization
-------

**Example:**


    <?php

	//First, we want to filter the pages for expected values. For this example we use only a-z/0-9
	//Whenever the values are tampered with, we can assume an attacker is trying to inject malicious input.
	if(!preg_match("/^[a-zA-Z0-9]+$/", $_GET['page']){

		//Set a log for whenever there is unexpected userinput with a threat level
		setLog($_SESSION['userID'],"invalid expected input", "FAIL", date(dd-mm-yyyy), $privelige, "HIGH");
		
		/*
		Set counter; if counter hits 3, the user's session must be terminated.
		After 3 session terminations the user's acount must be blocked.
		Given the high threat level, there will be immediate session termination.
		*/
		setCounter(3);
		
	}
 
 

	/* 
	Whenever you are checking whether a user is restricted to review certain data,
	the acces restrictions should be proccessed serverside.
	The userID could be stored inside a session variable on login, and should be used to retrieve userdata from the database:
	*/
	
	//We also want to validate the $page variable went through validations succesfully.
	setLog($_SESSION['userID'],"successful input validation for page", "SUCCESS", date(dd-mm-yyyy), $privelige, "NULL");
	
	/*
	Now we only select the data form the database which the user is allowed to watch by adding the ID to the query.
	If the results do not mach, the user will not be allowed to view the data.
	This prevents the users seeing data which they are not restricted to see simply by changing parameters.
	*/
	$stmt = $db->prepare("SELECT * FROM table WHERE id=:userID AND page=:page");
	$stmt->execute(array(':page' => $page, ':id' => $_SESSION['userID']));
	$rows = $stmt->fetchAll(PDO::FETCH_ASSOC);
	
	?>


	
