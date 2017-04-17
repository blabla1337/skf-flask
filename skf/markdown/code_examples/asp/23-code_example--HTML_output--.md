HTML output
-------

**Example:**


	/*
	Whenever user input is displayed in the application all user input should be properly escaped 
	to prevent XSS injections.

	The C# razor engine encodes userinput by default whenever this is not disabled in the web.config
	when outputted on screen, BUT you should get used to putting your variables in encoding functions
	and make this a habbit simply "assuming" your input will be encoded properly is a jack in the box waiting to
	pop out and bite you in the ....as you will find out when you read on
	*/

	/*
	This escaping is used whenever you put the code straight into the html like:
	<span>YOUR USERINPUT</span>
	The attack bellow will now be outputted as,
	&lt;script&gt;alert(1337);&lt;/script&gt;
	*/
	ViewBag.html = HttpUtility.HtmlEncode("<script>alert(1337);</script>");

	/*
	This next encoding method is used for whenever you are allowing userinput into 
	html attributes.
	The attack below will now be outputted as:
	onload=&amp;#39;alert(1337)&amp;#39;
	 */
	ViewBag.htmlatr = HttpUtility.HtmlAttributeEncode("onload='alert(1337);'");

	/*
	Whenever parameters are rendered via javascript your application will detect normal injections
	in the first instant. But your application still remains vulnerable to javascript encoding which will not
	be detected by the ASP.NET encoder. You MUST use the JavaScriptStringEncode function, any other 
	escaping function still leaves your code vulnerable
	*/
	ViewBag.java = HttpUtility.JavaScriptStringEncode(@"""\x3Cscript\x3Ealert(12);\x3C\x2Fscript\x3E""");
   
	/*
	Whenever a user can submit an link/AHREF in your application you must solely depend upon the
	"HttpUtility.UrlEncode" method since an attacker could otherwise inject the href with an XSS
	that looks like this "javacript:alert("XSS");" whenever a victim now clicks the link this XSS
	will be executed in his browser.
	*/ 
	ViewBag.url = HttpUtility.UrlEncode("javascript:alert(234);");

	/*
	Security consists of different layers of protection in order to guarantuee the integrity
	of your application. This means that the value displayed from the database/user should
	already be sanitised before being proccessed in order to prevent XSS.
	
	As an example, what do you do when you expect a nummeric value from your application?
	
	EXACTLY you first sanitize the userinput by means of an input validation method like:
	See the "input validation" class for the entire example!
	*/

	inputvalidation validate = new inputvalidation();
	string userinput = "when this string is evil the application will block operation!";
	if(validate.validateInput(userinput, "nummeric", "Unecpected userinput", "HIGH", 3)== false)
	{ /* Cancel operation of your application */ }
	

	/*
	In this example the application cancelled the request by means of simple validation.
	*/