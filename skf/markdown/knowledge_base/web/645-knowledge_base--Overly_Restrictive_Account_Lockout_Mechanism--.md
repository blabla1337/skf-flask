## Description:

The software contains an account lockout protection mechanism, but the mechanism is too restrictive and can be triggered too easily, which allows attackers to deny service to legitimate users by causing their accounts to be locked out.

Account lockout is a security feature often present in applications as a countermeasure to the brute force attack on the password based authentication mechanism of the system. After a certain number of failed login attempts, the users' account may be disabled for a certain period of time or until it is unlocked by an administrator. Other security events may also possibly trigger account lockout. However, an attacker may use this very security feature to deny service to legitimate system users. It is therefore important to ensure that the account lockout security mechanism is not overly restrictive.

## Mitigation:


PHASE:Architecture and Design:
Implement more intelligent password throttling mechanisms such as those which take IP address into account, in addition to the login name.

PHASE:Architecture and Design:
Implement a lockout timeout that grows as the number of incorrect login attempts goes up, eventually resulting in a complete lockout.

PHASE:Architecture and Design:
Consider alternatives to account lockout that would still be effective against password brute force attacks, such as presenting the user machine with a puzzle to solve (makes it do some computation).

