# SQL query
-------

## Example:


    <?php

	/*
	This example uses a prepared statement in order to insert data into the database.
	Because this method enforces the user to prepare all user input  passed into the query, it always escapes SQL
	injections so none could be accidentally forgotten as with the normal mysqli_real_escape_string() methods.
	*/

	$stmt = $db->prepare("SELECT * FROM table WHERE id=? AND name=?");
	$stmt->execute(array($id, $name));
	$rows = $stmt->fetchAll(PDO::FETCH_ASSOC);

	//or		

	$stmt = $db->prepare("UPDATE table SET name=? WHERE id=?");
	$stmt->execute(array($name, $id));
	$affected_rows = $stmt->rowCount();

	//or

	$stmt = $db->prepare("DELETE FROM table WHERE id=:id");
	$stmt->bindValue(':id', $id, PDO::PARAM_STR);
	$stmt->execute();
	$affected_rows = $stmt->rowCount();

	//or

	$stmt = $db->prepare("INSERT INTO table(field1,field2) VALUES(:field1,:field2)");
	$stmt->execute(array(':field1' => $field1, ':field2' => $field2));
	$affected_rows = $stmt->rowCount();

	/*
	All methods will prevent SQL injections.
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
