# Anti clickjacking headers
-------

## Example:

    
    """
    One way to defend against clickjacking is to include a 'frame-breaker' script in each
    page that should not be framed. The following methodology will prevent a webpage from
    being framed even in legacy browsers, that do not support the X-Frame-Options-Header.
    In the document HEAD element, add the following:
    First apply an ID to the style element itself:
    """

    <style id="antiClickjack">body{display:none !important;}</style>
    <!-- And then delete that style by its ID immediately after in the script -->
    <script type="text/javascript">
      if (self === top) {
        var antiClickjack = document.getElementById("antiClickjack");
        antiClickjack.parentNode.removeChild(antiClickjack);
      } else {
        top.location = self.location;
      }
    </script>

    @app.after_request
    def clickjacking_Protection(response):
        """
        The second option is to use 'security headers'.
        There are two options for setting the 'anti-clickjacking' headers in
        your application:
        """

        //This will completely prevent your page from being displayed in an iframe 
        response.headers["X-Frame-Options"] = "DENY"

        //This will completely prevent your page from being displayed in an iframe on other sites 
        response.headers["X-Frame-Options"] = "SAMEORIGIN"
        return response
