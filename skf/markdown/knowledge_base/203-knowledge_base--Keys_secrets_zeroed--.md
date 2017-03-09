# Zero keys and secrets before destroying them
-------

## Description:

Attackers are always on the lookout for secrets of a server of computer. When these secrets are
accessible for an attacker because the key was not properly being destroyed then this can lead to
security issues.

## Solution:

Before destroying a secret or a security key it's needed by the application to overwrite the secret
with a new value zeroes. This will make it harder for an attacker to obtain the correct old value
of the secret or security key.
