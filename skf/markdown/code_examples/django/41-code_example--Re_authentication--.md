# Re-authentication
-------

## Example:


    """
    Whenever a user wants to change his credentials or do other important data exchanges such as
    transferring money he should always be challenged to re-authenticate himself before
    allowing them to perform these actions.
    """
    
    from django.contrib.auth import authenticate, login

    def reauthenticate(request, password):
        //Access current_user
        current_user = request.user
        username = current_user.username
        //Authenticate user
        user = authenticate(request, username=username, password=password)
        //Validation of password 
        if user is not None:
            //After successful validation we will log that password was validated successfully
            log.info('Succeessful reauthentication user : {user} via ip: {ip}'.format(
                user=user,
                ip=ip
            ))

            //Flush Session token 
            request.session.flush()
            //Make the current_user active
            current_user.is_active = 1
            //Save the session ID 
            login(request, user)
            //Sucess page 
            return render(request, 'polls/home.html')
        else:
            //The user failed re-authenticating himself
            log.warning('Reauthentication Failed!! user : {user} via ip: {ip}'.format(
                user=user,
                ip=ip
            ))
            //If authentication failed destroyed the session
            request.session.flush()
            return render(request, 'polls/login.html')

    """
    Before we let a user perform certain actions he should first be challenged to authenticate
    himself. imagine the following scenario, the user wants to change his email address.
    """

    //Usage Example
    reauthenticate(password) 