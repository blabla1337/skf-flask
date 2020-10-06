# Identifier-based authorization
-------

## Example:


    <?php

	class identifierBasedAuth{ 	

		/*
		Define the whitelist pattern and validation type and input parameter like:
		identity("page1,page2,etc", "alphanumeric", $_GET['page'], "3")
		*/
		public function identity($whiteListPattern, $validationType, $inputParameter, $countLevel){

			//Include the classes of which you want to use objects from
			include_once("classes.php");

			$validate  = new validation();
			$whitelist = new whitelisting();
			$aggregate = new aggregateControl();
			$conn  	   = new database();

			//init DB connection
			$db = $con->connection();

			$continue = true;

			/*
			First, we want to filter the filenames for expected values. For this example we use only a-z/0-9
			Whenever the values are tampered with, we can assume an attacker is trying to inject malicious input.
			for more information about validation see "input validations" in the code examples:
			*/
			if($validate->inputValidation($inputParameter, $validationType,
			"Invalid user input", "HIGH", $countLevel) == false) {$continue = false;}

			/*
			Second, we want to whitelist the filenames for expected values, in this example they are,
			page1,page2 etc.. for more information about whitelisting see "white-listing" in the code examples:
			*/
			if($whitelist->checkpattern($whiteListPattern, $inputParameter, $countLevel) == false)
			{$continue = false;}

			/*
			Whenever you are checking whether a user is restricted to review certain data,
			the access restrictions should be processed server side.
			The userID could be stored inside a session variable on login, and should be used to
			retrieve user data from the database:
			*/
			if($continue == true){

				/*
				We count the number of connections towards the database,
				See "aggregate user controls" code example for more information:
				*/
				$aggregate -> countConnections(1);

				$stmt = $db->prepare("SELECT * FROM table WHERE id=:userID AND page=:page");
				$stmt->execute(array(':page' => $_GET['page'], ':id' => $_SESSION['userID']));
				$rows = $stmt->fetchAll(PDO::FETCH_ASSOC);
			}
		}
	}

    ?>
