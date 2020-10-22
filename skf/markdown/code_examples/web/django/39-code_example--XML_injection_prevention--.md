# XML injection prevention
-------


## Example:


    """
	
	Whenever you are using XML parsers you must sanitize or encode al user-input before
	including this input into your XML file.

	Some methods like below, the Dom document already encodes the input before storing it
	into the XML. But beware, since this encoded input is still a threat whenever you are
	displaying the this data on screen as HTML output. This encoded data should be escaped
	at all times before displaying.

	Whenever your XML function does not encode your data on the fly, you may want to write
	your own function for achieving this. See the code examples and search for "Input encoding"
	for more detailed information.
	"""


	//Let us take an easy example where we store your favorite number name into a XML file.
	from lxml import etree

	//Create Root Element employees

	root = etree.Element("employees")
	
	//Create child Element for employees
	employee = etree.SubElement(root, "employee")
	name = etree.SubElement(employee, "name")
	
	//Insert the text in name tag
	name.text = request.form['name']

	//Save it in xml file
	with open("test.xml", "w") as f:
		f.write(etree.tostring(root, pretty_print=True))

	"""
	We will try to insert <script>alert(123);</script> into the XML file,
	Now after inserting the employee name into the XML file it will look like:


		<?xml version="1.0"?>
		<employees>
			<employee>
				<name>&lt;script&gt;alert(123);&lt;/script&gt;</name>
			</employee>
		</employees>

		As you can see de input has been encoded but still can trigger an XSS whenever we
		extract the data as shown in the example below:

	NOTE: if you ever want to include the xml files by means of user-selected sources,
	be aware of the fact that an attacker could also include sources from external websites
	and even execute External entity injections on your applications. See the "XSLT injection prevention"
	code example for more detailed information on how to implement this type of functionality since
	the same principle's apply to both functions.
	"""
	
		//Read from a XML file
		x = etree.parse("test.xml")


		for element in x.iter("name"):
   	 		//This example is vulnerable to XSS
   	 		print element.text

   	 		//This example is escaped
   	 		print escape(element.text)

	"""
	We recommend to not rely solely on the encoding of the input by the Dom document.
	So before you insert user-input into the XML file you want to have it sanitized.
	See the "Encoding" and "input validation" code examples for more detailed information
	"""

 
