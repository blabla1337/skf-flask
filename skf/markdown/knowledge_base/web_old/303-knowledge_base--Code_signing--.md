## Description:
Code signing is the process of digitally signing executables and scripts to confirm the software 
author and guarantee that the code has not been altered or corrupted since it was signed. 
The process employs the use of a cryptographic hash to validate authenticity and integrity.

Code signing can provide several valuable features. The most common use of code signing is to 
provide security when deploying; in some programming languages, it can also be used to help prevent 
namespace conflicts. Almost every code signing implementation will provide some sort of digital 
signature mechanism to verify the identity of the author or build system, and a checksum to verify 
that the object has not been modified. It can also be used to provide versioning information about an object or to store other meta data about an objec

## Solution:
Sign your code and validate the signatures(checksums) of your code and third party
components to confirm the integrity of the deployed components.
