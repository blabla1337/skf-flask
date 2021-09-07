## Description:

Password brute-forces

MSTG-AUTH-6: The remote endpoint implements a mechanism to protect against the submission of credentials an excessive number of times.

A brute-force attack is an attempt to discover a password by systematically trying every possible combination of letters, numbers, and symbols until you discover the one correct combination that works. 

An attacker can always discover a password through this method, but the downside is that it could take years to find it. Depending on the password’s length and complexity, there could be trillions of possible combinations.


## Mitigation:

Some anti-brute-force controls:
	- Multifactor authentication (MFA), or Two-Factor Authentication (2FA) is when a user is required to present more than one type of evidence in order to authenticate on a system. It is by far the best defence against the majority of password-related attacks.
	- Account Lockout is the most common protection against these attacks. After a few unsuccessful login attempts, targeted accounts should be locked (temporarily or permanently), and additional login attempts should be rejected.
	- The use of an effective CAPTCHA can help to prevent automated login attempts against accounts. However, many CAPTCHA implementations have weaknesses that allow them to be solved using automated techniques or can be outsourced to services which can solve them. As such, the use of CAPTCHA should be viewed as a defence-in-depth control to make brute-force attacks more time consuming and expensive, rather than as a preventative.
	- Security Questions and Memorable Words can also help protect against automated attacks, especially when the user is asked to enter a number of randomly chosen characters from the word. 

These controls must be implemented on the server because client-side controls are easily bypassed.