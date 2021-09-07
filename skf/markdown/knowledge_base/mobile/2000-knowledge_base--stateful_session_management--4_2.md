## Description:

Stateful Session Management

MSTG-AUTH-2: If stateful session management is used, the remote endpoint uses randomly generated session identifiers to authenticate client requests without sending the user’s credentials.

Stateful (or "session-based") authentication is characterized by authentication records on both the client and server. The authentication flow is as follows:

	1. The app sends a request with the user's credentials to the backend server.
	2. The server verifies the credentials If the credentials are valid, the server creates a new session along with a random session ID.
	3. The server sends to the client a response that includes the session ID.
	4. The client sends the session ID with all subsequent requests. The server validates the session ID and retrieves the associated session record.
	5. After the user logs out, the server-side session record is destroyed and the client discards the session ID.

When sessions are improperly managed, they are vulnerable to a variety of attacks that may compromise the session of a legitimate user, allowing the attacker to impersonate the user. This may result in lost data, compromised confidentiality, and illegitimate actions.


## Mitigation:

Session Management Best Practices

Locate any server-side endpoints that provide sensitive information or functions and verify the consistent enforcement of authorization. The backend service must verify the user's session ID or token and make sure that the user has sufficient privileges to access the resource. If the session ID or token is missing or invalid, the request must be rejected.

Make sure that:

	- Session IDs are randomly generated on the server side.
	- The IDs can't be guessed easily (use proper length and entropy).
	- Session IDs are always exchanged over secure connections (e.g. HTTPS).
	- The mobile app doesn't save session IDs in permanent storage.
	- The server verifies the session whenever a user tries to access privileged application elements, (a session ID must be valid and must correspond to the proper authorization level).
	- The session is terminated on the server side and session information deleted within the mobile app after it times out or the user logs out.

Authentication shouldn't be implemented from scratch but built on top of proven frameworks. Many popular frameworks provide ready-made authentication and session management functionality. If the app uses framework APIs for authentication, check the framework security documentation for best practices. 
