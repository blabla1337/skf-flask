
Regular expression injection
-------

**Description:**

If the application uses regular expressions which receives user input, 
then the user input should be properly escaped. 
If not done properly then the hacker can affect the regular expression and modify their 
logic. In some cases, an attacker could even gain access to the server


**Solution:**

Do not use user-input without escaping in a regular expression.
	