
Session IDs do not timeout (idl)
-------

**Description:**

All sessions should implement an idle or inactivity timeout. 
This timeout defines the amount of time a session will remain active in case there is no 
activity in the session, closing and invalidating the session upon the defined idle period 
since the last HTTP request received by the web application for a given session ID. 
The idle timeout limits the chances an attacker has to guess and use a valid session ID 
from another user. However, if the attacker is able to hijack a given session, 
the idle timeout does not limit the attacker&#39;s actions, as he can generate activity on 
the session periodically to keep the session active for longer periods of time. 

Session timeout management and expiration must be enforced server-side. If the client is 
used to enforce the session timeout, for example using the session token or other client 
parameters to track time references (e.g. number of minutes since login time), an attacker 
could manipulate these to extend the session duration.


**Solution:**

Al user sessions should time-out based on logic server-side in order to decrease an 
attackers attack vector.

	