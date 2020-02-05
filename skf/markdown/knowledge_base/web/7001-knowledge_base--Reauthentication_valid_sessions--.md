## Description:

If the application allows the user to remain authenticated for a long period of time, for example "Stay logged in" functionality, which prolongs user session longer than the regular server-side timeouts, it increases the chance of an attacker to replay a valid session after successfully compromising the session. 


## Solution:

Implement periodical re-authentication both when actively used or after an idle period, making sure the session identifiers are also renewed.
Level 1 - 30 days
Level 2 - 12 hours or 30 minutes of inactivity, 2FA optional
Level 3 - 12 hours or 15 minutes of inactivity, with 2FA
