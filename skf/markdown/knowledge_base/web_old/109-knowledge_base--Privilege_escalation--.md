##Description:

Attackers with low access rights wil always try to elevate their privileges in order to get more sensitive information/functionalities at their disposal. This can be achieved by for example:

 - Functions that fail to check authorization
 - Compromised functions/services that run with higher privileges
 - Compromised user accounts with higher privileges

These examples just scratch the surface of what attackers will try in order to elevate their privilages on your application/system. Therefore it is very important to take this reccomendation high into account.

## Solution:

Checking if a user has enough authorization to execute certain request should always be enforced on the server-side. Also, you may apply the Principle of Least privilege, the principle of least privilege recommends that accounts have the least amount of privilege required to perform their business processes. This encompasses user rights, resource permissions such as CPU limits, memory, network, and file system permissions. For example, if a user only requires access to the network, read access to a database table, and the ability to write to a log, this describes all the permissions that should be granted. Under no circumstances should the user be granted administrative privileges. 
