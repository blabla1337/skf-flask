# Possible attackers of the application must be documented
-------

## Description:

Authentication decisions should be logged along with relevant metadata for security 
investigations. This information could for example, be used whenever there is suspicion about
accounts being compromised. Also, passwords and other sensitive information should never be stored
in these log files. Whenever an attacker gains knowledge of these files, this information
could be used to compromise other accounts. 

Note: "Usernames should also never be stored in the log files, users are not always paying
attention to their actions and sometimes provide the username form field with their password.
If the application would log the usernames, these passwords are now also stored and can be
used to compromise accounts whenever an attacker gains knowledge of these files.

## Solution:

Verify that all authentication decisions can be logged, without storing sensitive session 
identifiers or passwords. This should include requests with relevant metadata
needed for security investigations.
