##Description:

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


##Mitigation:

All the user supplied input that works outside of the intended opteration of the application
should be rejected by the application.

Syntax and Semantic Validity
An application should check that data is both syntactically and semantically 
valid (in that order) before using it in any way (including displaying it back to the user). 

Syntax validity, means that the data is in the form that is expected. For example, an application
may allow a user to select a four-digit “account ID” to perform some kind of operation. 
The application should assume the user is entering a SQL injection payload, and should 
check that the data entered by the user is exactly four digits in length, and consists only of numbers 
(in addition to utilizing proper query parameterization).

Semantic validity, includes only accepting input that is within an acceptable range for the
given application functionality and context. For example, a start date must be before an end
date when choosing date ranges.

