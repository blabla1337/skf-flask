##Description:

Always enforce multiple layers of security whenever you want to protect sensitive data/files
on your application. If one layer should fail the other layers should prevent the attackers
from succeeding.

##Mitigation:

Whenever sensitive data is stored on the server store the data in a separate folder with permission rules in order to prevent unauthorized users from reading the files. As an in-depth solution, you could also check if the session of the user has sufficient privileges to read the files according to the level of authorization.
Recommended knowledge base item:
•	Missing authentication or authorization
•	Sanitize sensitive data rapidly from memory

