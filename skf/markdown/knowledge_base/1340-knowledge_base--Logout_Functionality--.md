## Description:

The application should always provide a logout functionality (triggerable by a visible button in the UI) to allow users to explicitly delete their session data.
In this way, possibly leaked sessions IDs prevent attackers to perform session hijacking attempts due to their .

## Solution:

The application has to provide a way to manage all active sessions (like the ones established from different devices or browsers) so that users can either selectively or completely log out all active sessions.
