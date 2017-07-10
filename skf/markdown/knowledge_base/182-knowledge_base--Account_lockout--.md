## Description:

All applications should contain the possibility to lock down accounts for whenever it
detects attacks by/on users. Also you should include options for both soft and hard
lock-out mechanisms.

## Solution:

Soft lock-out:
This can be a good option for protecting your users against brute force attacks.
For example, whenever the user enters a wrong password three times, the application could
lock down the account for a minute in order to slow down the process of brute forcing his
password making it less profitable for the attacker to proceed. If u were to implement
hard lock-out countermeasures for this example you would achieve a "Dos" by permanently
locking out accounts.

Hard lock-out:
This type of lockout should be applied whenever you detect a user attacking your
application and counter him by means of permanently locking out his account until a
response team had time to do their forensics. After this process you can decide to
give the user back his account or take further legal actions against him.
This type of approach prevents the attacker from further penetrating your application
and infrastructure.

Note: 
Be cautious that a soft-lockout countermeasure does not override a hard-lockout status.


