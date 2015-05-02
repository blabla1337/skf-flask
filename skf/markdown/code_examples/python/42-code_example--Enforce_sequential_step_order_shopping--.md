
Enforce sequential step order (Shopping)
-------

**Example:**

   	<?php

	/*
	
	Whenever an functionality consists out of following several steps to achieve some goal i.e, 
	"User adds items to chart", "User enters shipping information", "User pays for goods",
	"Items will be shipped." You want to make sure the user can not skip the payment step in 
	order to receive his goods.	
	
	
	----------	----------  -----------  ----------------
	| Items  |	|  Cart	 |	|checkout |	 | CostumerInfo	| 
	----------	----------  -----------	 ----------------
	|itemID  |	|cartID  |	|PaymentID|  |ConsumerID    | 
	|price	 |	|itemID  |	|itemID   |	 |name          |
	|name	 |	|sesionID|	|Token    |	 |adress		| 
	----------	----------  |sessionID|  |sessionID   	| 
							|Verified |  |consumerToken | 
							----------	 ----------------		
	
	As you can see above we have a very simplified database structure for your average
	webshop. now we can walk through the different steps needed to enforce the user to take
	all steps before payment.
	
	We wont cover the entire shopping cart functions since that would become a rather big 
	example so let's cover the basics of enforcing the sequential steps.
	
	Step1: would be, the user adding items to his cart.
	
	Step2: would be, the user adding his items to checkout. Whenever he is done shopping
		   "add to checkout" generates a random token for the added items which
		    are inserted into the payment table in the databse
		    
	
	*/
	
	//First we build the checktokens function because we want to check the checkout tokens
	//multiple times throughout the steps
	function checkTokens(){	
		$stmt = $db->prepare("SELECT * from checkout where sessionID=? ");
		$stmt->execute(array(session_id()));
		$rows = $stmt->fetchAll(PDO::FETCH_ASSOC);

		foreach($rows as $row){
	
			//Here we check for a different token or new session token
			if(($row['token'] != $row['token']) && ($row['token'] != $_SESSION['token'])){
		
				$stmt = $db->prepare("DELETE FROM costumerinfo WHERE sessionID=:id");
				$stmt->execute(array(session_id()));
				$affected_rows = $stmt->rowCount();
		
				$stmt = $db->prepare("DELETE FROM checkout WHERE sessionID=:id");
				$stmt->execute(array(session_id()));
				$affected_rows = $stmt->rowCount();
			
				header('location:checkout.php');
			}
		}
	}
	
	//note: As soon as the user visits your website you start sessions in order to asign phpsessionID
	
	//A random token for every time the form loads
	$token = base64_encode(openssl_random_pseudo_bytes(128));
	
	/*
	We create a session with the token, if someone adds new items to the checkout this
	token will change and will intercept attackers tampering the system.
	*/
	
	
	?>
	
	<form methods="post">
	<input type="hidden" name="token"  value="<?php echo $token; ?>"/>
	<input type="submit" name="submit" value="add to checkout"/>
	</form>
	
	
	<?php 
	
	//On submit we create a new session for the token
	if(isset($_POST['submit']){
		$_SESSION['token'] = $token;
	}
	
	/*
	On submit we send al the shopping cart data to another table in the database, but
	this time al the items also contain the same random token. Now an attacker cannot sneak 
	in new items since these tokens will be evaluated on the payment page.
	
	next, the user lands on a page where he has to fill in his costumer info:
	
	NOTE: do not forget the CSRF token in order to prevent attackers from changing his 
	shipping info.
	*/
	
	//First we check the checkout tokens to see if no new items where added.
	checkTokens();

	?>
	
	<form methods="post">
	<input type="text"   name="costumerName" />
	<input type="text"   name="CostumerAdress" />
	<input type="submit" name="submit" value="to payment"/>
	<input type="hidden" name="token"  value="<?php echo $_SESSION['csrf']; ?>"/>
	</form>
	
	<?php
	
	//After submit we first ofcourse check the CSRF token for validity
	
	checkCsrf($_POST['token']);
	
	//Check the checkout tokens to see if no new items where added
	checkTokens();  
	
	//than we proceed to check if the post values where not empty
	$errors = array();
	$check = true;
	
	if(empty($_POST['costumerName'])){
			$check = false;
			array_push($errors, "Costumer name is required");
		}
			
		if(empty($_POST['costumerAdress'])){
			$check = false;
			array_push($errors, "Costumer adress is required");
		}

        if(!$check){
        	echo $errors;
        }
        else{
                        	
        	header('location:summary.php');
        	//In this step we also insert al the consumer data into the database.
        }
        
    /*
    Then we select al the comsumer info and shopping items on sessionID from the 
    database and display it on screen in order for the user to verify if all the 
    information displayed is correct.
    */
	
	//when the user has verfied we again check the checkout tokens to see if no new items where added
	checkTokens();    
    
    /*
    After that the user verifies this information then he will be redirected to the payment
    page like ideal, paypall etc. 
    
    Whenever the payment returns true you set the "verified" column on the checkout
    table to TRUE and you send the customer the invoice and send him his items.
    */
    
	
	$verified = "true";
	$stmt = $db->prepare("UPDATE checkout SET verified=? WHERE sessionID=? and token=?");
	$stmt->execute(array($verified, session_id(), $_SESSION['token']));
	$affected_rows = $stmt->rowCount();
    
    //also in this step we clear al the db items matching to the phpsessionid
    $stmt = $db->prepare("DELETE FROM costumerinfo WHERE sessionID=:id");
	$stmt->execute(array(session_id()));
	$affected_rows = $stmt->rowCount();
		
	$stmt = $db->prepare("DELETE FROM checkout WHERE sessionID=:id");
	$stmt->execute(array(session_id()));
	$affected_rows = $stmt->rowCount();
	
	$stmt = $db->prepare("DELETE FROM cart WHERE sessionID=:id");
	$stmt->execute(array(session_id()));
	$affected_rows = $stmt->rowCount();
    
    */

	