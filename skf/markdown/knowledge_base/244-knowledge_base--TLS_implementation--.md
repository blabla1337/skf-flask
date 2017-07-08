## Description:

Whenever sensitive information is being sent over the application TLS must be applied in the application
to prevent malicious attackers eavesdropping the network can look into and manipulate this
sensitive information.


## Solution:

Verify that TLS is used for all connections (including both external and backend connections) 
that are authenticated or that involve sensitive data or functions, and does not fall back to
insecure or unencrypted protocols. Ensure the strongest alternative is the preferred algorithm.

As modern cryptography relies on being computationally expensive to break, specific standards can be set for
key sizes that will provide assurance that with today’s technology and understanding, it will take too long
to decrypt a message by attempting all possible keys.

Therefore, we need to ensure that both the algorithm and the key size are taken into account when selecting
an algorithm. Whenever computer power increases the standards for selecting a new alogrithm changes as well.
