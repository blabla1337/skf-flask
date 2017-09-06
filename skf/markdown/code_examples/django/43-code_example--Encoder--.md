# Character encoding
-------

## Example:

    """
    This is the encoder class for whenever you have to allow certain
    possibly dangerous characters into your code for i.e names such as O'reily
	"""

	def encoder(allowed, input, count):
	    
	    """
	    As you can see you can specify allowed characters in your function
	    """
	    
	    flag = True
	    match = re.findall("/^[a-zA-Z0-9 " + allowed+"]+$/", input)

	    if match:

	        """
	        Set a log for whenever there is unexpected userinput with a threat level
	        See "audit logs" code example for more information:
	        """

	        setLog(session['id'], "Bad userinputs", "FAIL", datetime.utcnow(), "HIGH")
	        
	        """
	        Set counter if counter hits 3 the users session must terminated
	        After 3 session terminations the user account must be blocked
	        See "audit logs" code example for more information:
	        """
	        
	        counter.increment()
	        flag = False

	        # Remove Dangerous Characters
	        wordDict = {'&': '&amp;', '<' : '&lt;', '>' : '&gt;' , '"' : '&quot;', "'" : '&#x27;', '/' : &#x2F;, '\' : '\\'}

	        for key in wordDict:
	        	input = input.replace(key, wordDict[key])

	        return input
