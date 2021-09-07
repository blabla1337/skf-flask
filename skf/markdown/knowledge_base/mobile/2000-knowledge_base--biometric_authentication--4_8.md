## Description:

Biometric Authentication

MSTG-AUTH-8: Biometric authentication, if any, is not event-bound (i.e. using an API that simply returns “true” or “false”). Instead, it is based on unlocking the keychain/keystore.

Biometric authentication is a convenient mechanism for authentication, but also introduces an additional attack surface when using it.

The are a number of common types of biometrics that are used, including:
	- Fingerprint scans
	- Facial recognition
	- Iris scans
	- Handprint scans


## Mitigation:

Follow vendor's best practices if it is needed, and avoid of building your own biometric authentication mechanism.