## Description:

Authorization models

MSTG-AUTH-12: Authorization models should be defined and enforced at the remote endpoint.

Authorization is the process where requests to access a particular resource should be granted or denied. It should be noted that authorization is not equivalent to authentication - as these terms and their definitions are frequently confused. Authentication is providing and validating identity. The authorization includes the execution rules that determine which functionality and data the user (or Principal) may access, ensuring the proper allocation of access rights after authentication is successful.

It can be summarized as:
	"The requested **action** is **permitted** at this **time** for this **identity**"

Where:
	- **Identity** is _assured_ when the requester is challenged at the time they make the request, which means they have just fulfilled a challenge/response mechanism to verify they are who they claim, in terms of identity. If the challenge occurred before the request there is no assurance, acknowledging there may be a trusted session, but without assurance through via _challenge_ there can only be an unverified identity making this request
	- **Action** The purpose for an authorization mechanism, a requester is attempting to perform an action that is sensitive, requires elevated privileges, or has some other implication like user privacy or _material_ impacts to the business.
	- **Permitted** means the identity has been checked for permission to perform the action, using Access Controls.
	- **Time** is extremely meaningful for the security characteristics of Authorization because it is the responsibility of the server to verify that the request is being processed _now_ and that is when the request was made. If it was made earlier being replayed now, or has been time skewed to a future time, the server should reject the request as it is not relevant to the current Authorization context.


## Mitigation:

Authorization plays an important role for application security and all controls must be implemented on the server because client-side controls are easily bypassed.