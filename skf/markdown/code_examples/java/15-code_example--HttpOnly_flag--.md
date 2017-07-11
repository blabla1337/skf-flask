# HttpOnly flag
-------

## Example:


//If you're using Servlets 3.0, you can actually instruct the app server to ensure that all session cookies are HttpOnly and Secure //with the following fragments:

<session-config>
  <cookie-config>
    <secure>true</secure>
    <http-only>true</http-only>
  </cookie-config>
</session-config>


//httpOnly is supported as of Tomcat 6.0.19 and Tomcat 5.5.28.

//See the changelog entry for bug 44382.

//The last comment for bug 44382 states, "this has been applied to 5.5.x and will be included in 5.5.28 onwards." However, it does //not appear that 5.5.28 has been released.

//The httpOnly functionality can be enabled for all webapps in conf/context.xml:

<Context useHttpOnly="true">
...
</Context>

//  My interpretation is that it also works for an individual context by setting it on the desired Context entry in conf/server.xml // (in the same manner as above).

