## Description:

I/O commands allow you to own, use, read from, write to, and close devices. To direct I/O operations to a device.
Whenever user supplied input i.e file names and/or file data is being directly used in these commands this could lead 
to path traversal, local file include, file mime type, and OS command injection vulnerabilities.

## Solution:

File names and file contents should be sanitized before being used in I/O commands. 
