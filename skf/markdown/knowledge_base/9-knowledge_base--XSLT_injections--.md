
XSLT injections
-------

**Description:**

The vulnerability occurs when a XSL file is loaded from a source controlled by an attacker.
When the attacker is given the opportunity to specify the source of the included XSL file
he could include a file which contains malicious code to be parsed on the target application.
This could lead to, code execution, reading arbitrary files and many more
vulnerabilities such as XSS.


**Solution:**

To protect against such vulnerability one needs to make sure that he does not use 
user-supplied input in the XSL filename. 
The best solution would be to define a list of permitted filenames and 
only accept XSL filenames from that list.

	