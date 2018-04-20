# User registration / Sql truncation prevention
-------

## Example:


    """
    In order to prevent Column truncation sql injection Solution we have to make sure the
    applications structural logic does not mismatches with the database structural logic.
    To achieve this imagine the follow example of a database structure of a users table

    TABLE users
    ------------------------------------------------------------
    |	     *Name* 	   |	*Type* 		  |    *Extra*     |
    ------------------------------------------------------------
    |        userID	       |    Int(11)       | AUTO_INCREMENT |
    ------------------------------------------------------------
    |       Username  	   |    char(21)      |  		       |
    ------------------------------------------------------------
    |       Password       |  Varchar(255)    |			       |
    ------------------------------------------------------------
    |      PrivilegeID     |    Int(11)       | 	     	   |
    ------------------------------------------------------------   
    |      Status          |    Varchar(200)  |                |
    ------------------------------------------------------------
    """

    class User(db.Model):
        __tablename__ = "users"
        id = db.Column('user_id',db.Integer , primary_key=True)
        username = db.Column('username', db.String(20), unique=True , index=True)
        password = db.Column('password' , db.String(10))
        email = db.Column('email',db.String(50),unique=True , index=True)
        status = db.Column('status', db.String(50), index=True)
        registered_on = db.Column('registered_on' , db.DateTime)
        privilegeID = db.Column('privilegeID', db.Integer, db.ForeignKey('privileges.id'))
 
        def __init__(self , username ,password , email, privilegeID, status):
            self.username = username
            self.password = password
            self.email = email
            self.registered_on = datetime.utcnow()
            self.privilegeID = privilegeID
            self.status = status

    //Function to add the details to database
    def userRegister(username, password, email, privilegeID, status):
        user = User(username, password, email, privilegeID, status)
        db.session.add(user)
        db.session.commit()

    //Register user 
    @app.route('/register' , methods=['GET','POST'])
    def register():
        if request.method == 'GET':
            return render_template('signup.html')
        //Ensure the username is not long
        if len(request.form['inputName'] >= 21):
            raise Exception("Long username")
        //Create password hash
        password = passwordHash(request.form['inputPassword'])
        userRegister(request.form['inputName'], password, request.form['inputEmail'], 3, "Active")
        flash('User successfully registered')
        return redirect(url_for('login'))        
        