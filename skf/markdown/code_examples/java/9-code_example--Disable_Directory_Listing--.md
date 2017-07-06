# Diseable Directory Listing 
-------

## Example:


// Directory Listing configuraton in web.xml 

<servlet>
    <servlet-name>default</servlet-name>
    <servlet-class>
      org.apache.catalina.servlets.DefaultServlet
    </servlet-class>
    <init-param>
        <param-name>debug</param-name>
        <param-value>0</param-value>
    </init-param>
    <init-param>
        <param-name>listings</param-name>
        <param-value>false</param-value>    <!-- This setting enables/disables directory listings -->
    </init-param>
    <load-on-startup>1</load-on-startup>
</servlet>

