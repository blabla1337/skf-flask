# Does the application enforce the use of secure passwords
-------

## Description:

Applications should encourage the use of strong passwords and pass-phrases. Preferably the
password policy should not put limitations or restrictions on the chosen passwords.
Whenever the application supports strong passwords and the use of password managers, the
possibility for an attacker performing a succesfull brute-force attack drops significally.

## Solution:

Verify password entry fields allow, or encourage, the use of passphrases, and do not prevent
password managers, long passphrases or highly complex passwords being entered. Also known top 1000 passwords
should also be forbidden and rejected.

note:
Never put restrictions on the password the user submits. Some applications for
instance do not allow passwords longer than twenty chars. This is an example of bad
practice since the password must be allowed as strong as the users wants it to be.
