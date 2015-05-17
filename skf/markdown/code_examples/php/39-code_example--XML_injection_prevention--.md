
XML injection prevention
-------

**Example:**
	
	<?php

	/*
	Whenever you are using XML parsers you must sanitise or encode al user-input before 
	including this input into your XML file.

	Some methods like below, the Domdocument already encodes the input before storing it
	into the XML. But beware, since this encoded input is stil a threat whenever you are
	displaying the this data on screen as HTML output. This encoded data should be escaped
	at all times before displaying.
	
	Whenever your XML function does not encode your data on the fly, you may want to write
	your own function for achieving this. See the code examples and search for "Input encoding"
	for more detailed information.
	*/
	
	
	//Let us take an easy example where we store your faforite number name into a XML file.
	$doc = new DOMDocument();
	$doc->formatOutput = true;

	$r = $doc->createElement( "employees" );
	$doc->appendChild( $r );

	$b = $doc->createElement( "employee" );

	$name = $doc->createElement( "name" );
	$name->appendChild(
	$doc->createTextNode( $_POST['name'] )
	);
	$b->appendChild( $name );

	$r->appendChild( $b );

	$doc->save("test.xml");
	
	/*
	We will try to insert <script>alert(123);</script> into the XML file,
	Now after inserting the employee name into the XML file it wil look like:
	

		<?xml version="1.0"?>
	<employees>
	  <employee>
		<name>&lt;script&gt;alert(123);&lt;/script&gt;</name>
	  </employee>
	</employees>
	
	As you can see de input has been encoded but still can trigger an XSS whenever we
	extract the data as shown in the example below:
	
	NOTE: if you ever want to inlcude the xml files by means of user-selected sources,
	be aware of the fact that an attacker could also include sources from external websites
	and even execute External entity injections on your applications. See the "XSLT injection prevention"
	code example for more detailed information on how to implement this type of functionality since
	the same principle's apply to both functions.
	*/

		
	$doc = new DOMDocument();
	$doc->load( 'test.xml' );
	$doc -> validateOnParse = true;
	$employees = $doc->getElementsByTagName( "employee" );
	
	foreach( $employees as $employee )
	{
	
		$names = $employee->getElementsByTagName( "name" );
		$name = $names->item(0)->nodeValue;
	
		//This example is vulnerable to XSS
		echo $name;
		
		//This example is escaped
		$esc = htmlspecialchars($name);
		
		echo $esc;

	}
		
	/*
	We recommend to not rely soly on the encoding of the input by the Domcocument.
	So before you insert user-input into the XML file you want to have it sanitised.
	See the "Encoding" and "input validation" code examples for more detailed information
	*/


	
	

	
	?> 