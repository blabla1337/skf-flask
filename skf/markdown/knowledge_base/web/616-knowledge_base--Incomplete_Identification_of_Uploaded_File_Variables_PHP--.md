## Description:

The PHP application uses an old method for processing uploaded files by referencing the four global variables that are set for each file (e.g. $varname, $varname_size, $varname_name, $varname_type). These variables could be overwritten by attackers, causing the application to process unauthorized files.

These global variables could be overwritten by POST requests, cookies, or other methods of populating or overwriting these variables. This could be used to read or process arbitrary files by providing values such as /etc/passwd.

## Mitigation:


PHASE:Architecture and Design:
Use PHP 4 or later.

PHASE:Architecture and Design:
If you must support older PHP versions, write your own version of is_uploaded_file() and run it against $HTTP_POST_FILES['userfile']))

PHASE:Implementation:
For later PHP versions, reference uploaded files using the $HTTP_POST_FILES or $_FILES variables, and use is_uploaded_file() or move_uploaded_file() to ensure that you are dealing with an uploaded file.

