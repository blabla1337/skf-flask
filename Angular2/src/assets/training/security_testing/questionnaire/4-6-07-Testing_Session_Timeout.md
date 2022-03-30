# Question

Decide if the given statmen is true or false.

"Session timeout defines the amount of time a session will remain active in case there is no activity by the user, closing and invalidating the session upon the defined idle period since the last HTTP request received by the web application for a given session ID. "

* ( ) True
* ( ) False

-----SPLIT-----

# Answer

* (x) True
* ( ) False


-----SPLIT----


# Question

Decide if the given statmen is true or false.

"Session timeout management and expiration must be enforced client-side."

* ( ) True
* ( ) False

-----SPLIT-----

# Answer

* ( ) True
* (x) False


Explanation: Session timeout management and expiration must be enforced server-side.

-----SPLIT----


# Question

Which of the followings actions need to check while testing session timeout? Can choose multiple answers.

* ( ) The log out function effectively destroys all session token, or at least renders them unusable,
* ( ) The server performs proper checks on the session state, disallowing an attacker to replay previously destroyed session identifiers
* ( ) A timeout is enforced and it is properly enforced by the server. If the server uses an expiration time that is read from a session token that is sent by the client (but this is not advisable), then the token must be cryptographically protected from tampering.
* ( ) None of the above

-----SPLIT-----

# Answer

* (x) The log out function effectively destroys all session token, or at least renders them unusable,
* (x) The server performs proper checks on the session state, disallowing an attacker to replay previously destroyed session identifiers
* (x) A timeout is enforced and it is properly enforced by the server. If the server uses an expiration time that is read from a session token that is sent by the client (but this is not advisable), then the token must be cryptographically protected from tampering.
* ( ) None of the above

-----SPLIT-----