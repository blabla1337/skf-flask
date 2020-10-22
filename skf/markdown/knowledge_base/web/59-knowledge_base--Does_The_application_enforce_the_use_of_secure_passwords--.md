## Description:

Applications should encourage the use of strong passwords and pass-phrases. Preferably the
password policy should not put limitations or restrictions on the chosen passwords (for example
the length of a password). Whenever the application supports strong passwords and
the use of password managers, the possibility for an attacker performing a succesfull brute-force 
attack drops significantly.
This also increases the possibility that the application can be used with users' passwords managers.

## Solution:

Verify password entry fields allow, or encourage, the use of passphrases, and do not prevent
password managers, long passphrases or highly complex passwords being entered. 
A password ideally should be:
* at least 12 characters in length
* passwords even longer than 64 characters are allowed
* every special characters from Unicode charset should be permitted (including emoki, kanji, multiple whitespaces, ecc.)
* No limit for the number of characters allowed from the same type (lowercase characters, uppercase characters, digits, symbols) 
