
Aggregate user controlls
-------

**Example:**

   	<?php

	/*
	In order to enforce Aggregate access control protection the best method would be to 
	define your rules by means of a database structure rather than sessions or log's.
	This is due to the fact that if the user drops his session the rating would start
	al over again. 
	
	TABLE users
	---------------------------------------------------------------------------------   
	| userID | userName | password | privilegeID |    access    | AggregateControl	|
	---------------------------------------------------------------------------------  
	|   1    | Admin    | Csdar323 |      1      |     TRUE     |		2322		|
	---------------------------------------------------------------------------------   
	|   2    | User     | Adf4fsv  |      2      |     FALSE    |		  0			|
	---------------------------------------------------------------------------------  
	|   3    | Guest    | dff4fKr  |      3      |     TRUE     |	     125		|	
	---------------------------------------------------------------------------------

	TABLE privileges
	----------------------------------   
	| privilegeID | privilege        | 
	----------------------------------
	|     1       | edit:read:delete |
	----------------------------------
	|     2       | edit:read        |
	----------------------------------
	|     3       | read             |
	----------------------------------
	

	*/
	
	function countAccess($count){
		
		/*
		Everytime the user accesses the database we keep track of the number of times he
		connected. Whenever the user passes a reasonable number he should be rejected 
		since he could be an attacker scraping your table contents and stealing company information
		You could a CRON job in your mysql system in order to clean the Aggregate column within certain timeframes
		*/
		
		//First we log the access
		setLog($_SESSION['userID'],"User access the database ", "SUCCESS", date(dd-mm-yyyy), $privelige, "NULL");
		
		//Then we update the users table and count +1 tot the AggregateControl column
		$stmt = $db->prepare("UPDATE users SET AggregateControl=? WHERE userID=?");
		$stmt->execute(array($count, $_SESSION['userID']));
		$affected_rows = $stmt->rowCount();
		
		//After that we select 
		$stmt = $db->prepare("SELECT AggregateControl FROM users WHERE userID=:id ");
		$stmt->execute(array(':id' => $id));
		$rows = $stmt->fetchAll(PDO::FETCH_ASSOC);
	
			if($rows['aggregateControl'] >= 5000){
			
				//First we log the surpassing of the user control count
				setLog($_SESSION['userID'],"Aggregate access control breach ", "FAIL", date(dd-mm-yyyy), $privelige, "HIGH");
			
				/*
				Then we lock out the users account assuming it has been compromised by
				an attacker.
				*/
				$access = "FAIL";
				$stmt = $db->prepare("UPDATE users SET access=? WHERE userID=?");
				$stmt->execute(array($access, $_SESSION['userID']));
				$affected_rows = $stmt->rowCount();
								
			}	
		
	}
	
	

	?>

