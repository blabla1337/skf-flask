# Timeout Sessions 
-------

## Example:


/*
Within your web.xml you can configure your session idle timeout.
The default time is set to 20 minutes.
*/

<webapp>
...
  <session-config>
    <session-timeout>20</session-timeout> <!-- in minutes -->
  </session-config>
</webapp>

