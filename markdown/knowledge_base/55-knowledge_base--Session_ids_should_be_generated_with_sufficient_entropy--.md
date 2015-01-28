
Session ids should be generated with sufficient entropy  

-------


**Description:**

Whenever session ids are not generated with a sufficient entropy this could lead to a session collision or session hijacking.


**Solution:**

The WebLogic deployment descriptor should specify a session identifier length of at least 128 bits. A shorter session identifier leaves the application open to brute-force session guessing attacks. If an attacker can guess an authenticated user's session identifier, he can take over the user's session. The remainder of this explanation will detail a back-of-the-envelope justification for a 128 bit session identifier.

The expected number of seconds required to guess a valid session identifier is given by the equation:

2B + 1
______
2A * S

Where:

    B is the number of bits of entropy in the session identifier

    A is the number of guesses an 
attacker can try each second

    S is the number of valid session identifiers that are valid and available to be guessed at any given time 	