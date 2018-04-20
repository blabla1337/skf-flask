## Description:

When working with sessions there are a couple of things you need to consider in order to implement them securely throughout your system. For more detailed information about these items you should check the knowledge-base about:
1.	Session management control
2.	Session cookies without the Secure flag
3.	Session cookies without the HTTP Only flag
4.	External session hijacking
5.	Insecure transmission of session cookies
6.	Session information is not stored server side
7.	Session ids should be generated with sufficient entropy, the preferred method is the frameworks default session management control implementation is used by the application
8.	User generated session ids should be rejected by the server
9.	The logout functionality should revoke the complete session
10.	The login functionality should always generate (and use) a new session id
11.	Session IDs do not timeout.(idle)
12.	Absolute session timed out
13.	Verify that the session id is never disclosed
14.	Session cookies (Domain)

## Solution:

The items as pointed out before should be looked into and taken into consideration
whenever you are working with sessions on your system in order to enforce a
high level of security.

Though there are more than ten design patterns related to session, all of them need to be implemented. 
If any one is left out for implementation, the whole session management layer is not secure and could be defeated by attackers.
