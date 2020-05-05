## Description:

The product does not require that users should have strong passwords, which makes it easier for attackers to compromise user accounts.

Authentication mechanisms often rely on a memorized secret (also known as a password) to provide an assertion of identity for a user of a system. It is therefore important that this password be of sufficient complexity and impractical for an adversary to guess. The specific requirements around how complex a password needs to be depends on the type of system being protected. Selecting the correct password requirements and enforcing them through implementation are critical to the overall success of the authentication mechanism.

## Mitigation:


PHASE:Architecture and Design:
A product's design should require adherance to an appropriate password policy. Specific password requirements depend strongly on contextual factors, but it is recommended to contain the following attributes: Enforcement of a minimum and maximum length Restrictions against password reuse Restrictions against using common passwords Restrictions against using contextual string in the password (e.g., user id, app name) Depending on the threat model, the password policy may include several additional attributes. Complex passwords requiring mixed character sets (alpha, numeric, special, mixed case) Increasing the range of characters makes the password harder to crack and may be appropriate for systems relying on single factor authentication. Unfortunately, a complex password may be difficult to memorize, encouraging a user to select a short password or to incorrectly manage the password (write it down). Another disadvantage of this approach is that it often does not result in a significant increases in overal password complexity due to people's predictable usage of various symbols. Large Minimum Length (encouraging passphrases instead of passwords) Increasing the number of characters makes the password harder to crack and may be appropriate for systems relying on single factor authentication. A disadvantage of this approach is that selecting a good passphrase is not easy and poor passwords can still be generated. Some prompting may be needed to encourage long un-predictable passwords. Randomly Chosen Secrets Generating a password for the user can help make sure that length and complexity requirements are met, and can result in secure passwords being used. A disadvantage of this approach is that the resulting password or passpharse may be too difficult to memorize, encouraging them to be written down. Password Expiration Requiring a periodic password change can reduce the time window that an adversary has to crack a password, while also limiting the damage caused by password exposures at other locations. Password expiration may be a good mitigating technique when long complex passwords are not desired. See NIST 800-63B https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-63b.pdf Sections: 5.1.1, 10.2.1, and Appendix A for further information on password requirements.

PHASE:Architecture and Design:
Consider a second authentication factor beyond the password, which prevents the password from being a single point of failure. See CWE-308 for further information.

PHASE:Implementation:
Consider implementing a password complexity meter to inform users when a chosen password meets the required attributes.

