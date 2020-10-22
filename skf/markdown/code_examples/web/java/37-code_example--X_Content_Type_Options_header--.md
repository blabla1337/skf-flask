# X-Content-Type-Options header
-------

## Example:


    /*
    In order to set the "X-Content-Type-Options" header you'll have to add the 
    following code to the head of your application, the following code could be used in your controller:
    */

    response.appendHeader("X-Content-Type-Options", "nosniff");
