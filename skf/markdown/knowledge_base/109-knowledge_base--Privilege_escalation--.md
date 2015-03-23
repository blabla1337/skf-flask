
Privilege escalation
-------

**Description:**

In every portion of the application where a user can create information in the database 
(e.g., making a payment, adding a contact, or sending a message), then he can receive 
information (statement of account, order details, etc.), or delete information 
(drop users, messages, etc.), it is necessary to record that functionality. 
The tester should try to access such functions as another user in order to verify if it is 
possible to access a function that should not be permitted by the users role/privilege 
(but might be permitted as another user). 


**Solution:**

Checking if a user has enough authorisation to execute certain request should always be 
enforced on the server-side. Also you may to apply the Principle of Least privilege, 
the principle of least privilege recommends that accounts have the least amount of 
privilege required to perform their business processes. This encompasses user rights, 
resource permissions such as CPU limits, memory, network, and file system permissions. 
For example, if a user server only requires access to the network, read access to a 
database table, and the ability to write to a log, this describes all the permissions 
that should be granted. Under no circumstances should the user be granted administrative 
privileges. Also for making testing easier you can create Unit-tests that verifies the 
user role permissions.

	