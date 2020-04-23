## Description:

Opening temporary files without appropriate measures or controls can leave the file, its contents and any function that it impacts vulnerable to attack.



## Mitigation:


PHASE:Requirements:
Many contemporary languages have functions which properly handle this condition. Older C temp file functions are especially susceptible.

PHASE:Implementation:
Ensure that you use proper file permissions. This can be achieved by using a safe temp file function. Temporary files should be writable and readable only by the process that owns the file.

PHASE:Implementation:
Randomize temporary file names. This can also be achieved by using a safe temp-file function. This will ensure that temporary files will not be created in predictable places.

