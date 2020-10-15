##Description:

The application should always generate session IDs with a sufficient level of entropy.
The goal to use randomly generated values for tokens is that of preventing session collision or session hijacking. If an attacker can guess an authenticated user's session identifier, he can take over the user's session. Moreover, an attacker that breaks the algorithm logic behind the session IDs generation might be able to arbitrary craft valid session tokens for any user.


##Mitigation:

Verify that session tokens are created using approved cryptographic algorithms with more than 64 bits of entropy. As a Developer you should rely on functionalities provided by the framework. If not present, always refer to Secure Random Number functions provided by the programming language libraries.
