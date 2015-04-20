
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

    function setCounter($count){

        //Here we want to set a counter for whenever a user attacks the application so we can lock-out his account 
        //when there are to many violations registered.
        $stmt = $db->prepare("UPDATE counter SET count=? blocker=? WHERE id=?");
        $stmt->execute(array($count, $_SESSION['userID']));
        $affected_rows = $stmt->rowCount();

        $sth = $this->_db->prepare($sql);
        return $sth->execute($data);

        //Here we select all data to verify if the users session should be terminated or his acount should be locked-out
        $stmt = $db->prepare("SELECT count, blocker FROM counter WHERE userID=:id");
        $stmt->execute(array($_SESSION['userID']));
        $rows = $stmt->fetchAll(PDO::FETCH_ASSOC);

            //If the users counter was bigger than three his session should be terminated
            if($rows['count'] >= 3)
            {
            	//Log that the users sessions have been terminated:
				setLog($_SESSION['userID'],"The users session was terminated", "SUCCESS", date(dd-mm-yyyy), $privelige, "NULL");
                
                //We also empty the current session before destroying it
                $_SESSION['isAuthenticated'] = "";
                
                ssession_start();
                session_destroy();
                $count = 0;
                die;
            }	

            //If the users counter was bigger than three his session should be terminated
            if($rows['blocker'] >= 12)
            {	
                //Log that the users has been denied access to system:
				setLog($_SESSION['userID'],"The users is denied access to system", "SUCCESS", date(dd-mm-yyyy), $privelige, "NULL");
            	
                //If the blocker was bigger than 12 it means the user has made three strikes and his acount should blocked
                $status = "blocked"
                $stmt = $db->prepare("UPDATE users SET status=? WHERE id=?");
                $stmt->execute(array($status, $_SESSION['userID']));
                $affected_rows = $stmt->rowCount();

                $sth = $this->_db->prepare($sql);
                return $sth->execute($data);	
            }	

        //After the counter has terminated a session he should be set to zero again
        $stmt = $db->prepare("UPDATE counter SET count=? WHERE id=?");
        $stmt->execute(array($count, $_SESSION['userID']));
        $affected_rows = $stmt->rowCount();

        $sth = $this->_db->prepare($sql);
        return $sth->execute($data);

    }




    ?>



	