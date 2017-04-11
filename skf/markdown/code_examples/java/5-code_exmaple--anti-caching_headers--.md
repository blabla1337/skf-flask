# Anti-cashing headers 
-------

## Example:


    /*
    Add the following headers to your application head in order to prevent the browser from caching
    the following code could be used in your controller:
    */

    response.appendHeader("Cache-Control", "no-cache, no-store, must-revalidate"); // HTTP 1.1.
    response.appendHeader("Pragma", "no-cache"); // HTTP 1.0.
    response.appendHeader("Expires", "0"); // Proxies.

