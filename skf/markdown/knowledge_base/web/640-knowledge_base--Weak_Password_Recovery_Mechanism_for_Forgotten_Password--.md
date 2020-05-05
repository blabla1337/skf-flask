## Description:

The software contains a mechanism for users to recover or change their passwords without knowing the original password, but the mechanism is weak.

It is common for an application to have a mechanism that provides a means for a user to gain access to their account in the event they forget their password. Very often the password recovery mechanism is weak, which has the effect of making it more likely that it would be possible for a person other than the legitimate system user to gain access to that user's account. Weak password recovery schemes completely undermine a strong password authentication scheme. This weakness may be that the security question is too easy to guess or find an answer to (e.g. because the question is too common, or the answers can be found using social media). Or there might be an implementation weakness in the password recovery mechanism code that may for instance trick the system into e-mailing the new password to an e-mail account other than that of the user. There might be no throttling done on the rate of password resets so that a legitimate user can be denied service by an attacker if an attacker tries to recover their password in a rapid succession. The system may send the original password to the user rather than generating a new temporary password. In summary, password recovery functionality, if not carefully designed and implemented can often become the system's weakest link that can be misused in a way that would allow an attacker to gain unauthorized access to the system.

## Mitigation:


PHASE:Architecture and Design:
Make sure that all input supplied by the user to the password recovery mechanism is thoroughly filtered and validated.

PHASE:Architecture and Design:
Do not use standard weak security questions and use several security questions.

PHASE:Architecture and Design:
Make sure that there is throttling on the number of incorrect answers to a security question. Disable the password recovery functionality after a certain (small) number of incorrect guesses.

PHASE:Architecture and Design:
Require that the user properly answers the security question prior to resetting their password and sending the new password to the e-mail address of record.

PHASE:Architecture and Design:
Never allow the user to control what e-mail address the new password will be sent to in the password recovery mechanism.

PHASE:Architecture and Design:
Assign a new temporary password rather than revealing the original password.

