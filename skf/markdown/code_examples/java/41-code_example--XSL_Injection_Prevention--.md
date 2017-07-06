XSL Injection Prevention 
-------------------------

***Example:***

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

/*
In order to prevent XSL injections you must enforce strict policy's whenever the
files are loaded from a source controlled by a possible attacker.

Let's say for example that the user can choose from several XSL files on your application.

ABC.xsl arranges your employee names on alphabetical order
CBA.xsl just shows the input by order of your XML file.

Before attaching the XSL files to the style sheet we first want to 
do validation on the request to make sure the included file was one of our own predefined files
*/

package com.edw;

import java.io.File;
import java.io.IOException;

import javax.xml.parsers.DocumentBuilder;
import javax.xml.parsers.DocumentBuilderFactory;
import javax.xml.parsers.FactoryConfigurationError;
import javax.xml.parsers.ParserConfigurationException;
import javax.xml.transform.OutputKeys;
import javax.xml.transform.Source;
import javax.xml.transform.Transformer;
import javax.xml.transform.TransformerException;
import javax.xml.transform.TransformerFactory;
import javax.xml.transform.dom.DOMResult;
import javax.xml.transform.dom.DOMSource;
import org.w3c.dom.ls.LSSerializer;
import org.w3c.dom.Document;
import org.xml.sax.SAXException;
import org.w3c.dom.ls.DOMImplementationLS;

public class IncludeXSL {

	private WhiteList wt = new WhiteList();
	
	public String includeXSL(String WhiteListing, String input)
	{
		LSSerializer serializer = null ;
		boolean continue_ = true;
		Document result = null;
		
		/*
        We want to WhiteList the paged for expected values, in this example they are,
        page1,page2 etc.. for more information about WhiteListing see "white-listing" in the code examples:
        */
		
        if (wt.WhiteListing(WhiteListing, input) == false) { continue_ = false; }
		
        //If all went good we do the function
        if(continue_){
        	//LOAD XML FILE
            //Load the XML source
        	Document xslt = null; 
        	Document xml = null; 
        	try {
        	File fXmlFile = new File(input);
        	DocumentBuilderFactory dbFactory = DocumentBuilderFactory.newInstance();
        	
        	DocumentBuilder db = dbFactory.newDocumentBuilder();
        	
        	xml  = db.newDocument();
        	xslt = db.parse(fXmlFile);
			} catch (SAXException | IOException | ParserConfigurationException e) {
				
			}
        	
            xml.appendChild(xml.createElementNS(null, "root"));
            try {
				 result = transformXML(xml, xslt);
			} catch (TransformerException | ParserConfigurationException | FactoryConfigurationError e) {
				
			}
            serializer = ((DOMImplementationLS) xml.getImplementation()).createLSSerializer();
        	
        	

        }
        return serializer.writeToString(result); 
	}
	
    //Configure the transformer
	public static Document transformXML(Document xml, Document xslt) throws TransformerException, ParserConfigurationException, FactoryConfigurationError {

        Source xmlSource = new DOMSource(xml);
        Source xsltSource = new DOMSource(xslt);
        DOMResult result = new DOMResult();

        // the factory pattern supports different XSLT processors
        TransformerFactory transFact = TransformerFactory.newInstance();
        Transformer trans = transFact.newTransformer(xsltSource);
        trans.setOutputProperty(OutputKeys.ENCODING, "UTF-8");
        trans.transform(xmlSource, result);

        Document resultDoc = (Document) result.getNode();

        return resultDoc;
    }
}

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~