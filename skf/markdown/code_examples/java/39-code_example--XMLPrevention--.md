# XML Injection Prevention 
-------

## Example:


	package com.edw;

	import java.io.FileOutputStream;
	import java.io.IOException;
	import java.util.ArrayList;
	import javax.xml.parsers.DocumentBuilder;
	import javax.xml.parsers.DocumentBuilderFactory;
	import javax.xml.parsers.ParserConfigurationException;
	import javax.xml.transform.OutputKeys;
	import javax.xml.transform.Transformer;
	import javax.xml.transform.TransformerException;
	import javax.xml.transform.TransformerFactory;
	import javax.xml.transform.dom.DOMSource;
	import javax.xml.transform.stream.StreamResult;
	import com.edw.InputValidation; 

	import org.w3c.dom.Document;
	import org.w3c.dom.Element;

	public final class XMLPrevention {

		public void storeFunction(String name, String lastName, String gender)
		{
			/*
			First we import our InputValidation class. for more detailed information about 
			input validation check the code examples for "Input validation" & "Single input validation".
			*/
			InputValidation validate = new InputValidation();
			boolean  doFunction = true;
			//If the function returns false, we do not execute the function
			//see the "input validation" code example for more detailed information about this function
			if (validate.validateInput(name, "alphanumeric", "Invalid userinput name", "HIGH") == false)     { doFunction = false; }
			if (validate.validateInput(lastName, "alphanumeric", "Invalid userinput name", "HIGH") == false) { doFunction = false; }
			if (validate.validateInput(gender, "alphanumeric", "Invalid userinput name", "HIGH") == false)    { doFunction = false; }

			if (doFunction == true)
			{
				Document dom;
				Element e = null;
				String xml = null;

				// instance of a DocumentBuilderFactory
				DocumentBuilderFactory dbf = DocumentBuilderFactory.newInstance();
				try {
					// use factory to get an instance of document builder
					DocumentBuilder db = dbf.newDocumentBuilder();
					// create instance of DOM
					dom = db.newDocument();

					// create the root element
					Element rootEle = dom.createElement("roles");

					// create data elements and place them under root
					e = dom.createElement("name");
					e.appendChild(dom.createTextNode(name));
					rootEle.appendChild(e);

					e = dom.createElement("lastName");
					e.appendChild(dom.createTextNode(lastName));
					rootEle.appendChild(e);

					e = dom.createElement("gender");
					e.appendChild(dom.createTextNode(gender));
					rootEle.appendChild(e);

					dom.appendChild(rootEle);

					try {
						Transformer tr = TransformerFactory.newInstance().newTransformer();
						tr.setOutputProperty(OutputKeys.INDENT, "yes");
						tr.setOutputProperty(OutputKeys.METHOD, "xml");
						tr.setOutputProperty(OutputKeys.ENCODING, "UTF-8");
						tr.setOutputProperty(OutputKeys.DOCTYPE_SYSTEM, "roles.dtd");
						tr.setOutputProperty("{http://xml.apache.org/xslt}indent-amount", "4");

						// send DOM to file
						tr.transform(new DOMSource(dom),new StreamResult(new FileOutputStream(xml)));

					} catch (TransformerException te) {
						System.out.println(te.getMessage());
					} catch (IOException ioe) {
						System.out.println(ioe.getMessage());
					}
				} catch (ParserConfigurationException pce) {
					System.out.println("UsersXML: Error trying to instantiate DocumentBuilder " + pce);
				}
			}
		}
	}

	/*
	Now we prevented malicious user input from coming into your XML file.
	NOTE: Do not forget to also properly encode your input as a last line of defense, 
	 	  also In this example the XmlReader disables external entities by default.
		  If you should choose another parser make sure your parser disables these entities 
		  in order to prevent XXE injections.
	*/

