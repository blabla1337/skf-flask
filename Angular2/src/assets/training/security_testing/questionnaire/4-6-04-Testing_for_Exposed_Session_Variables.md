# Question

Decide if the given statmen is true or false.

"Encryption or cryptographic hashing of the Session ID should be considered separately from transport encryption."

* ( ) True
* ( ) False

-----SPLIT-----

# Answer

* (x) True
* ( ) False

Explanation: Encryption or cryptographic hashing of the Session ID only allows the Session ID itself being protected, not the data that may be represented by it.

-----SPLIT-----


# Question

Decide if the given statmen is true or false.

"The cryptographically secure Session ID cannot be stolen/captured in a communication that uses HTTP Protocol"

* ( ) True
* ( ) False

-----SPLIT-----

# Answer

* ( ) True
* (x) False

Explanation: In general, the Session ID should never be sent over unencrypted transport and should never be cached. The application should be examined to ensure that encrypted communications are both the default and enforced for any transfer of Session IDs

-----SPLIT-----