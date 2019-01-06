# Hashing
-------

## Example:

	/**
	   Taken from https://www.npmjs.com/package/bcrypt
	**/
	var bcrypt = require('bcrypt')
	
	function hash(password){
		var saltRounds = 10
		var hash = bcrypt.hash(myPlaintextPassword, saltRounds)
		return hash
	}

	// Asynchronous method
	function validatePassword(user, password){
		bcrypt.compare(myPlaintextPassword, hash, function(err, res) {
			if(res) {
			// Passwords match
			} else {
			// Passwords don't match
		  	} 
		});
	}

	// Synchronous method
	function validatePassword(user, password){
		if(bcrypt.compareSync('somePassword', hash)) {
		 // Passwords match
		 return true;
		} else {
		 // Passwords don't match
		 return false;
		}
	}
