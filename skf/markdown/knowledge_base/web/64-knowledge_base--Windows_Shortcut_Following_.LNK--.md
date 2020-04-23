## Description:

The software, when opening a file or directory, does not sufficiently handle when the file is a Windows shortcut (.LNK) whose target is outside of the intended control sphere. This could allow an attacker to cause the software to operate on unauthorized files.

The shortcut (file with the .lnk extension) can permit an attacker to read/write a file that they originally did not have permissions to access.

## Mitigation:


PHASE:Architecture and Design:STRATEGY:Separation of Privilege:
Follow the principle of least privilege when assigning access rights to entities in a software system. Denying access to a file can prevent an attacker from replacing that file with a link to a sensitive file. Ensure good compartmentalization in the system to provide protected areas that can be trusted.

