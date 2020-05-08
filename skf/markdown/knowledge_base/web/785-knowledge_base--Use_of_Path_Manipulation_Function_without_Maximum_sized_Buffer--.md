## Description:

The software invokes a function for normalizing paths or file names, but it provides an output buffer that is smaller than the maximum possible size, such as PATH_MAX.

Passing an inadequately-sized output buffer to a path manipulation function can result in a buffer overflow. Such functions include realpath(), readlink(), PathAppend(), and others.

## Mitigation:


PHASE:Implementation:
Always specify output buffers large enough to handle the maximum-size possible result from path manipulation functions.

