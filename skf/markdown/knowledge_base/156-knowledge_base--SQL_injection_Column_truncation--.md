
Column truncation sql injection
-------

**Description:**

Whenever an applications structural logic mismatches with the database structural logic
an attacker gains the opportunity to truncate his submit towards your database column by
submitting a value longer then the limit allowed in the database. 

Imagine you have a system where users can register themselves.

The attacker can abuse this behaviour of the database to overflow the length limit 
and truncate his submit and register himself as the admin, thus gaining its 
privileges.




**Solution:**

On critical places where unique values are enforced and expected 
such as usernames in order to authorise or distribute certain privileges. The users submit
should be checked on the server side in order to verify if it does not exceed the limit
set in your database. 


