##Description:

Authenticating a user, or otherwise establishing a new user session, without invalidating any existing session identifier gives an attacker the opportunity to steal authenticated sessions.

Such a scenario is commonly observed when: 1. A web application authenticates a user without first invalidating the existing session, thereby continuing to use the session already associated with the user. 2. An attacker is able to force a known session identifier on a user so that, once the user authenticates, the attacker has access to the authenticated session. 3. The application or container uses predictable session identifiers. In the generic exploit of session fixation vulnerabilities, an attacker creates a new session on a web application and records the associated session identifier. The attacker then causes the victim to associate, and possibly authenticate, against the server using that session identifier, giving the attacker access to the user's account through the active session.

##Mitigation:


PHASE:Architecture and Design:
Invalidate any existing session identifiers prior to authorizing a new user session.

PHASE:Architecture and Design:
For platforms such as ASP that do not generate new values for sessionid cookies, utilize a secondary cookie. In this approach, set a secondary cookie on the user's browser to a random value and set a session variable to the same value. If the session variable and the cookie value ever don't match, invalidate the session, and force the user to log on again.

