## Description:

Only authorized administrators should have access to change security-relevant configurations.

These administrators should also regularly check these configurations to be adequate and that
they are not unchanged by malicious intent. This could keep systems vulnerable to attacks due
to the disabling of important security systems.


## Solution:

Verify that authorised administrators have the capability to verify the
integrity of all security-relevant configurations to ensure that they have not been tampered with.

One way to achieve this would be to apply (HIDS) rules. 
This is a system that monitors important operating system files and can verify whether these files
have been edited. Whenever these files are edited a four eyes principle must be applied that checks
the integrity of these changes.
