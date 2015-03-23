
Brute-force password guessing
-------

**Description:**

Login functions should not abused in an automated way that an attacker could create a 
script that contains a list of usernames and passwords, which he could use against your 
login function in order to gain unauthorised access to user accounts.


**Solution:**

Implement a method that limit the amount of tries with automated tools. 
Some examples are a CAPTCHA or a tarpit.

	