# White-listing
-------

## Example:


    """
    First we create a function which checks the allowed patterns:
    whitelisting("value1,value2,value3" , input)
    Whitelisting is checking if a value is identically the same as the whitelist we created. Please rewrite the below part to reflect this.
    """

    def whitelisting(allowed, input):
        result = allowed.split(',')
        flag = False
        for x in result:
            if x == match:
            //If the value is valid we send a log to the logging file
            setLog(session["id"], "Good whitelist validation", "SUCCESS", datetime.utcnow(),"HIGH")
            flag = True
            //Whenever there was a valid match we return true
            return True
            
        //Check for a false in order to send error to log and counter the user
        if flag == False:
            //If the whitelist is bad log the validation 
            setLog(session["id"], "Bad whitelist validation", "FAIL", datetime.utcnow(), "HIGH")            
            counter.increment()
            return False    
