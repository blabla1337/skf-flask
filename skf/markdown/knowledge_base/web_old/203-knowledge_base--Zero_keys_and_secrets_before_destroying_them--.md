##Description:

Attackers are always on the lookout for secrets of a server or computer. When these secrets are
accessible for an attacker because the key was not properly being destroyed then this can lead to
security vulnerabilities. All secrets and keys should be completely erased from the memory since 
an attacker could otherwise potentially retrieve these keys with memory dumping attacks on the application.

## Solution:

Secrets and keys should be erased from the memory and zeroed when they are no longer needed to prevent attackers from 
doing memory dumping attacks.

Also take into consideration the different Garbage collectors of your programming language. Whenever you zero out the keys of secret in question, you have no guarantee that a copy of it doesn't exist elsewhere in memory.
