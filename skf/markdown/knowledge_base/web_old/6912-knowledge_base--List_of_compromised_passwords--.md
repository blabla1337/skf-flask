##Description:

	The application should compare the new prospective password against a list that contains values known to be commonly-used, expected, or compromised. 

##Mitigation:
	
	Verify that new or changed passwords are validated against a list of compromised secrets, 
	and if found to be compromised, the user is prompted to choose another secret.
	You can include pasword list as the ones found here https://wiki.skullsecurity.org/Passwords and/or
	use an API that provides a list of compromised secrets as can be found here https://haveibeenpwned.com/API/v2
