
Too verbose authentication-failure logging
-------

**Description:**

The error messages that are displayed when a user fails to login into an application should selected with caution. When this error message gives away too much information, this information can be exploited by a hacker.


**Solution:**

The application should never publish available usernames. When an attacker gains this information he increases his attack vector and reduces the time required to identify accounts.

i.e:

Imagine an "forgot password" function where the user enters his username in order for the application to send a new password to his email adress, the user enters a correct username and the application reply's with:

<b>Email succesfully send to your email adress.</b><br>
when the user enters a incorrect username it says.<br>
<b>Error: user does not exsist.</b><br>

This function would be vulnerable to username enumeration

	