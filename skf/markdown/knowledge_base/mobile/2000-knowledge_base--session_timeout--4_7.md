## Description:

Session Timeout

MSTG-AUTH-7: Sessions are invalidated at the remote endpoint after a predefined period of inactivity and access tokens expire.

In order to minimize the time period an attacker can launch attacks over active sessions and hijack them, it is mandatory to set expiration timeouts for every session, establishing the amount of time a session will remain active. Insufficient session expiration by the app increases the exposure of other session-based attacks, as for the attacker to be able to reuse a valid session ID and hijack the associated session, it must still be active.


## Mitigation:

The shorter the session interval is, the lesser the time an attacker has to use the valid session ID. The session expiration timeout values must be set accordingly with the purpose and nature of the app, and balance security and usability, so that the user can comfortably complete the operations within the application without his/her session frequently expiring.