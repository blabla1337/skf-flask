## Description:

When the browser has to guess the charset according to the content that is presented by
the application, then this could lead to XSS injections when the guess is wrong.

## Solution:

Define the charset for all your pages in order to prevent the browser for guessing
the content types.

This could be done by adding a meta header in the head of your HTML like:

For HTML4:
```html
<meta http-equiv="Content-Type" content="text/html;charset=ISO-8859-1">
```
For HTML5:
```html
<meta charset="UTF-8">
```
Or simply by setting content-type headers by your server-side language,
C# example of a content type header:
Response.AppendHeader("Content-Type:text/html", "charset=UTF-8");
