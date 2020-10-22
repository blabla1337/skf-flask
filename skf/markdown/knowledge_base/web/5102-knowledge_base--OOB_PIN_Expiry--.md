## Description:

If an application allows the user to attempt for out-of-band authentication after a set time interval, it increases the chance of an attacker to replay a valid out-of-band authentication key after successfully compromising the session.


## Solution:

The most effective solution is to reject out of band authentication attempts after 10 minutes and also ensure the out-of-band authentication key can be used only once.
