
Identifier-based authorization
-------

**Example:**


    <?php

	/* 
	Whenever you are checking whether a user is restricted to review certain data,
	the acces restrictions should be proccessed serverside.
	The userID could be stored inside a session variable on login, and should be used to retrieve userdata from the database:
	*/
	

	$stmt = $db->prepare("SELECT * FROM table WHERE id=:userID AND page=:page");
	$stmt->execute(array(':page' => $page, ':id' => $_SESSION['userID']));
	$rows = $stmt->fetchAll(PDO::FETCH_ASSOC);
	
	?>


	
