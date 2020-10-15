##Description:

Client side storage also known as Offline Storage or Web Storage. The Underlying storage mechanism may vary from one
user agent to the next. In other words, any authentication your application requires can
be bypassed by a user with local privileges to the machine on which the data is stored.
Therefore, it's recommended not to store any sensitive information in local storage.

##Mitigation:

Verify that authenticated data is cleared from client storage, such as the browser DOM, after the
session is terminated. This also goes for other session and local storage information which could
assist an attacker launching an successful attack.

Verify that data stored in client side storage (such as HTML5 local storage, session storage, IndexedDB, regular
cookies or Flash cookies) does not contain sensitive data or PII (personal identifiable information).


