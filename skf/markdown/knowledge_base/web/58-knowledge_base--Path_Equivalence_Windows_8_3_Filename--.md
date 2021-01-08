##Description:

The software contains a protection mechanism that restricts access to a long filename on a Windows operating system, but the software does not properly restrict access to the equivalent short 8.3 filename.

On later Windows operating systems, a file can have a long name and a short name that is compatible with older Windows file systems, with up to 8 characters in the filename and 3 characters for the extension. These 8.3 filenames, therefore, act as an alternate name for files with long names, so they are useful pathname equivalence manipulations.

##Mitigation:


PHASE:System Configuration:
Disable Windows from supporting 8.3 filenames by editing the Windows registry. Preventing 8.3 filenames will not remove previously generated 8.3 filenames.

