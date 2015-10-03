
HTTPS and weakly or unencrypted links
-------

**Description:**

Imagine the scenario where you have a login form and an application which supports HTTPS. 
Whenever the initial connection (login.php) is not HTTPS and after login (loggedin.php) 
will be HTTPS the username and password will not be send through an encrypted manner thus 
could be easily compromised by attackers. This principle also applies to sending 
vulnerable data towards other unencrypted/weak encrypted links in your application. 


**Solution:**

Do not traverse unencrypted or weakly encrypted links.
As soon as you allow a single connection to be send over unencrypted lines, the
integrity and confidentiality of your data can no longer be guaranteed.



 