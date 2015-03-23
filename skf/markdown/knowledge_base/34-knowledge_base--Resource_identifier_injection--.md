
Resource identifier injection
-------

**Description:**

A resource identifier injection basically means that the attacker can determine which 
resources are loaded into the web application. 
An attacker could thus influence the operation of the web application and redirect users 
to other websites. This attack consists of changing resource identifiers used by an 
application in order to perform a malicious task. When an application permits a user 
input to define a resource, like a file name or port number, 
this data can be manipulated to execute or access different resources. 
In order to be properly executed, the attacker must have the possibility to specify a 
resource identifier through the application form and the application must permit the execution. 
The resource type affected by user input indicates the content type that may be exposed. 
For example, an application that permits input of special characters like period, slash, 
and backslash is risky when used in methods that interact with the file system. 
The resource injection attack focuses on accessing other resources than the local 
filesystem, which is different attack technique known as a Path Manipulation attack.


**Solution:**

Safe use of resource identifiers can be done by performing authorisation checks if the 
identifier is belonging to the user.
	