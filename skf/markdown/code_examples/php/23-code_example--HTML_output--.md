# HTML output
-------

## Example:


    <?php

	/*
	Whenever user input is displayed in the application, whether, as content or a parameter value
	submitted towards the url, all user input should be properly escaped to prevent XSS injections.
	*/

	//For normal output this escaping will do the trick
	$escaped = htmlspecialchars($_POST['value'], ENT_QUOTES, 'UTF-8');
	echo $escaped;

	//This also applies, for instance, when retrieving content from a database:
	while($row = $stmt->fetch(PDO::FETCH_ASSOC)) {
		echo htmlspecialchars($row['value'], ENT_QUOTES, 'UTF-8');
	}

	/*
	Security consists of different layers of protection, in order to guarantee the integrity
	of your application. This means that the value submitted from the user should
	already be sanitized before being submitted towards the database in order to prevent XSS.
	As an example, you are expecting only alphanumerical value here:
	*/

	if(!preg_match("/^[a-zA-Z0-9]+$/", $escaped)){
		die();
	}

	/*
	This type of approach should be used whenever you are allowing userinput in
	your DOM like for example, let's say a user was allowed to upload an image and
	set an alt text. when you do not sanitize his input a possible attack string could be:
	*/

	this is an image" onload="alert('XSS');"

	/*
	whenever this string now is added to the users image this will be the outcome, leading
	to xss:
	*/

	<img src="http://image.com/image.jpg" alt="this is an image" onload="alert('XSS')"" />

	/*
	After this sanitation malicious code can no longer exist in the $_POST['value'] variable.

	Another possibility for attackers to execute an XSS injection, is to pass malicious code directly
	into the URL by means of a "href", e.g.:
	javascript:alert(document.cookie);
	or
	data:text/html;base64,base64xssinjection

	In the following scenario escaping with htmlspecialchars() is not sufficient to block the injection.
	By checking the URL to see if it starts with either http:// or https:// whenever a link has
	been submitted to the web application by a user.

	?>
