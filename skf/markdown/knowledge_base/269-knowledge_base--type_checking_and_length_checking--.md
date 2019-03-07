## Description

Type checking, length checking and whitelisting is an essential in defense in depth strategie to make
your application more resiliant against input injection attacks.

Example:
    ```
    SELECT * FROM pages WHERE id=mysql_real_escape_string($_GET['id'])
    ```
    
This PHP example did effectively not mitigate the SQL injection. This was due to the fact
that it only escaped string based SQL injection. 

Now, if this application also had additional checks to validate if the value of 
the $_GET['id'] parameter was indeed as expected an integer and rejected if this condition was false, 
the attack would effectively been mitigated.


## Solution

All the user supplied input that works outside of the intended opteration of the application
should be rejected by the application.
