input validation
-------

## Example:

	"""
	This function is where you store all your input validation controls. 
	It makes it easy to maintain whenever you want to apply changes for 
	certain input validation roles and reduces the chance of mistakes in your regexes.
	"""

	def isAlphanumeric(str):

		match = re.findall("^[a-zA-Z0-9]+$" , str)
		
		# Check for alphanumeric
		if match:
			return True
		else:
			return False

	def isAlpha(str):

		match = re.findall("^[a-zA-Z]+$" , str)
		
		# Check for alpha
		if match:
			return True
		else:
			return False

	def isDigit(str):

		match = re.findall("^[0-9]+$" , str)
		
		# Check for isDigit
		if match:
			return True
		else:
			return False	

	def isBool(str):
	    match = re.findall("^(True|False)+$" , str)
     
		if match:
	        return True
	    else:
            return False	

	def inputValidation(input, type):

	    if type == alphanumeric:
	    	# Set the audit log
	    	setLog(session["id"], "Alphanumeric matched", "Success", str(datetime.utcnow()), session['privilege'])

	    	return isAlphanumeric(input)

	   	elif type == numeric:
	   		# Set the audit log
	   		setLog(session["id"], "Numeric matched", "Success", str(datetime.utcnow()), session['privilege'])
	   		return isDigit(input)

	   	elif type == alpha:
	   		# Set the audit log
	   		setLog(session["id"], "Alphabet matched", "Success", str(datetime.utcnow()), session['privilege'])

	   		return isAlpha(input)

	   	elif type == bool:
	   		# Set the audit log
	   		setLog(session["id"], "Bool matched", "Success", str(datetime.utcnow()), session['privilege'])

	   		return isBool(input)

	   	else:
	   		# Set the audit log
	   		setLog(session["id"], "FAIL", str(datetime.utcnow()), session['privilege'])
	    	
	   		# Increment the counter
	    	counter.increment(1)
	   		return False

