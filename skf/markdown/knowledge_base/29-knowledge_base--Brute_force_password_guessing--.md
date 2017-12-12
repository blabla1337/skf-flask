## Description:

Login functions should not be abused in an automated way that an attacker could create a
script that contains a list of usernames and passwords, which he could use against your
login function in order to gain unauthorized access to user accounts.

## Solution:

Implement a method that limits the amount of tries with automated tools.
Some examples are using a CAPTCHA or a TARPIT(rate-limiting) method.

Be aware that a simple limitation on number of tries may be used as a method to perform denial-of-service attack and hence to block certain users like system administrator from logging in. A combination of tries limit and challenge-response test can be used to prevent this risk while providing convenience for actual user login. For example, start to ask user to complete a CAPTCHA or a TARPIT question during login after a certain number of tries is reached.
