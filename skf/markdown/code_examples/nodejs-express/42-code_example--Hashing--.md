# Hashing
-------

## Example:

	/**
	  * Taken from https://www.npmjs.com/package/bcrypt
	  */
	var bcrypt = require('bcrypt')
	
	function hash(password){
		var saltRounds = 10
		var hash = bcrypt.hash(myPlaintextPassword, saltRounds)
		return hash
	}

	function validatePassword(user, password){
		var result = bcrypt.compare(myPlaintextPassword, hash, function(err, res)
		return result
	}