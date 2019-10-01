# Re-authentication
-------

## Example:
    

    """
    Whenever a user wants to change his credentials or do other important data exchanges such as
    transferring money he should always be challenged to re-authenticate himself before
    allowing them to perform these actions.
    """
    
    def reauthenticate(password):
        user = User.query.filter_by(id=session['id']).first()

        //Validation of password in bcrypt encryption
        if ValidatePassword(user.password, password):
        
            //After successful validation we will log that password was validated successfully
            setLog(session['id'], "Password return true", "SUCCESS", str(datetime.utcnow()), session['privilege'], "NULL")

            //Here we set a session to see if the user is authenticated throughout the system
            session['access'] = 'active'

            """
            The userID in a session variable to use as an identifier to prevent a user reading
            into unauthorized data, See Identifier-based authorization for more information and
            code examples.
            """

            //Setting the user Id
            session['id'] = user.id

            return True

        else:

            //The user failed re-authenticating himself
            setLog(session['id'], "Re-authentication failed", "FAIL", str(datetime.utcnow()), "null", "MOD")
            //If authentication failed destroyed the session
            session.destroy()
            session.regenerate()
            session['access'] = ""

            return False


    """
    Before we let a user perform certain actions he should first be challenged to authenticate
    himself. imagine the following scenario, the user wants to change his email address.
    """

    if reauthenticate(password) !== True :

        return "<div id='error'>please reauthenticate yourself<div>"\
    	+ "<form method='post'>"\
    	+ "<input type='password' name='password'/>"\
    	+ "<input type='submit' name='authenticate'/>"\
    	+ "</form>"

    else:
    	//Do operation for changing the email address
    	return "<div id='success'>You can now change your email address!</div>";

