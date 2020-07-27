##Description:

If accounts for communicating between components have granted more privileges than
necessary, these accounts could impose a great threat whenever one of these components gets
compromised by attackers. 

i.e:
A web application running on root privileges which has a path traversal vulnerability
can be used to read both the "etc/passwd" file as well as reading the "etc/shadow" file.

These files can then be used in an offline password cracking attacks to recover accounts
on the server.

## Solution:

Communications between components, such as between the application server and the database 
server should be authenticated using an account with the least necessary privileges.
