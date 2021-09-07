## Description:

Device-Access-Security Policy

MSTG-STORAGE-11: The app enforces a minimum device-access-security policy, such as requiring the user to set a device passcode.

Apps that process or query sensitive information should run in a trusted and secure environment. 


## Mitigation:

To create this environment, the app can check the device for the following:
	- PIN or password-protected device locking
	- Recent OS version
	- Debugging activation
	- Device encryption
	- Device rooting/jail breaking