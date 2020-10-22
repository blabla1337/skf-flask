# Session Cookies 
-------

## Example:


    /*
    Setting the "Domain" attribute to a too permissive value, such as "example.com" 
    allows an attacker to launch attacks on the session IDs between different hosts and 
    web applications belonging to the same domain, known as cross-subdomain cookies.
    For example, vulnerabilities in www.example.com might allow an attacker to get access 
    to the session IDs from secure.example.com.
    */

    //This is apparently supported via a configuration setting in 6.0.27 and onwards:

    Configuration is done by editing META-INF/context.xml

    <Context sessionCookiePath="/something" sessionCookieDomain=".domain.tld" />
