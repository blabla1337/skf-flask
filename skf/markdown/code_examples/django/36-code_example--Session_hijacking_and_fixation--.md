# Session hijacking and fixation
-------

## Example:

    
    """
    Session hijacking and Session fixation are attempts to gain access to another user. 
    We Should never put session IDS in the URL, use SSL and secure connection and HTTP only
    Cookies.

    We should regenerate a SESSION ID when someone logs in. But Django does regenerating 
    Session ID automatically.  

    First we implement the strict transport security header, this is in order to prevent
    users from accessing your application over an unprotected connection.
    """

    //Example of the strict transport security header:
    response['Strict-Transport-Security'] = "max-age=31536000"
    //If all present and future subdomains will be HTTPS:
    response['Strict-Transport-Security'] = "max-age=31536000; includeSubDomains"    

    """
    Recommended: If the site owner would like their domain to be included in the HSTS preload
    list maintained by Chrome (and used by Firefox and Safari), then use:
    """

    response['Strict-Transport-Security'] = "max-age=31536000; includeSubDomains; preload"    

    """
    The `preload` flag indicates the site owner's consent to have their domain preloaded.
    The site owner still needs to then go and submit the domain to the list. the preload list
    enforces the browser to always present your application on HTTPS even on the first time
    the user hits your application

    Then we set the httpOnly flag in settings.py
    (see "HttpOnly" in the code examples for more details about implementation)
    """
    	
    SESSION_COOKIE_HTTPONLY = True

    """
    Then we set the flag for session timeout in settings.py
    (see "Timeout" in the code examples for more details about implementation)
    """
    	
    SESSION_COOKIE_AGE = 60000 

    """
    Then we set the session secure flag in settings.py
    (see "Secure flag" in the code examples for more details about implementation)
    """
    
    SESSION_COOKIE_SECURE = True