##Description:

The software creates a temporary file in a directory whose permissions allow unintended actors to determine the file's existence or otherwise access that file.

On some operating systems, the fact that the temporary file exists may be apparent to any user with sufficient privileges to access that directory. Since the file is visible, the application that is using the temporary file could be known. If one has access to list the processes on the system, the attacker has gained information about what the user is doing at that time. By correlating this with the applications the user is running, an attacker could potentially discover what a user's actions are. From this, higher levels of security could be breached.

##Mitigation:


PHASE:Requirements:
Many contemporary languages have functions which properly handle this condition. Older C temp file functions are especially susceptible.

PHASE:Implementation:
Try to store sensitive tempfiles in a directory which is not world readable -- i.e., per-user directories.

PHASE:Implementation:
Avoid using vulnerable temp file functions.

