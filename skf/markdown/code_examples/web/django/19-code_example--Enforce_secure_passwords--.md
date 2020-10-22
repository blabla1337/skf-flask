# Enforce secure passwords
-------

## Example:

    
    def checkPassword(pwd):
    	error = []
    	proceed = True

    	//Recommended a longer password for Security
    	if(len(pwd) < 13):
        	error.append("Password is too Short!!")
        	proceed = False
    
		"""
		The password should include at least one number, a small letter, a CAPS,
		and a special character as defined in the patterns array:
		"""
    
    	if not any(x.isupper() for x in pwd):
        	error.append('Your password needs at least 1 capital letter')
    	if not any(x.islower() for x in pwd):
        	error.append('Your password needs at least 1 small letter')
    	if not any(x.isdigit() for x in pwd):
        	error.append('Your password needs at least 1 digit')

		"""
		Even though your password is sufficient according to all your standards, the password could still be weak.
		Just imagine the password "Password!"; this could easily be guessed by an attacker. To prevent the use of weak passwords we 
		compare the password with a list of top 500 bad passwords and if matched, the password wil be rejected:
		"""

    	file = open('badpasswords.txt').read()
    	pattern = file.split(",") 

    	for value in pattern:
        	if value != pwd:
            	pass
        	else:
            	error.append("Your password was matched with the bad password list, please try again.")
            	proceed = False
            	break
    	if proceed == True:
        	flash("Your password is allowed!")
        	return True
        else:
        	flash("Password validation failure(your choice is weak):")
        	for x in error:
            	print x
        	return False