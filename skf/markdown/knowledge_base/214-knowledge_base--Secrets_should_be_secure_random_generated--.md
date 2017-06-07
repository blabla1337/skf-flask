# Secrets should be secure random generated
-------

## Description:

Secret keys, API tokens, or passwords must be dynamically generated. Whenever these tokens
are not dynamically generated they can become predicable and used by attackers to compromise
user accounts. 

## Solution:

When it comes to API tokens and secret keys these values have to be dynamically generated 
and should be cryptographically random secure with at least 120 bit of effective entropy.

Passwords on the other hand should be created by the user himself, rather than assigning
a user a dynamically generated password. The user should be presented a link with a 
cryptographically random token by means of an email or SMS which is used to activate his 
account and provide a password of his own.
 
