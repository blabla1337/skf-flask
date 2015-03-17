
Session ids should be generated with sufficient entropy  
-------

**Description:**

Whenever session ids are not generated with a sufficient entropy this could lead to a 
session collision or session hijacking.


**Solution:**

The WebLogic deployment descriptor should specify a session identifier length of at 
least 128 bits. A shorter session identifier leaves the application open to 
brute-force session guessing attacks. If an attacker can guess an authenticated user's 
session identifier, he can take over the user's session. 