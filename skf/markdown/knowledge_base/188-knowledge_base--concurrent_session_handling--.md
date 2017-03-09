# Concurrent session handling
-------

## Description:

You should limit and keep track of all the different active concurrent sessions.
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
3. Limit and destroy sessions if they become concurrent.

If so, the user should be notified and given the opportunity to end the other sessions.

A best practice would be to create a function which summarizes all the different active sessions
with the opportunity to terminate them at any given time.

As an extra layer of protection the user should also be prompted with the option to terminate all
active sessions whenever he:

1. changes his password
2. re-authenticates
3. does step up or adaptive authentication

Along with the renewal of the session identifier in these steps you now have full hardened defenses against
session hijacking attacks.

Recommended knowledge-base items:

- Session hijacking
- Session fixation
