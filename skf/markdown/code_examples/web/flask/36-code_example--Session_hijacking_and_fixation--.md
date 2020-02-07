# Session hijacking and fixation
-------

## Example:


    """
    As soon as a user logs into your application you must store his session id as well as his
    IP address along with his userID. This information will be used later on in your application in order to identify possible session hijacking.

    TABLE track_sessions
    ---------------------------------------------------------------------------------
    | TrackID | userID |		   	   SESSION 		            |     Ip address	    |
    ---------------------------------------------------------------------------------
    |   1     | 1      | 	79dcd529c0f5e01a9bfb2425c52036c6    |	123.45.67.89	|   
    ---------------------------------------------------------------------------------
    |   2     | 1      | 	79dcd529c0f5e01a9bfb2425c52036c6    |	123.45.67.81	|
    ---------------------------------------------------------------------------------
    |   3     | 2      | 	c80959d3ea4c166413774e45375ac2a1    |	987.65.43.21	|
    ---------------------------------------------------------------------------------

    In order to prevent session hijacking there are a couple of defense strategies
    which combined are a hardened defense.  
    """

    """
    First we implement the strict transport security header, this is in order to prevent
    users from accessing your application over an unprotected connection.
    """

    //Example of the strict transport security header:
    response.headers["Strict-Transport-Security"] = "max-age=31536000"

    //If all present and future subdomains will be HTTPS:
    response.headers["Strict-Transport-Security"] = "max-age=31536000; includeSubDomains"    

    """
    Recommended: If the site owner would like their domain to be included in the HSTS preload
    list maintained by Chrome (and used by Firefox and Safari), then use:
    """

    response.headers["Strict-Transport-Security"] = "max-age=31536000; includeSubDomains; preload"    

    """
    The `preload` flag indicates the site owner's consent to have their domain preloaded.
    The site owner still needs to then go and submit the domain to the list. the preload list
    enforces the browser to always present your application on HTTPS even on the first time
    the user hits your application
    """

    """
    Then we set the httpOnly flag
    (see "HttpOnly" in the code examples for more details about implementation)
    """
    	
    app.config['SESSION_COOKIE_HTTPONLY'] = True

    """
    Then we set the flag for session timeout
    (see "Timeout" in the code examples for more details about implementation)
    """
    	
    app.config['PERMANENT_SESSION_LIFETIME'] = 3600

    """
    Then we set the session secure flag
    (see "Secure flag" in the code examples for more details about implementation)
    """
    app.config['SESSION_COOKIE_SECURE'] = True

    """
    On login we change the session id in order to prevent session fixation
    (see "Login functionality" in the code examples for more details about implementation)
    """
    
    //In header we should include this
    from flask_kvsession import KVSessionExtension
    
    //Call for session regenerate to prevent session fixation
    session.regenerate()

    """
    NOTE: On applications that require high level security, there should never be an
    remember me functionality implemented.
    """


    """
    Now imagine the scenario after the login of the user (see the "login functionality" in
    the code examples for more details). Whenever the user is logged in, the users IP address
    and session id are also stored in the database these values are used in order to verify
    if there are multiple users active on the same session.
    If so, we can let the user decide to terminate the session and terminate the
    other assigned sessions.
    """

    def checkSession():
        //To check whether the user is active
        if session['status'] != "active" or session['status'] == "":
            return redirect(url_for('login'))

        """
        Then we start the rest of the function where we will check if there are multiple
        users/IP addresses using the same session id
        """
    
        //Store the current session
        session = request.cookies.get('session')

        //Get user ip address
        ipaddress = request.remote_addr

        trackSession = track_sessions.query.filter_by(ipaddress = ipaddress).first()
        if trackSession.session == ipaddress:
            return """<div style='border-style:solid; border-color:black; color:white; background-color:red; float:left;'>
                <p>There are other active sessions on other IP-addresses.<br/>
                Your session could be hijacked press logout in order to authenticate again
                for security reasons!
                <br/><br/>
                <a href='/logout'>Terminate sessions</a>
                <br/>
                <a href='/Proceed'>Proceed anyway</a>
                </p>
                </div>"""

    """
    The only thing left to do now is to update your track_sessions table by inserting
    the IP address, sessionID and userID if you want to accept the other sessions as valid.
    Otherwise the user just has to terminate his current session in order to lock out the
    other sessions.
    """