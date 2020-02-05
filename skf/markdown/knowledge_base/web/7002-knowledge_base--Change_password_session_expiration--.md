## Description:

In case the user session is not terminated after a major user profile modification such as a role modification or password change, the user session and profile won't be in the most updated state. If the user password is compromised, an attacker will be able to operate the application on behalf of the user while the session remains valid, even after the password is changed.


## Solution:

After a successful password change process, terminate all other active sessions, and this is effective across the application, federated login (if present) and any relying parties.
