##Description:

There are some security headers which should be properly configured in order to protect some API callbacks against Reflective File Download and other type of injections.

Also check if the API response is dynamic, if user input is reflected in the response. If so, you must validate and encode the input, in order to prevent XSS and Same origin method execution attacks.

##Mitigation:

Sanitize your API's input (in this case they should just allow alphanumeric); escaping is not sufficient

Verify that all API responses contain X-Content-Type-Options: nosniff, to prevent the browser from interpreting files as something else than declared by the content type (this helps prevent XSS if the page is interpreted as html or js).

Add 'Content-Disposition: attachment; filename="filename.extension"' with extension corresponding the file extension and content-type, on APIs that are not going to be rendered

