## Description:

Verifying Appropriate Authentication

MSTG-AUTH-1: If the app provides users access to a remote service, some form of authentication, such as username/password authentication, is performed at the remote endpoint.

Authentication bypass vulnerabilities exist when authentication state is not consistently enforced on the server and when the client can tamper with the state. While the backend service is processing requests from the mobile client, it must consistently enforce authorization checks: verifying that the user is logged in and authorized every time a resource is requested.


## Mitigation:

Perform the following steps when testing authentication and authorization:

	- Identify the additional authentication factors the app uses.
	- Locate all endpoints that provide critical functionality.
	- Verify that the additional factors are strictly enforced on all server-side endpoints.
