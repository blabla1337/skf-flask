
HTML output
-------

**Example:**



		/*
		Whenever user input is displayed in the application, whether this is as content or as a parameter
		value submitted towards the url, all user input should be properly escaped to prevent XSS injections.

		Imagine this POST value being shown as content somewhere
		on the application. In it's current state it is vulnerable for XSS injection. 

		In its escaped state we used the php function "htmlspecialchars()" in order to disarm
		malicious user input triggering the XSS injection.

		<form method='POST'>
		<input type='text' name='value'/><br/>
		<input type='submit' name='submit' value='submit'/>
		</form>
		*/
 
		//POST value current state:
		$vulnerable = $_POST['value'];
		echo $vulnarable

		//POST value escaped state:
		$escaped = htmlspecialchars($_POST['value']);
		echo $escaped;

		//This also apply's for instance, when retrieving content from a database.

		while($row = $stmt->fetch(PDO::FETCH_ASSOC)) {

		echo htmlspecialchars($row['value']);

		}//end while loop

		/*
		security consists out of different layers of protection in order to warrant the 
		integrity of your application. which means the value subtracted from the database should
		already be sanitised before submitted towards the database in order to prevent XSS.
		for instance, you only expected a numerical value:
		*/

		if(!preg_match('/^[0-9]/', $escaped))
		{
		die;
		}

		/*
		After this sanitation malicious code can no longer exist in the $_POST['value'] variable.

		Another possibility for hackers to execute an XSS injection is to pass malicious code directly into the url by means of a href like:
		javascript:alert(document.cookie);
		or
		data:text/html;base64,base64xssinjection
		In this scenario the escaping with htmlspecialchars() is not sufficient enough in order to block the injection.
		By checking the URL to see if it starts with either http:// or https:// you can prevent this attack by exiting the application 
		when this anomaly is triggered. */ 

		if(substr_compare($_SERVER['REQUEST_URI'], "http://", 0, 7, true ) != 0
		&&
		substr_compare($_SERVER['REQUEST_URI'], "https://", 0, 8, true)    !=0 )  
		{
		die;
		}



	