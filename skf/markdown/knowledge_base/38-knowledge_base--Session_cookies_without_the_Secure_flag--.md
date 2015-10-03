
Session cookies without the Secure flag
-------

**Description:**

The secure flag is an option that can be set when creating a cookie. 
This flag ensures that the cookie will not be sent over an unencrypted 
connection by the browser. 
Which ensures that the session cookie can not be send over a non-encrypted link.


**Solution:**

When creating a session cookie which is send over an encrypted connection 
you should set the secure flag. The Secure flag should be set during every set-cookie. 
This will instruct the browser to never send the cookie over HTTP. 
The purpose of this flag is to prevent the accidental exposure of a cookie value if a user
follows an HTTP link. 
