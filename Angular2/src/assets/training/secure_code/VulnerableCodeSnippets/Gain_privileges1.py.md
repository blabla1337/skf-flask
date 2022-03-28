# Question
 
What is the problem here?
 
```
def makeNewUserDir(username):
	if not username:
		print('Username cannot be empty!')
		return False
	try:
		raisePrivileges()
		os.mkdir('/home/' + username)
		lowerPrivileges()
	except OSError:
		print('Unable to create new user directory for user:' + username)
		return False
	return True
```
 
-----SPLIT-----
 
# Answer

It is a Gain Privilege issue. This code temporarily raises the program's privileges to allow creation of a new user folder. While the program only raises its privilege level to create the folder and immediately lowers it again, if the call to os.mkdir() throws an exception, the call to lowerPrivileges() will not occur. As a result, the program is indefinitely operating in a raised privilege state, possibly allowing further exploitation to occur. https://cwe.mitre.org/data/definitions/269.html