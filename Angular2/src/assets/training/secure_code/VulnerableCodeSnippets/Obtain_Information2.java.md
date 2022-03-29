# Question
 
What is the problem here?
 
```
public boolean checkUserCreds(String userName, String userPasswd) {
	Console.WriteLine("Your credentials are being checked!");
	if isUserValid(userName){
		if isPasswdValid(userName, userPasswd){
			Console.WriteLine("Wellcome" + userName + ", you will be redirected to now!");
			return true;
		}
		else{
			Console.WriteLine("Your password is not valid!");
			return false;
		}
	}
	else {
		Console.WriteLine("Your username is not valid!");
		return false;
	}
}
public boolean isUserValid(String userName){
	return validation(username);
}
public boolean isPasswdValid(String userName, String userPasswd){
	return validation(username, userPasswd);
}
```
 
-----SPLIT-----
 
# Answer

It is an Obtain Information issue. The application responses details about which login credential is wrong: username or password. However, it should only provide more generic information to the endusers.
