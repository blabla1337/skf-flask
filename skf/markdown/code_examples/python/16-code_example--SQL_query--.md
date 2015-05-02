
SQL query
-------

**Example:**


    <?php

	/*
	This example uses a prepared statement in order to insert data into the database.
	Because this method enforces the user to prepare all user input  passed into the query, it always escapes SQL 
	injections so none could be accidentally forgotten as with the normal mysqli_real_escape_string() methods.
	*/
	
	/*
	For detecting a possible attack on your application simply escaping the userinput is obviously not enough.
	Therefore, you'll want to verify the input as submitted by the user does not contain malicous code.
	In this example the expexted input is a-z/0-9:
	*/
	if(!preg_match("/^[a-zA-Z0-9]+$/", $name){

		//Set a log for whenever there is unexpected userinput with a threat level:
		setLog($_SESSION['userID'],"invalid expected input", "FAIL", date(dd-mm-yyyy), $privelige, "HIGH");


		/*
		Set counter; if counter hits 3 the user's session must terminated.
		After 3 session terminations, the user's acount must be blocked
		*/
		setCounter(1);

	}

	//After successful validation we want to log that name was validated successfully:
	setLog($_SESSION['userID'],"succesfull input validation", "SUCCESS", date(dd-mm-yyyy), $privelige, "NULL");

	$stmt = $db->prepare("SELECT * FROM table WHERE id=? AND name=?");
	$stmt->execute(array($id, $name));
	$rows = $stmt->fetchAll(PDO::FETCH_ASSOC);

	}
	
	
	//or		

	//After successful validation we want to log that name was validated successfully:
	setLog($_SESSION['userID'],"succesfull input validation", "SUCCESS", date(dd-mm-yyyy), $privelige, "NULL");
	
	$stmt = $db->prepare("SELECT * FROM table WHERE id=:id AND name=:name");
	$stmt->execute(array(':name' => $name, ':id' => $id));
	$rows = $stmt->fetchAll(PDO::FETCH_ASSOC);
	
	/*
	Both methods will prevent SQL injections.
	The less recommended option for preventing sql injections is to use the mysqli_real_escape_string() function.
	*/

	$username = mysqli_real_escape_string($connectionString, $_POST['username']);
	$email    = mysqli_real_escape_string($connectionString, $_POST['email']);

	mysqli_query($connectionString, "INSERT INTO users (username, email) VALUES ("'.$username.'", "'.$email.'")");

	/*
	NOTE: mysqli_real_escape_string() will _not_ work when escaping integers since the function only
	escapes strings. In order to prevent all SQL injection vulnerabilities, we strongly recommend 
	using prepared statements
	*/
	
   ?>



	
