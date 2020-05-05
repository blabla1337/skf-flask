## Description:

The product uses external input to determine the names of variables into which information is extracted, without verifying that the names of the specified variables are valid. This could cause the program to overwrite unintended variables.

For example, in PHP, extraction can be used to provide functionality similar to register_globals, a dangerous functionality that is frequently disabled in production systems. Calling extract() or import_request_variables() without the proper arguments could allow arbitrary global variables to be overwritten, including superglobals. Similar functionality is possible in other interpreted languages, including custom languages.

## Mitigation:


PHASE:Implementation:STRATEGY:Input Validation:
Use whitelists of variable names that can be extracted.

PHASE:Implementation:
Consider refactoring your code to avoid extraction routines altogether.

PHASE:Implementation:
In PHP, call extract() with options such as EXTR_SKIP and EXTR_PREFIX_ALL; call import_request_variables() with a prefix argument. Note that these capabilities are not present in all PHP versions.

