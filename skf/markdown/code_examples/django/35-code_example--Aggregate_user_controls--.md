# Aggregate user controls
-------

## Example:

 
    """
    	In order to enforce Aggregate access control protection the best method would be to
    	define your rules by means of a database structure rather than sessions or log's.
    	This is due to the fact that if the user drops his session the rating would start
    	al over again.
    

    	TABLE userAggregate
    	-----------------------------------------   
    	|   id   | user_id  | AggregateControl	|
    	-----------------------------------------  
    	|   1    | Admin    | 	  2322    	    |
    	-----------------------------------------   
    	|   2    | User     |     0             |
    	-----------------------------------------  
    	|   3    | Guest    |     125           |
    	-----------------------------------------
    	
    """

    # Extend the existing User model by adding another model and linking it to the User model using # one-to-one relation in models.py

    class userAggregate(models.Model):
       user = models.OneToOneField(User)
       AggregateControl = models.IntegerField(default=0)


    # countAccess in views.py

    import logging

    def countAccess(request, count):
        
        """
        Everytime the user accesses the database we keep track of the number of times he
        connected. Whenever the user passes a reasonable number he should be rejected
        since he could be an attacker scraping your table contents and stealing company information
        You could a CRON job in your mysql system in order to clean the Aggregate column within certain timeframes
        """
        
        current_user = request.user

        log = logging.getLogger(__name__)

        #Add logging
        log.debug('User aggregate control updated: {user} via ip: {ip}'.format(
            user=user,
            ip=ip
        ))

        registered_user = userAggregate.objects.get(pk=current_user.id)
        
        # We add the count to control variable for the update
        control = registered_user.AggregateControl + count
            
        # Check the aggregate
        if control > 5000:
            logger.warning('User aggregate control breach: {user} via ip: {ip}'.format(
                user=user,
                ip=ip
            ))
                
            """
            Then we lock out the users account assuming it has been compromised by
            an attacker
            """
                
            access = 0
            current_user.is_active = access
            current_user.save()

            #we update the users table and count +1 tot the AggregateControl column
            registered_user.AggregateControl = control

            registered_user.save()  