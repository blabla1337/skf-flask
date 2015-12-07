Client side storage
-------

**Description:**

Also known as Offline Storage, Web Storage. Underlying storage mechanism may vary from one
user agent to the next. In other words, any authentication your application requires can
be bypassed by a user with local privileges to the machine on which the data is stored.
Therefore, it's recommended not to store any sensitive information in local storage.

**Solution:**

Verify that authenticated data is cleared from client storage, such as the browser DOM, after the 
session is terminated. This also goed for other session and local storage information which could
assist an attacker launching an succesfull attack.

Recommended knowledge base items:

- HTML5 caching