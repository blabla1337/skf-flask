
Anti clickjacking headers
-------

## Example:


One way to defend against clickjacking is to include a "frame-breaker" script in each
page that should not be framed. The following methodology will prevent a webpage from
being framed even in legacy browsers, that do not support the X-Frame-Options-Header.
In the document HEAD element, add the following:
First apply an ID to the style element itself:
	
    <style id="antiClickjack">body{display:none !important;}</style>
    //And then delete that style by its ID immediately after in the script:

    <script type="text/javascript">
	   if (self === top) {
		   var antiClickjack = document.getElementById("antiClickjack");
		   antiClickjack.parentNode.removeChild(antiClickjack);
	   } else {
		   top.location = self.location;
	   }
    </script>

  """
  To set the same X-Frame-Options value for all responses in your site, put 'django.middleware.clickjacking.XFrameOptionsMiddleware' to MIDDLEWARE:

    MIDDLEWARE = [
      ...
      'django.middleware.clickjacking.XFrameOptionsMiddleware',
      ...
    ]

  Middleware will be enabled by default while starting the project.

  By default the X-Frame-Options header is set to SAMEORIGIN  

  """

  # If we want to set the X_FRAME_OPTIONS to DENY
  # If you want DENY instead, set the X_FRAME_OPTIONS setting

  X_FRAME_OPTIONS = 'DENY'
