## Description:

Imagine the scenario where you have a login form and an application which supports HTTPS.
Whenever the initial connection (login.php) is not HTTPS and after login (loggedin.php)
will be HTTPS the username and password will not be sent through an encrypted manner thus
could be easily compromised by attackers. This principle also applies to sending
vulnerable data towards other unencrypted/weak encrypted links in your application.

## Solution:

Verify that credentials or other sensitive information is transported via TLS.
