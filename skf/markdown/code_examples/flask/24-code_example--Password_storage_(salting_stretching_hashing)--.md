# Password storage (salting/stretching/hashing)
-------

## Example:


    from flask.ext.bcrypt import Bcrypt

    //Intialise the application with Bcrypt
	app = Flask(__name__)
	bcrypt = Bcrypt(app)

	//For the encryption of passwords we use BCRYPT encryption method.

	def createHash(pwd):
		setLog(0, "Create password Hash", "SUCCESS", str(datetime.utcnow()), "HIGH")
		return bcrypt.generate_password_hash(pwd)

	//Validate your password

	def ValidatePassword(pwd_hash, pwd):
		setLog(0, "Start ValidatePassword", "SUCCESS", str(datetime.utcnow()), "HIGH")
		try:
			return bcrypt.check_password_hash(pwd_hash, pwd)
			setLog(0, "ValidatePassword correct password", "SUCCESS", str(datetime.utcnow()), "HIGH")
		except ValueError:
			return False
			setLog(0, "ValidatePassword incorrect password", "FAIL", str(datetime.utcnow()), "HIGH")

		