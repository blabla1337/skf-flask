##Description:

The error messages that are displayed when a user fails to login into an application
should be selected with caution. When this error message gives away too much information,
this information can be exploited by a hacker.

## Solution:

The application should never publish available usernames. When an attacker gains this
information he increases his attack vector and reduces the time
required to identify accounts.

I.e:

Imagine a forgot password function where the user enters his username in order for the
application to send a new password to his email address, the user enters a correct username
and the application responds with:

“Email successfully sent to your email address.” When the user enters an incorrect username it says,  “Error: user does not exist.”

This function would be vulnerable to username enumeration
