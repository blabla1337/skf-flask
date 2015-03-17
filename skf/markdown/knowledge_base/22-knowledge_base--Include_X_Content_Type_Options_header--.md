
Include X-Content-Type-Options header
-------

**Description:**

The only defined value, nosniff, prevents Internet Explorer and Google Chrome from
MIME-sniffing a response away from the declared content-type. 
This also applies to Google Chrome, when downloading extensions. 
This reduces exposure to drive-by download attacks and sites serving user uploaded 
content that, by clever naming, 
could be treated by MSIE as executable or dynamic HTML files.


**Solution:**

These headers are also known as the: X-Content-Type-Options: nosniff; 
and provide protection against Mime content type attacks when implemented in the 
application or webserver. 

	