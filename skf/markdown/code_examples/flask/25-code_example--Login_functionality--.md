# Login functionality
-------

## Example:


    """
    For privilege based authentication we need an extra table in your database in order to write the users privileges to.

    TABLE users
    ---------------------------------------------------------------------
    | userID     | userName   | password | privilegeID   |    access	| 
    ---------------------------------------------------------------------   
    |   1        | Admin	  | Csdar323 |	  1		     | 	   TRUE		|
    ---------------------------------------------------------------------   	
    |	2	     | User		  | Adf4fsv  |	  2		     |	   FALSE	|
    ---------------------------------------------------------------------   
    |	3	     | Guest	  | dff4fKr  |	  3		     |	   TRUE		|
    ---------------------------------------------------------------------   

    TABLE privileges
    -------------------------------------- 
    | privilegeID     | privilege        |
    --------------------------------------
    |     1           | edit:read:delete |
    --------------------------------------
    |	  2	          | edit:read		 |
    --------------------------------------
    |	  3	          | read	         |
    --------------------------------------

    Now instead of using roles in sessions we rather want to assign privileges to users
    by means of a Database-Based Authentication system.
    Now we can easily assign a user certain privileges for him to access.
    See "Privilege based authentication" code example for more information:
    We will be using flask_login module for login
    """

    from flask_login import login_user, LoginManager, UserMixin, logout_user, login_required

    //Instantiating Flask Login
    login_manager = LoginManager()
    login_manager.init_app(app)


    //Database model for User
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


    //Login a user
    @app.route('/login', methods=['GET', 'POST'])
    def login():
        //Redirect to login page in GET request
        if request.method == 'GET':
            return render_template('login.html')
        
        //Initializing username and password
        username = request.form['inputName']
        password = request.form['inputPassword']

        //Check whether the username is alphanumeric
        if inputValidation('alphanumeric', username) != True:
            setLog(0, "invalid expected input", "FAIL", str(datetime.utcnow()), "HIGH")
            return redirect(url_for('login'))

        //Username and password check   
        registered_user = User.query.filter_by(username=username).first()
        if registered_user is None:
            flash('Username or Password is invalid' , 'error')
            return redirect(url_for('login'))

        //Validate the password hash on bycrypt
        elif ValidatePassword(registered_user.password, password):
            //Logged In successfully
            login_user(registered_user)
            flash('Logged in successfully')
        
        return render_template('home.html', user=request.form['inputName'])
