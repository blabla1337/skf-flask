# Open Forwards and Redirects 
-------

## Example:


    /*
    When using forwards & redirects you should make sure the URL is being explicitly 
    declared in the code and cannot be manipulated by an attacker like:
    */

    //res.redirect("/login")

    /*
    Generally you should avoid getting input into the redirect which could contain
    user-input by any means. if for any reason this may not be feasible than you 
    should make a WhiteList input validation for the redirect like so:
    */
    app.get("/offers", function(req, res, next) {
        var redirectTo = req.query.redirect;
        if(validRedirectURLs.includes(redirectTo)) {
            return res.redirect(redirectTo);
        } else {
            return res.status(500).send({ error: 'Invalid URL' });
        }
    });