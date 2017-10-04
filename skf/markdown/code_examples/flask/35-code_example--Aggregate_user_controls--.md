# Aggregate user controls
-------

## Example:

 
    """
    In order to enforce Aggregate access control protection the best method would be to
    define your rules by means of a database structure rather than sessions or log's.
    This is due to the fact that if the user drops his session the rating would start
    al over again.

    TABLE users
    ---------------------------------------------------------------------------------   
    | userID | userName | password | privilegeID |    access    | AggregateControl	|
    ---------------------------------------------------------------------------------  
    |   1    | Admin    | Csdar323 |      1      |     TRUE     |	  2322    	    |
    ---------------------------------------------------------------------------------   
    |   2    | User     | Adf4fsv  |      2      |     FALSE    |	  0             |
    ---------------------------------------------------------------------------------  
    |   3    | Guest    | dff4fKr  |      3      |     TRUE     |	  125           |
    ---------------------------------------------------------------------------------

    TABLE privileges
    ----------------------------------   
    | privilegeID | privilege        |
    ----------------------------------
    |     1       | edit:read:delete |
    ----------------------------------
    |     2       | edit:read        |
    ----------------------------------
    |     3       | read             |
    ----------------------------------
    """

    def countAccess(count):
        
        """
        Each time the user accesses the database we keep track of the number of times he
        connected. Whenever the user passes a reasonable number he should be rejected
        since he could be an attacker scraping your table contents and stealing company information
        You could a CRON job in your mysql system in order to clean the Aggregate column within certain timeframes
        """
            
        setLog(session['id'], "User access database ", "SUCCESS", datetime.utcnow(), "NULL")
        registered_user = User.query.filter_by(id=session['id']).first()
            
        //We add the count to control variable for the update
        control = registered_user.AggregateControl + count
            
        //Check the aggregate
        if control > 5000:
            setLog(session['id'], "Aggregate control breach", "FAIL", date("d-m-y"), "HIGH")
                
            """
            Then we lock out the users account assuming it has been compromised by
            an attacker
            """
                
            access = "Fail"
            registered_user.status = access
            
            //we update the users table and count +1 tot the AggregateControl column
            registered_user.AggregateControl = control

            db.session.commit()