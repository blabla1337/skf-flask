# SQL query
-------

## Example:


    """
    SQLAlchemy is the Python SQL toolkit and Object Relational Mapper that gives application developers the full power and flexibility of SQL.
	"""

	from flask_sqlalchemy import SQLAlchemy
	
	//Will track modifications of objects and emit signals
	app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
	//Database URI is used for connection
	app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
	//Create object of SQL Alchemy
	db = SQLAlchemy(app)

	//Class Model that is a declarative base which can be used to declare models
	class User(db.Model):
    	id = db.Column(db.Integer, primary_key=True)
    	username = db.Column(db.String(80), unique=True, nullable=False)
    	password = db.Column(db.String(120), unique=True, nullable=False)

    	def __repr__(self):	
        	return '<User %r>' % self.username

    
    //create the tables and database
    from yourapplication import db
	db.create_all()

	//Inserting data into the database - create, add and commit
	admin = User(username='admin', password='9u3$$_m3_1f_y0u_C@n')
	db.session.add(admin)
	db.session.commit()

	//Delete entries from the table
	db.session.delete(admin)
	db.session.commit()

	//Querying Records
	//Retrieve the user with username
	admin = User.query.filter_by(username='admin').first()
	admin.id

	//SQL raw string approach

	from sqlalchemy import text

	if inputValidation(inputParameter, 'alphanumeric') == False:
		//Protection from string interpolation attack
		sql = text("select name from penguins where id =%s" % (inputParameter,) )
	
		result = db.engine.execute(sql)
		print result[0]