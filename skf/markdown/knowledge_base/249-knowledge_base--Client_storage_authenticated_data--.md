# authenticated data cleared from client storage
-------

## Description:

All authenticated data should be removed from the browsers storage as soon as
the session is terminated. This reduces the possibility that a potential attacker gains
sensitive authenticated information whenever the application is attacked.

This aproach also is necessary to disable unauthenticated users to access the information
if the user was initially logged in on a public computer.

## Solution:

Whenever the user terminates his session al sensitive authenticated information should be 
cleared from the browser in the client storage. such as:

* local storage
* Session storage
* web SQL
* Cache storage
* Application cache
* etc
