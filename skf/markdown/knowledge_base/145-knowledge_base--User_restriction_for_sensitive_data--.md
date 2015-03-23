
User restriction for sensitive data
-------

**Description:**

Aways enforce multiple layers of security whenever you want to protect sensitive data/files 
on your application. If one layer should fail the other layers should prevent the attackers 
from succeeding.


**Solution:**

Whenever sensitive data is stored on the server you should consider storing this data in 
a separate folder with permission rules in order to prevent unauthorised users to 
read these files. As an in depth solution you could also check if the session of the user 
has sufficient privileges to read the files according to the level of authorisation.

	