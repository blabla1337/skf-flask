# Privilege based authentication
-------

## Example:

        
    """
    For privilege based authentication we need an extra table in your database in order to write the users privileges to.

    TABLE users
    ---------------------------------------------------------------------------------    
    | userID | userName | password | privilegeID |    access	| AggregateControl	  |
    ---------------------------------------------------------------------------------   
    | 1	     | Admin	  | Csdar323 |	  1		     | 	   TRUE		|		2336		          |
    ---------------------------------------------------------------------------------   	
    |	2	     | User		  | Adf4fsv  |	  2		     |	   FALSE	|		 0		        	  |
    ---------------------------------------------------------------------------------   
    |	3	     | Guest	  | dff4fKr  |	  3		     |	   TRUE		|		135		        	  |
    ---------------------------------------------------------------------------------   

    TABLE privileges
    ----------------------------------   
    | privilegeID | privilege 		   |
    ----------------------------------
    |   1	 	      | edit:read:delete |
    ----------------------------------
    |	  2	 	      | edit:read		     |
    ----------------------------------
    |	  3	 	      | read			       |
    ----------------------------------

    Now instead of using roles in sessions we rather want to assign privileges to users
    by means of a Database-Based Authentication system.
    Now we can easily assign a user certain privileges for him to access.

    Here is the isAuthorized function in which we check whether the user is permitted to do the action
    """

    def isAuthorized(ispermitted):

      //Select Privilege from the database
      data = Users.query.join(privileges, Users.projectID==privileges.projectID).filter_by(Users.userId==session['id'], privileges.access='TRUE').all()

      privilege = data.privilege

      //We first explode the value's to see how much parts the arrays consists of
      permission = privilege.split(':')
      authorization = ispermitted.split(':')

      //Then we count the authorization array
      count = len(authorization)
      counthits = 0

      """
      We check the permissions against the ispermitted value to see how many times
      they match. whenever they match we count the hits
      """

      for value in permission:
        if value == ispermitted:
          counthits = countshits + 1

      """
      Whenever the counts hits are greater or equal to the needed permissions
      we now know we deserved access to the part of the system.
      """

      if counthits > count:
        //Log that the user had sufficient privileges:
        setLog(session['id'], "User was privileged!", "SUCCESS", str(datetime.utcnow()), privilege, "NULL")
        return True
      else:
        //Log that the user had sufficient privileges:
        setLog(session['id'], "User was not privileged!", "FAIL", str(datetime.utcnow()), privilege, "HIGH")

        """
        Set counter; if counter hits 3, the user's session must be terminated.
        After 3 session terminations the user's account must be blocked.
        Given the high threat level, there will be immediate session termination.
        in this case the user tried to manipulate the application operation in order to do things he is not
        privileged to, immediate session termination will follow!
        """

        Counter.increment(3)
        return False
        