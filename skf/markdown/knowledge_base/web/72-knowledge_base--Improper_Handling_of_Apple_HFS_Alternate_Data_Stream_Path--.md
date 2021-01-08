##Description:

The software does not properly handle special paths that may identify the data or resource fork of a file on the HFS+ file system.

If the software chooses actions to take based on the file name, then if an attacker provides the data or resource fork, the software may take unexpected actions. Further, if the software intends to restrict access to a file, then an attacker might still be able to bypass intended access restrictions by requesting the data or resource fork for that file.

##Mitigation:
