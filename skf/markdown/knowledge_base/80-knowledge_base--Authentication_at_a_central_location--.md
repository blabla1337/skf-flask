# Authentication at a central location
-------

## Description:

Authentication should always be performed at a central location in the application, in
order to prevent missing authentication on certain levels in the application.

## Solution:

Use a central location for authentication. If u want to put extra constraints on the
users for accessing critical parts of your application, you have to implement
step-up or adaptive authentication mechanisms.

Verify that alternative and less secure access paths do not exist.
