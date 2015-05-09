
Audit logs
-------

**Example:**

	<?php

    /*
    The log function does not have to be complicated as long as you log at least these 6 values
    */

    function setLog($userID, $errorMessage, $value, $date, $privilege, $threat){

        //Save log file in a directory which has restrictions in place so no one can access it easily
        $myFile = "/restrictedfoler/logfile.txt";

        $fh = fopen($myFile, 'w') or die("can't open file");

        //Notice how we user the userID instead of the actual username in order to prevent the integrity of these usernames
        //should an attacker ever gain acces to these log files
        $stringData = $date." ".$userID." ".$errorMessage." ".$value." ".$privelege." ".$threat." \n" ;

        fwrite($fh, $stringData);
        fclose($fh);
    }
	
	/*
	Whenever a user is registered or added to your system, the application must also 
	automatically generate a table for this user which contans his userID, counter and blocker
	variable in order to keep track of his behavior.
	*/
	
    function setCounter($count){

        //Here we select all data to verify if the users session should be terminated or his acount should be locked-out
        $stmt = $db->prepare("SELECT count, blocker FROM counter WHERE userID=:id");
        $stmt->execute(array($_SESSION['userID']));
        $row = $stmt->fetchAll(PDO::FETCH_ASSOC);
			
		foreach($row as $rows){
		
			//First we update the count/blocker variable with the old values for the update
			$dbCount   = $rows['count'];
			$dbBlocker = $rows['blocker'];
			
		}
		
		$countUpdate   = $count + $dbCount;
		$blockerUpdate = $count + $dbBlocker; 
		
		var_dump($dbCount);

        //Here we want to set a counter for whenever a user attacks the application so we can lock-out his account 
        //when there are to many violations registered.
        $stmt = $db->prepare("UPDATE counter SET count=?, blocker=? WHERE userID=?");
        $stmt->execute(array($countUpdate, $blockerUpdate, $_SESSION['userID']));
        $affected_rows = $stmt->rowCount();

		//If the users counter was bigger than three his session should be terminated
		if($countUpdate >= 3){
		
			//Log that the users sessions have been terminated:
			setLog($_SESSION['userID'],"The users session was terminated", "SUCCESS", date(dd-mm-yyyy), $privelige, "NULL");
			
			//Clear the session variable to deny access
			$_SESSION['accessor'] = "";
			
			session_start();
			session_destroy();
			$countUpdate = 0;	
		}	
		
			
		//If the users counter was bigger than three his session should be terminated
		if($blockerUpdate >= 12){
			
			//Log that the users has been denied access to system:
			setLog($_SESSION['userID'],"The users is denied access to system", "SUCCESS", date(dd-mm-yyyy), $privelige, "NULL");
			
			//If the blocker was bigger than 12 it means the user has made three strikes and his acount should blocked
			$status = "blocked";
			$stmt = $db->prepare("UPDATE users SET status=? WHERE userID=?");
			$stmt->execute(array($status, $_SESSION['userID']));
			$affected_rows = $stmt->rowCount();	
		}	

        //After the counter has terminated a session he should be set to zero again
        $stmt = $db->prepare("UPDATE counter SET count=? WHERE userID=?");
        $stmt->execute(array($countUpdate, $_SESSION['userID']));
        $affected_rows = $stmt->rowCount();

    }

    ?>





	