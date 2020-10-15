##Description:

The secure flag is an option that can be set when creating a cookie.
This flag ensures that the cookie will not be sent over an unencrypted
connection by the browser,which ensures that the session cookie can not be sent over a non-encrypted link.

##Mitigation:

When creating a session cookie which is sent over an encrypted connection
you should set the secure flag. The Secure flag should be set during every set-cookie.
This will instruct the browser to never send the cookie over HTTP.
The purpose of this flag is to prevent the accidental exposure of a cookie value if a user
follows an HTTP link.


