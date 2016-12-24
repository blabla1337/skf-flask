X-Path-Query
----------------

***Example:***

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


package com.edw;

import java.io.File;
import java.io.FileInputStream;
import java.io.IOException;

import javax.xml.xpath.XPath;
import javax.xml.xpath.XPathExpression;
import javax.xml.xpath.XPathExpressionException;
import javax.xml.xpath.XPathFactory;

import org.apache.log4j.Logger;
import org.xml.sax.InputSource; 

public class xpath {
	
	
	final static Logger logger = Logger.getLogger(xpath.class);

	 public String selectPath(String employeeID)
     {
          /*
          In order to prevent x-path injections we have to treat these query's similar as 
          to the sql query's. An option would be to use a precompiled XPath query.
          But since this is a third party library i consider it untrusted and would
          rather use our own crafted escaping function.

          NOTE: if you want to look into the precompiled x-path library you can find more
          detailed information about it on: http://www.onjava.com/pub/a/onjava/2005/01/12/xpath.html
          */

          /*
          As with every injection prevention we first focus on the expected user values
          in this case we expect an integer we use our single input validation method for integers
          See the "input validation" code example for more detailed information.
          */
     
		 boolean continueFunction = true;
         String foo = "";

         inputvalidation validate = new inputvalidation();
         
         
         //Here we put the variable in our inputvalidation method in order to prevent untrusted userinput from parsing
         //NOTE: logging and countering is also done in your validation method
         if (validate.validateInput( employeeID, "nummeric", "x-path input validation", "HIGH") == false) 
         { continueFunction = false; }

		
         //Only if our validation function returned true we put the userinput in the function
         //fXmlFile is the java.io.File object of the example XML document.
         File fXmlFile = new File("C:\\Users\\Public\\xml\\register.xml");
         
         if (continueFunction == true)
         {
        	 
				try { 					
        	 
					//The evaluate methods in the XPath and XPathExpression interfaces 
					//are used to parse an XML document with XPath expressions.
					//The XPathFactory class is used to create an XPath object.
					//Create an XPathFactory object with the static newInstance method of the XPathFactory class.
	        	    XPathFactory factory=XPathFactory.newInstance();
	        	    //Create an XPath object from the XPathFactory object with the newXPath method.
	        	    XPath xPath=factory.newXPath();
	        	    //Create and compile an XPath expression with the compile method of the XPath object. 
	        	    //As an example, select the title of the article with its date attribute set to January-2004.
	        	    //An attribute in an XPath expression is specified with an @ symbol. 
	        	    //For further reference on XPath expressions, 
	        	    //see the XPath specification for examples on creating an XPath expression.
	        	    XPathExpression xPathExpression=xPath.compile("/Employees/Employee[@ID=" + employeeID + "]");
	        	    //Create an InputSource for the example XML document.
	        	    //An InputSource is a input class for an XML entity.
	        	    //The evaluate method of the XPathExpression interface evaluates
	        	    //either an InputSource or a node/node list of the types org.w3c.dom.
	        	    //Node, org.w3c.dom.NodeList, or org.w3c.dom.Document.
	        	    InputSource inputSource = new InputSource(new FileInputStream(fXmlFile));
	        	    //Evaluate the XPath expression with the InputSource of the example XML document to evaluate over.
					foo = xPathExpression.evaluate(inputSource);  		
						
   					   					
				} catch (IOException | XPathExpressionException e) {
							logger.error(e.toString());
				}        	 
          }         
         
         return foo;
          
     }
	
}

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~