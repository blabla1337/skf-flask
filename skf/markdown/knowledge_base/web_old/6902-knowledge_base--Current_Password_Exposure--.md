##Description:

The recovery of cedentials should never reveal or send the current password to the user.

## Solution:

It is best practice to send a unique url or an URL with a unique parameter that allows the user to create new credentials.
Make sure the URL expires in a reasonable time and the URL/parameter becomes invalid once the user has been reactivated.
In addition please note that passwords should not be stored in clear text in the database of an application. Instead it is best practice to store password hashes en verify the hashes when authenticating the user.
