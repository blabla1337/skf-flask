## Description:

You should keep track of all the different active concurrent sessions.
Whenever the application discovers concurrent sessions it should always notify the user
about this and should give him the opportunity to end the other sessions.

With this defense in place it becomes harder for attackers to hijack a users session since
they will be notified about concurrent sessions.

## Solution:

The application should keep track and limit all the granted sessions.
It should store your users IP address, session id and user id. After storing these credentials
it should do regular checks to see if there are:

1. Multiple active sessions linked to same user id
2. Multiple active sessions from different locations
3. Multiple active sessions from different devices
4. Limit and destroy sessions when they exceed an accepted threshold.

The more critical the application becomes the lower the accepted threshold for
concurrent sessions should be.


