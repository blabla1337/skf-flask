# Secure Session Cookies 
-------

## Example:


    //Secure Flag

    //Benefit: Instructs the browser to never send the cookie over a HTTP request. The cookie can only be sent over HTTPS. This works //even if the user manually types in a request for HTTP. The HTTP request will be sent, but the browser will not send any cookies //marked as “SECURE”

    //Limitations: The HTTP Request is still sent and this could be manipulated by a man in the middle to perform convincing phishing //attacks (See Strict Transport Security for solution).

    /*
    Setting the "Domain" attribute to a too permissive value, such as "example.com" 
    allows an attacker to launch attacks on the session IDs between different hosts and 
    web applications belonging to the same domain, known as cross-subdomain cookies.
    For example, vulnerabilities in www.example.com might allow an attacker to get access 
    to the session IDs from secure.example.com.
    */



    var session = require('cookie-session')
    var express = require('express')
    var app = express()

    var expiryDate = new Date(Date.now() + 60 * 60 * 1000) // 1 hour
    app.use(session({
    name: 'session',
    keys: ['key1', 'key2'],
    cookie: {
        secure: true,
        httpOnly: true,
        domain: 'complete.subdomain.example.com',
        path: 'foo/bar',
        expires: expiryDate
    }
    }))
