# Context sensitive authorization
-------

## Description:

Whenever granting users different types of authorization throughout the application
the authorization grants should be granted and enforced outside of the attackers scope.

i.e whenever a user gets his authorization grants through a cookie that says,

````
    auth=admin or auth=user
````

These authorization grants are easily manipulable.


## Solution:

Authorization grants must be granted and enforced outside of the attackers scope. 

i.e: 
The user logs into the application, the user id is than stored in a local variable.
The application stores grants(privileges/attributes/claims) in the database and for each
function the user calls the application gets the grants from the DB using the local variable
and checks if the user has access to this function.
