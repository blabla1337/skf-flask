## Description:

Sending passwords or activation key's in clear text exposes sensitive information. 

## Solution:

It is best practice to send a unique url or an URL with a unique parameter that allows the user to be re(activated).
Make sure the URL expires in a reasonable time and the URL/parameter becomes invalid once the user has been reactivated.
