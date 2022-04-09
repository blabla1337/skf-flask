# Question
 
What is the problem here?
 
```
<?php
...
session_start();
if (! session_is_registered("username")) {
	echo "invalid session detected!";
	// Redirect user to login page	
	exit;
	}
// The user session is valid, so process the request
// and update the information
update_profile();

function update_profile {
	// read in the data from $POST and send an update
	// to the database
	SendUpdateToDatabase($_SESSION['username'], $_POST['email']);
	[...]
	echo "Your profile has been successfully updated.";
	}
?>
```
 
-----SPLIT-----
 
# Answer

it is a Cross-Site Request Forgery (CSRF) issue. This code may look protected since it checks for a valid session. However, CSRF attacks can be staged from virtually any tag or HTML construct, including image tags, links, embed or object tags, or other attributes that load background images. The attacker can then host code that will silently change the username and email address of any user that visits the page while remaining logged in to the target web application. https://cwe.mitre.org/data/definitions/352.html