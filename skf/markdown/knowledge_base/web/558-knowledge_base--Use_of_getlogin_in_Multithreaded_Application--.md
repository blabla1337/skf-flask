## Description:

The application uses the getlogin() function in a multithreaded context, potentially causing it to return incorrect values.

The getlogin() function returns a pointer to a string that contains the name of the user associated with the calling process. The function is not reentrant, meaning that if it is called from another process, the contents are not locked out and the value of the string can be changed by another process. This makes it very risky to use because the username can be changed by other processes, so the results of the function cannot be trusted.

## Mitigation:


PHASE:Architecture and Design:
Using names for security purposes is not advised. Names are easy to forge and can have overlapping user IDs, potentially causing confusion or impersonation.

PHASE:Implementation:
Use getlogin_r() instead, which is reentrant, meaning that other processes are locked out from changing the username.

