# Centralized the mechanisms for protecting resources and the access
-------

## Description:

Applications have often different ways for granting access to protected resources, sometimes these are 
done based on a role that is defined in a Database or using an Active Directory permission. Also, external
authorization services may be implemented and needed for the application. With all these different ways 
for protecting resources and the access to these assets mistakes will be easily made. 

## Solution:

Immplement a centralized mechanism where all the different types of resources and grating access to 
these resources (including libraries that call external authorization services) are located. This way
it's easier to maintain and the lower the complexity.
