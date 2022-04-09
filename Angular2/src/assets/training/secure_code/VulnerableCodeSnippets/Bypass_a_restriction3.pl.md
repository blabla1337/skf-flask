# Question
 
What is the problem here?
 
```
my $q = new CGI;
if ($q->cookie('loggedin') ne "true") {
	if (! AuthenticateUser($q->param('username'), $q->param('password'))) {
		ExitError("Error: you need to log in first");
	}
	else {
		# Set loggedin and user cookies.
		$q->cookie(
			-name => 'loggedin',
			-value => 'true'
		);
		$q->cookie(
			-name => 'user',
			-value => $q->param('username')
			);
	}
}
if ($q->cookie('user') eq "Administrator") {
	DoAdministratorTasks();
}
```
 
-----SPLIT-----
 
# Answer

It is a Bypassing Restriction issue. The code controls depend on user supply data and attacker can bypass login controls with only providing "Cookie: user=Administrator" and "Cookie: loggedin=true" together. https://cwe.mitre.org/data/definitions/287.html