# Audit logs
-------

## Example:


    """
    The log function does not have to be complicated as long as you log at least these 6 values

    Whenever a user is registered or added to your system, the application must also
    automatically generate a table for this user which contains his userID, counter and blocker
    variable in order to keep track of his behavior.
    """

        def setLog(userId, error, value, date, threat):

            """

            """
            
            //Take the client's IP address
            ip = request.remote_addr

            //Save log file in a directory which has restrictions in place so no one can 
            file = "restrictedfolder/logfile.txt"
            f = open(file, 'w+')
            
            //Notice how we user the userID instead of the actual username in order to prevent the integrity of these usernames
            f.write(date + str(userId) + error + value + threat + "Ip : " + str(ip))
            f.close()


        class Counter(db.Model):
            __tablename__ = "counter"
            count = db.Column(db.Integer, nullable=False)
            blocker = db.Column(db.Integer, nullable=False)
            userID = db.Column('userID', db.Integer, db.ForeignKey('users.user_id'), primary_key=True)

            def __init__(self, count, blocker, userID):
                self.count = count 
                self.blocker = blocker
                self.userID = userID

            def increment(self, count):
                self.count+= count
                self.blocker+= count

                if self.counter >= 3:
                    setLog(self.userId,"The users session was terminated", "SUCCESS", datetime.utcnow(), "NULL")
                    //After the counter has terminated a session he should be set to zero again
                    self.count = 0
                    //Log that the users sessions have been terminated
                    logout()

                if self.blocker >= 12:
                    //If the blocker was bigger than 12 it means the user has made three strikes and his account should blocked
                    setLog(self.userId,"The users is denied access to system", "SUCCESS", datetime.utcnow(), "NULL")
                    user = User.query.filter_by(id=self.userID).first()
                    user.status = 'Blocked'