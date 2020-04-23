## Description:

	The user should be the only one who knows his password, so if an administrator provides the initial password, 
	the user should be able to change his password. Also when a user believes the current password has 
	been (or might have been) compromised, or as a precautionary measure the user must be able to change his password. 	
	When a user changes his password, his current password should be validated. 
	This prevents an attacker that is able to take control of a valid session, to easily change the victim's password.

## Solution:
	
	Verify users can change their password, and the change validates the current secret.
