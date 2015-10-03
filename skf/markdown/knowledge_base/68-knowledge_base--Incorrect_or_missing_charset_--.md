
Incorrect or missing charset 
-------

**Description:**

When the browser has to guess the charset according of the content that is presented by 
the application, then this could could lead to XSS injections when guessing wrong.


**Solution:**

Define the charset for al your pages in order to prevent the browser for guessing 
the content types.

This could be done by adding a meta header in the head of your HTML like:

For HTML4:
<meta http-equiv="Content-Type" content="text/html;charset=ISO-8859-1">

For HTML5:
<meta charset="UTF-8"> 

Or simply by setting content-type headers by your server-side language,
C# example of a content type header:
Response.AppendHeader("Content-Type:text/html", "charset=UTF-8");

	