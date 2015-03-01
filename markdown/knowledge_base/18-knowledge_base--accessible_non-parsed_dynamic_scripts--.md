
Accessible non-parsed dynamic scripts
-------

**Description:**

Applications often include files in other pages. When these files can be directly aproached by normal users, the operation of the application can be traced because the source code becomes available. This improves the possibility that the attacker discovers vulnerabilities.


**Solution:**

Always add the different types of extentions to the webserver handler to parse. This way the file source cannot be viewed.

	