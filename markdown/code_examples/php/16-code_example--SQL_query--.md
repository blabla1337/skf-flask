
SQL query
-------

**Example:**



		/*
		This example uses a prepared statement in order to insert data into the database.
		Because this method enforces the user to prepare al the user input which is passed into the query
		it always escapes SQL injections so none could be accidentally forgotten as with the normal mysqli_real_escape_string() methods.
		*/

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
	





	