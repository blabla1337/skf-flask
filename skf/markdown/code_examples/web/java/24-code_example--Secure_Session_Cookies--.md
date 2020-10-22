# Secure Session Cookies 
-------

## Example:


    //Secure Flag

    //Benefit: Instructs the browser to never send the cookie over a HTTP request. The cookie can only be sent over HTTPS. This works //even if the user manually types in a request for HTTP. The HTTP request will be sent, but the browser will not send any cookies //marked as “SECURE”

    //Limitations: The HTTP Request is still sent and this could be manipulated by a man in the middle to perform convincing phishing //attacks (See Strict Transport Security for solution).

    //Example within HTTP Response:
    //Cookie: JSESSIONID=kljahsdf123; SECURE;

    //web.xml

    //Servlet 3.0 (Java EE 6) introduced a standard way to configure secure attribute for the session cookie, this can be done by //applying the following configuration in web.xml

    <session-config>
    <cookie-config>
    <secure>true</secure>
    </cookie-config>
    </session-config>

    //Tomcat

    //In Tomcat 6 if the first request for session is using https then it automatically sets secure attribute on session cookie. 

    //or programmatically 

    String sessionid = request.getSession().getId();
    response.setHeader("SET-COOKIE", "JSESSIONID=" + sessionid + "; secure");
    