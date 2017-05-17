	    
HTML encoding
--------------

***Example***

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
		
/*
Whenever user input is displayed in the application all user input should be properly escaped 
to prevent XSS injections.
*/

/*
This escaping is used whenever you put the code straight into the html like:
<span>YOUR USERINPUT</span>
The attack bellow will now be outputted as,
&lt;script&gt;alert(1337);&lt;/script&gt;
*/

import org.owasp.esapi.ESAPI;
import org.owasp.esapi.errors.EncodingException;

String htmlbug = ESAPI.encoder().encodeForHTML("<script>alert(1337);</script>");


/*
This next encoding method is used whenever you are allowing userinput into 
html attributes.
The attack below will now be outputted as:
onload=&amp;#39;alert(1337)&amp;#39;
 */
	      
String htmlatr = ESAPI.encoder().encodeForHTMLAttribute("onload='alert(1337);'");
	      
/*
Whenever parameters are rendered via javascript your application will detect normal injections
in the first instant. in order for the application not to be vulnerable to javascrpt encoding you MUST use the encodeForJavaScript function, any other escaping function still leaves your code vulnerable
*/	      

ESAPI.encoder().encodeForJavaScript("\\x3Cscript\\x3Ealert(12);\\x3C\\x2Fscript\\x3E");
	      

/*
Whenever a user can submit an link/AHREF in your application you must solely depend upon the
"ESAPI.encoder().encodeForURL" method since an attacker could otherwise inject the href with an XSS
that looks like this "javacript:alert("XSS");" whenever a victim now clicks the link this XSS
will be executed in his browser.
*/ 

try {
	ESAPI.encoder().encodeForURL("javascript:alert(234);");
} catch (EncodingException e) {
	// TODO 
	}


/*
Security consists of different layers of protection in order to guarantuee the integrity
of your application. This means that the value displayed from the database/user should
already be sanitised before being proccessed in order to prevent XSS.

As an example, what do you do when you expect a nummeric value from your application?

you first sanitize the userinput by means of an input validation method like:
See the "input validation" class for the entire example!
*/
inputValidation validate = new inputValidation();
	      String userinput = "when this string is evil the application will block operation!";
	      if(validate.validateInput(userinput, "nummeric", "Unecpected userinput", "HIGH", 3)== false)
	      { /* Cancel operation of your application */ }
		  
/*
In this example the application cancelled the request by means of simple validation.
*/


~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
