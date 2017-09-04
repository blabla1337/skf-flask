# Charsets 
-------

## Example:


	/*
	In order to set the "Charsets" header you'll have to add the 
	following code to the head of your application, the following code could be used in your controller 
	for by example, text/html:
	*/

	response.addHeader("Content-Type: text/html", "charset=utf-8");

	/*
	Or directly into your html markup:
	*/

	<meta http-equiv="Content-Type" content="text/html; charset=utf-8">
		