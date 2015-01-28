
Open forward & Open redirects
-------


**Description:**

An open forward is an application that takes a parameter and forwards a user to another part of the application without any validation or access control checks. This may allow an attacker to bypass access control checks, especially those enforced externally, such as by a web server. 

An open redirect is an application that takes a parameter and redirects a user to the parameter value without any validation. This vulnerability is used in phishing attacks to get users to visit malicious sites without realizing it. 


**Solution:**

Safe use of redirects and forwards can be done in a number of ways:

1.
Simply avoid using redirects and forwards.

2.
If used, do not involve user parameters in calculating the destination. This can usually be done.

3.
If destination parameters can not be avoided, ensure that the supplied value is valid, and authorized for the user.
It is recommended that any such destination parameters be a mapping value, rather than the actual URL or portion of the URL, and that server side code translate this mapping to the target URL.

4. 
Use a whitelisting method for determining where the user should be redirected towards.

Avoiding such flaws is extremely important as they are a favorite target of phishers trying to gain the users trust. 	