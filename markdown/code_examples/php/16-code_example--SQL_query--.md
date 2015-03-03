
SQL query
-------

**Example:**



    	<?php

	/*
	This example uses a prepared statement in order to insert data into the database.
	Because this method enforces the user to prepare al the user input which is passed into the query
	it always escapes SQL injections so none could be accidentally forgotten as with the normal mysqli_real_escape_string() methods.
	*/
	
		/*
		For detecting a possible attack on your application simply escaping the userinput obviously not enough
		So you want to verify the submitted input by the user does not contain malicous code.
		In this example the expexted input is a-z/0-9.
		*/
     	if(!preg_match("/^[a-zA-Z0-9]+$/", $name)
     	{
     		/*
			Set counter if counter hits 3 the users session must terminated
			After 3 session terminations the user acount must be blocked
			*/
			setCounter(1);
			
			//Set a log for whenever there is unexpected userinput with a threat level
			setLog($_SESSION['userID'],"invalid expected input", "FAIL", date(dd-mm-yyyy), $privelige, "HIGH");
     	}

	$stmt = $db->prepare("SELECT * FROM table WHERE id=? AND name=?");
	$stmt->execute(array($id, $name));
	$rows = $stmt->fetchAll(PDO::FETCH_ASSOC);
	
	//or		

	$stmt = $db->prepare("SELECT * FROM table WHERE id=:id AND name=:name");
	$stmt->execute(array(':name' => $name, ':id' => $id));
	$rows = $stmt->fetchAll(PDO::FETCH_ASSOC);
	
	/*
	Both methods are preventing SQL injections.
	The less recommended option for preventing sql injections is to use the mysqli_real_escape_string() function.
	*/

	$username = mysqli_real_escape_string($connectionString, $_POST['username']);
	$email    = mysqli_real_escape_string($connectionString, $_POST['email']);

	mysqli_query($connectionString, "INSERT INTO users (username, email) VALUES ("'.$username.'", "'.$email.'")");

	/*
	NOTE: mysqli_real_escape_string() will not work when escaping integers since the function only
	escapes strings. In order to prevent al SQL injection vulnerability we strongly recommend 
	using the prepared statements
	*/
	
   ?>



	