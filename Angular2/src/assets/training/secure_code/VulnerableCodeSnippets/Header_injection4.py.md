# Question
 
What is the problem here?
 
```
@app.route('/usermanagement/<user_ID>')
	def route():
	userID = user_ID	
	if request.method == 'GET':
		return render_template('login.html')
	elif request.method == 'POST':
		userName = request.form['userName']
		sessionCookie = request.cookies.get('SessionID')
		if not checkUserSession(userName, sessionCookie):
			return render_template('login.html')
	return redirect(url_for('/users',userID = userID))

def checkUserSession(userName,cookie):
	session = True
	...
	# check if the username:session is valid
	...
	return session
```
 
-----SPLIT-----
 
# Answer

It is a Header Injection issue. The code does not perform any sanitization for 'SessionID' parameter. If the attacker provides 'CR' or 'LF' characters to the parameter, she/he can manipulate the service responses. For example: 'Name1\r\nContent-Length:40\r\n\r\n'