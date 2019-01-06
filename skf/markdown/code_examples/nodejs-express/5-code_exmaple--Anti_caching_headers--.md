# Anti-cashing headers 
-------

## Example:

    /*
    Add the following headers to your application head in order to prevent the browser from caching
    the following code could be used in your controller:
    */

    resp.set("Cache-Control", "no-cache, no-store, must-revalidate"); // HTTP 1.1.
    res.set("Pragma", "no-cache"); // HTTP 1.0.
    res.set("Expires", "0"); // Proxies.
    
