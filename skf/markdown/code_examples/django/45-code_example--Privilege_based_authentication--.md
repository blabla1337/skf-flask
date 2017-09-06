# Privilege based authentication
-------

## Example:


  """
    For privilege based authentication we will use the table users.

    TABLE users
    
      ------------------------------------------------------------
      |      *Name*      |  *Type*              |    *Extra*     |
      ------------------------------------------------------------
      |        ID        |    Int(11)           | AUTO_INCREMENT |
      ------------------------------------------------------------
      |       Username       |    char(21)      |                |
      ------------------------------------------------------------
      |       Password       |  Varchar(255)    |                |
      ------------------------------------------------------------
      |      last_login      |    date          |                |
      ------------------------------------------------------------   
      |      is_superuser    |    int(1)        |                |
      ------------------------------------------------------------
      |      first_name      |    varchar(30)   |                |
      ------------------------------------------------------------
      |      last_name       |    varchar(30)   |                |
      ------------------------------------------------------------
      |      email           |    varchar(30)   |                |
      ------------------------------------------------------------
      |      is_staff        |    int(1)        |                |
      ------------------------------------------------------------
      |      is_active       |    int(1)        |                |
      ------------------------------------------------------------
      |      date_joined     |    date          |                |
      ------------------------------------------------------------ 

    Now instead of using roles in sessions we rather want to assign privileges to users
    by means of a Database-Based Authentication system.
    Now we can easily assign a user certain privileges for him to access.
  """

  """
  Django has inbuilt privilege based approach. Different privileges for django users table
  is superuser, staff, user.

  superuser has the most permission, then staff and at last the user
  """

  def isAuthorized(request):

    # Select current user 
    current_user = request.user

    if current_user.is_superuser == 1 or current_user.is_staff:
      
      # Log the successful authorization
      log.debug('User is privileged: {user} via ip: {ip}'.format(
            user=user,
            ip=ip
      ))
      return True
    
    else:

      # Log the unsuccessful authorization

      log.warning('User is not privileged: {user} via ip: {ip}'.format(
            user=user,
            ip=ip
      ))
      
      # Set counter
  
      return False
  