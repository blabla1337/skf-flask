# Question
 
What is the problem here?
 
```
<?php  
$role = $_COOKIES['role'];
if (!$role) {
	$role = getRole('user');
	if ($role) {
		// save the cookie to send out in future responses
		setcookie("role", $role, time()+60*60*2);
	}
	else{
		ShowLoginScreen();
		die("\n");
	}
}
if ($role == 'Reader') {
	DisplayMedicalHistory($_POST['patient_ID']);
}
else{
	die("You are not Authorized to view this record\n");
}
?>
```

-----SPLIT-----
 
# Answer

It is a Bypassing Restriction issue. The code could be for a medical records application. It displays a record to already authenticated users, confirming the user's authorization using a value stored in a cookie. The programmer expects that the cookie will only be set when getRole() succeeds. The programmer even diligently specifies a 2-hour expiration for the cookie. However, the attacker can easily set the "role" cookie to the value "Reader". As a result, the $role variable is "Reader", and getRole() is never invoked. The attacker has bypassed the authorization system. https://cwe.mitre.org/data/definitions/863.html