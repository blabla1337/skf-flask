# Question
 
What is the problem here?
 
```
@app.route("/changePasswd")
def login():
    username = request.args.get('username')
    password = request.args.get('password')
    #randomToken = request.args.get('transactionToken')
    #if not isValid(randomToken):
    #	return render_template('Eror.html')
    try:
    	connection = mysql.connector.connect(host='localhost', database='database', user='root', password='p@ssw0rd')
    	cursor = connection.cursor(prepared=True)
    	passwordUpdate = """UPDATE users set password = %s where username = %s"""
    	values = (password, username)
    	cursor.execute(passwordUpdate, values)
    	connection.commit()
    	print("Your password has been changed successfuly.")
	except:
	    print("An error occurred")
```
 
-----SPLIT-----
 
# Answer

It is a Cross-Site Request Forgery (CSRF) issue. The code shows anti-CSRF token control is disabled and the user lacks of protection. You may also realize the database query is using parameterization aganist injection attacks.
