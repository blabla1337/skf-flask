
Password forget function - pattern
-------

**Description:**

Whenever you are implementing a forgot password function into your system there are 
a few things you need to take into consideration in order to prevent security flaws
in your application.

1. Forget password functions
2. Denial of service by locking out accounts 
3. Username enumeration
4. Does The application enforce the use of secure passwords 
5. Disallow the use of old passwords 


**Solution:**

The first thing is to verify that forgot password and other recovery paths
send a link including a time-limited activation token rather than the password itself. 

Additional authentication based on soft-tokens 
(e.g. SMS token, native mobile applications, etc.) can be required as well before 
the link is sent over.

Second, you should not lock out the users account whilst the process of getting a new 
password is in progress. This could lead to a Denial of service attack whenever an
attacker decides to intentionally lock out the users with an automated attack.

Third, whenever the new password request was set in progress, the message you display
should be generalised in order to prevent username enumeration.

Fourth, always disallow the use of old passwords and implement a strong password policy.
