# X-Content-Type-Options header
-------

## Example:


    /*
    In order to set the "X-Content-Type-Options" header you'll have to add the 
    following code to the head of your application, the following code could be used in your controller:
    */

    res.set("X-Content-Type-Options", "nosniff");

    /*
         alternatively use dont-sniff-mimetype
     */
    const nosniff = require('dont-sniff-mimetype')
    app.use(nosniff())


    /* ALternatively you can use helmet https://www.npmjs.com/package/helmet which sets X-FRAME headers along with a host of other security headers */
