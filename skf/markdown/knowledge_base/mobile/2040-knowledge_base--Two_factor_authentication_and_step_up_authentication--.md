## Description:

Two-Factor Authentication and Step-up Authentication

MSTG-AUTH-9: A second factor of authentication exists at the remote endpoint and the 2FA requirement is consistently enforced.

MSTG-AUTH-10: Sensitive transactions require step-up authentication.

Two-factor authentication (2FA) is standard for apps that allow users to access sensitive functions and data. Common implementations use a password for the first factor and any of the following as the second factor:

	- One-time password via SMS (SMS-OTP)
	- One-time code via phone call
	- Hardware or software token
	- Push notifications in combination with PKI and local authentication


## Mitigation:

Whatever option is used as 2nd factor, it always must be enforced and verified on the server-side and never on client-side. Otherwise the 2nd factor can be easily bypassed within the app.

The secondary authentication can be performed at login or later in the user's session. For example, after logging in to a banking app with a username and PIN, the user is authorized to perform non-sensitive tasks. Once the user attempts to execute a bank transfer, the second factor ("step-up authentication") must be presented.
