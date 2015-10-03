
The login functionality should always generate (and use) a new session id  
-------

**Description:**

Whenever an user is successfully authenticated the application should generate a 
new session cookie.


**Solution:**

The login functionality should always generate (and use) a new session id after a 
successful login. This is done to prevent an attacker doing a session fixation attack
on your users. 

Some frameworks do not provide the possibility to change the session id on login such as
.net applications. Whenever this problem occurs you could set an extra random cookie on 
login  with a strong token and store this value in a session variable.

Now you can compare the cookie value with the session variable in order to prevent
session fixation since the authentication does not solely relies on the session id since
the random cookie can not be predicted or fixated by the attacker.







	
