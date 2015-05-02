
Enforce sequential step order (Wizzard)
-------

**Example:**

	<?php

	/*
	This example consists out of three different steps in order to complete the wizzard
	and execute your main function. The main purpose of this function is to enfoce the user
	completing the entire wizzard in the intended sequential step order.
	*/

	//First we start a session 
	session_start();

	//The beginSteps post is for starting the wizzard
	if(isset($_POST['beginSteps'])){
	step1();
	}


	//in the first step we want the user to submit 2 value's to be processed
	function step1(){
		if(!isset($_POST['step1'])){
			echo " function 1";
			echo " <form method='post'>
				   <input type='text' name='value1' />
				   <input type='text' name='value2' />
				   <input type='submit' name='step2' value='to step 2'/>
				   </form>";	
		}	
	}


	//On submit we start the seccond step
	if(isset($_POST['step2'])){
		step2();
	}

	//Here we check the value's
	function step2(){

		$errors = array();
		$check = true;
		
			//Check if variable is set
			if (empty($_POST['value1'])){
					$check = false;
					array_push($errors, "Value1 was missing");
				}
			
				//Check if variable is set
				if (empty($_POST['value2'])){
					$check = false;
					array_push($errors, "Value2 was missing");
				}
			
				//If variable's are not set we destroy the session and the user has to start
				//The wizard al over again.
				if (!$check){
					echo "something went wrong, please start again.";
				
					//Display the errors on screen
					foreach($errors as $error){
						echo "<br/>".$error."<br/>";
					}
				
					//Here we destroy the sessions to force the user to start over again.
					session_start();
					session_destroy();
				}else{
					//If al goes well we set the session to the final version where we going to process the data
					$_SESSION['active'] = 'final';
			}
		}


	//Final step in the wizzard.
	if($_SESSION['active'] == "final"){
		echo 
		"
		Now we can process our main function, like writing data to database,
		or adding another step in your wizzard for expansion and extra steps.		
		";
	}

	?>