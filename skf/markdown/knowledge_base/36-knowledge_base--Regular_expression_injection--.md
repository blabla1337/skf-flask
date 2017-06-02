# Regular expression injection
-------

## Description:

If the application uses regular expressions which receive user input,
then the user input should be properly escaped.
If not done properly, then the hacker can affect the regular expression and modify their
logic. In some cases, an attacker could even gain access to the server.


## Solution:

Do not use user-input without escaping in a regular expression "regex pattern",
Since this could lead to serious security vulnerabilities.
