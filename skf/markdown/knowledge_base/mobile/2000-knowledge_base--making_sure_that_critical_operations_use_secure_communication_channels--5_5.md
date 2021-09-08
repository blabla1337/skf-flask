## Description:

Making Sure that Critical Operations Use Secure Communication Channels

MSTG-NETWORK-5: The app doesn’t rely on a single insecure communication channel (email or SMS) for critical operations, such as enrollments and account recovery.

For sensitive applications like banking apps, [OWASP MASVS](https://github.com/OWASP/owasp-masvs/blob/master/Document/0x03-Using_the_MASVS.md "The Mobile Application Security Verification Standard") introduces "Defense in Depth" verification levels. The critical operations (e.g., user enrolment and account recovery) of such applications are some of the most attractive targets to attackers. This requires implementation of advanced security controls, such as additional channels to confirm user actions without relying on SMS or email.

Note that using SMS as an additional factor for critical operations is not recommended. Attacks like SIM swap scams were used in many cases to [attack Instagram accounts, cryptocurrency exchanges](https://motherboard.vice.com/en_us/article/vbqax3/hackers-sim-swapping-steal-phone-numbers-instagram-bitcoin "The SIM Hijackers") and of course [financial institutions](https://www.fintechnews.org/sim-swapping-how-the-mobile-security-feature-can-lead-to-a-hacked-bank-account/ "SIM swapping") to bypass SMS verification. SIM swapping is a legitimate service offered by many carriers to switch your mobile number to a new SIM card. If an attacker manages to either convince the carrier or recruits retail workers at mobile shops to do a SIM swap, the mobile number will be transferred to a SIM the attacker owns.  As a result of this, the attacker will be able to receive all SMS and voice calls without the victim knowing it.

There are different ways to [protect your SIM card](https://www.wired.com/story/sim-swap-attack-defend-phone/ "How to protect yourself against a SIM swap attack"), but this level of security maturity and awareness cannot be expected from a normal user and is also not enforced by the carriers. 

Also the usage of emails shouldn't be considered as a secure communication channel. Encrypting emails is usually not offered by service providers and even when available not used by the average user, therefore the confidentiality of data when using emails cannot be guaranteed. Spoofing, (spear|dynamite) phishing and spamming are additional ways to trick users by abusing emails. Therefore other secure communication channels should be considered besides SMS and email.


## Mitigation:

Review the code and identify the parts that refer to critical operations. Make sure that additional channels are used for such operations. The following are examples of additional verification channels:

	- Token (e.g., RSA token, YubiKey),
	- Push notification (e.g., Google Prompt),
	- Data from another website you have visited or scanned (e.g. QR code) or
	- Data from a physical letter or physical entry point (e.g., data you receive only after signing a document at a bank).

Make sure that critical operations enforce the use of at least one additional channel to confirm user actions. These channels must not be bypassed when executing critical operations. If you're going to implement an additional factor to verify the user's identity, consider also one-time passcodes (OTP) via [Google Authenticator](https://github.com/google/google-authenticator-android "Google Authenticator for Android").
