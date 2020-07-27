##Description:

Whenever you are supplying your JavaScript/jquery with data which is controlled by the
user, you should make sure this data is not supplied towards functions which could
interpreted the supplied and parse input as code. This could lead to XSS and other code
injections.

## Solution:

Below we listed some safe functions for whenever it is needed to supply your
JavaScript/jquery functions with user-input.

JQUERY functions:
.txt();
.val();
.parse();

Example:
      ````
	<script>
	function myFunction() {
		$( "p" ).text( "append user-input to paragrapgh safely" );
	}
	</script>


	Javscript functions:
	.innerText();   <- not supported by firefox
	.textContext(); <- not supported on I.E 8 and lower
	.createTextNode();
	.value();
	```
	
Example:
	```
	<script>
	function myFunction() {
   		var t = document.createTextNode("append user-input to body safely");
    	document.body.appendChild(t);
	}
	</script>
	```
