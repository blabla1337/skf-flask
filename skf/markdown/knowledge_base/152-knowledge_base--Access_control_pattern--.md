
Access-control/Login systems - pattern
-------

**Description:**

For successful access control/login functionality there are a lot of things to take into
consideration before you start implementing these functions.



**Solution:**

If you design your access/login system with these items into consideration it will save you a 
lot of time not having to implement them afterwards.

1. Audit logs
2. Principle of least privilege (Privilege based authentication system)
3. Passwords must be encrypted, salted and stretched
4. Security flags
5. Cross-Site Request Forgery (CSRF for authenticated forms)
6. Brute force attack counter-measures

First, your users table in your database should contain some extra tables and rows for handling
the privilege based authentication system, as well as implementing a system for user lock-out when
your logging system detects a possible attacker.

Second, we want to build a logging system which also keeps track of possible attackers and 
locks-out users when they are actively attacking your system.

Third, we build a login system with strong password encryption, PDO prepared statements and set security flags
for the sessions in order to protect them against XSS and enforce them to be transmitted over
only encrypted data lines.

Fourth, we want to protect your login form against brute-force attacks.

And last, now that all the protection layers are in place we want to secure al our data transactions by means of 
CSRF tokens.

note: As soon as the user hits your application you want to enforce him using a https protected 
connection this can be done by including the Strict-Transport-Security header which looks like:

Strict-Transport-Security: max-age=31536000; includeSubDomains

Also you should consider adding your application to a HSTS Preload list for enforcing a higher
level of security.

