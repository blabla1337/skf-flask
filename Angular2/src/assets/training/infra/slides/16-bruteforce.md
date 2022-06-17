## Brute Force Attack
Brute force attack consists of an attacker submitting many passwords or passphrases with the hope of eventually guessing correctly. The attacker systematically checks all possible passwords and passphrases until the correct one is found. It is a very time consuming method and trying all possible combinations may take a very long time. So attackers may generate a little bit smart dictionary list to try, for example: years (2020, 2021, 2022), months (May, June, July), default passwords, location and company related information, etc.

Some common testing tools:
* Burp Suite and Zap Proxy can be used for credential and directory brute forcing. They only supports HTTP protocol and do not work for others.
* hydra, nmap, ncrack, medusa, etc. are some example of online brute-forcing tools. They support various of network protocols and do quite similar jobs.
* john the ripper, hashcat, etc. are some example of offline brute-forcing tools. We can use them to crack hashes, passwords, etc.

And the target system should restrict user attempts with implementing:

* A proper password policy: complex password (upper case, lower case, special characters and numbers) with enough length
* Lockout policy: lock user accounts temporary or permanently, if suspicious attempts happen.
* Captcha: It might be a good option to prevent bulk requests in a short amount of time, but it should be complex enough to not solve easily.
* Limiting request numbers: ban requests or give delayed responses.
* Monitor suspicious activities: monitor user accounts and activates to detect intrusive behaviors. 
* Two-factor authentication: Users should approve her/his own requests through a separate communication channel. This out-of-band authentication approval method can be something you know, something you have, and something you are.
