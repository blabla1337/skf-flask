##Description:

The application should always generate a new session ID only after the user submits a set of valid credentials upon authentication.
This is meant to prevent an attacker from performing Session Fixation attacks against other users.

## Solution:

Verify that session tokens are generated after a successfull authentication, not before. Please note also that these IDs should be unique and randomly generated.
