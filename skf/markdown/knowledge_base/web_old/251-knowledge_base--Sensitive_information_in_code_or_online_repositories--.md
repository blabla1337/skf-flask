##Description:

Whenever secrets, API keys, and passwords are stored in the applications source code an attacker
can potentially retrieve this sensitive information by i.e:

1. Finding old zip files with earlier releases
2. Retrieve and read files by path traversal attacks

Also be cautious not to store this sensitive information on online repositories.
Whenever this repository gets made public by accident or compromised all this sensitive information
can fall into the hands of attackers.

##Mitigation:

Verify that secrets, API keys, and passwords are not included in the source code, or online source code 
repositories.This could be achieved by manual code reviews and potentially small tools that checks the code
for these keys and secrets by means of pattern matching.
