
Production passwords stored alongside the source code.
-------

**Description:**

Sometimes when developing an application a programmer stores a password or other 
credentials into the source-code as a comment for other developers to 
login into the application. When these comments still exist in a live environment, 
an attacker could use these credentials to gain access to the system.


**Solution:**

Search your source code for comments which contains possible user-credentials.

	