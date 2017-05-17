X-Path-Query
----------------

***Example:***

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


package prime.com.beans;

import java.io.File;
import java.io.FileInputStream;
import java.io.IOException;

import javax.faces.bean.ManagedBean;
import javax.xml.parsers.DocumentBuilder;
import javax.xml.parsers.DocumentBuilderFactory;
import javax.xml.xpath.XPath;
import javax.xml.xpath.XPathConstants;
import javax.xml.xpath.XPathExpression;
import javax.xml.xpath.XPathExpressionException;
import javax.xml.xpath.XPathFactory;

import org.apache.log4j.Logger;
import org.w3c.dom.Document;
import org.xml.sax.InputSource;

import com.edw.inputValidation; 

@ManagedBean
public class xpath {
	
	private String employeeID;
	private String employeeRole;

    public String getEmployeeRole() {
		return employeeRole;
	}

	public void setEmployeeRole(String employeeRole) {
		this.employeeRole = employeeRole;
	}

	public String getEmployeeID() {
        return employeeID;
    }
 
    public void setEmployeeID(String employeeID) {
        this.employeeID = employeeID;
    }
    
    
	final static Logger logger = Logger.getLogger(xpath.class);

	 public void selectPath()
     {
          /*
          In order to prevent x-path injections we have to treat these query's similar as 
          to the SQL query's. An option would be to use a pre-compiled XPath query.
          But since this is a third party library i consider it untrusted and would
          rather use our own crafted escaping function.

          NOTE: if you want to look into the pre-compiled x-path library you can find more
          detailed information about it on: http://www.onjava.com/pub/a/onjava/2005/01/12/xpath.html
          */

          /*
          As with every injection prevention we first focus on the expected user values
          in this case we expect an integer we use our single input validation method for integers
          See the "input validation" code example for more detailed information.
          
          For this example we use the following XML snippet 
          
          		<?xml version="1.0" encoding="utf-8"?>
					<Employees>
					   <Employee ID="1">
					      <FirstName>Arnold</FirstName>
					      <LastName>Baker</LastName>
					      <UserName>ABaker</UserName>
					      <Password>SoSecret</Password>
					      <Type>Admin</Type>
					   </Employee>
					   <Employee ID="2">
					      <FirstName>Peter</FirstName>
					      <LastName>Pan</LastName>
					      <UserName>PPan</UserName>
					      <Password>NotTelling</Password>
					      <Type>User</Type>
					   </Employee>
					</Employees>

          */
     
		 boolean continueFunction = true;
         

         inputValidation validate = new inputValidation();
         
         
         //Here we put the variable in our input validation method in order to prevent untrusted user input from parsing
         //NOTE: logging and countering is also done in your validation method
        //Input used into an XPATH expression must not contains any of the characters below:

         //	 ( ) = ' [ ] : , * / WHITESPACE
         
         //Another method of avoiding XPath injections is by using variable into XPATH expression with a variable //resolver enabled evaluator. 
         //See XPath parameterization example
         
         if (validate.validateInput("", employeeID, "xpath", "x-path input validation", "HIGH") == false) 
         { continueFunction = false; }

		
         //Only if our validation function returned true we put the user input in the function
         //fXmlFile is the java.io.File object of the example XML document.
         File fXmlFile = new File("C:\\xmldb\\users.xml");
         
                  
         if (continueFunction == true)
         {     	 
                	 
				try { 					
        	 
					//The evaluate methods in the XPath and XPathExpression interfaces 
					//are used to parse an XML document with XPath expressions.					
					DocumentBuilderFactory factory = DocumentBuilderFactory.newInstance();
	       			DocumentBuilder builder = factory.newDocumentBuilder();
	       		    //Create an InputSource for the example XML document.
	        	    //An InputSource is a input class for an XML entity.	        	    
	       			Document document = builder.parse(new InputSource(new FileInputStream(fXmlFile)));
	       		    //The XPathFactory class is used to create an XPath object.
					//Create an XPathFactory object with the static newInstance method of the XPathFactory class.
	        	    XPathFactory xPathfactory = XPathFactory.newInstance();
        	  
	        	    //Create an XPath object from the XPathFactory object with the newXPath method.
        	  
	        	    XPath xpath = xPathfactory.newXPath();
        	  
	        	    //Create and compile an XPath expression with the compile method of the XPath object. 
	        	    //As an example, select the title of the article with its date attribute set to January-2004.
	        	    //An attribute in an XPath expression is specified with an @ symbol. 
	        	    //For further reference on XPath expressions, 
	        	    //see the XPath specification for examples on creating an XPath expression.
	        	    
	        	    XPathExpression expr = xpath.compile("/Employees/Employee[@ID=" + "'" + employeeID + "'" + "]/Type");	        	    
	        	    
	        	    //The evaluate method of the XPathExpression interface evaluates
	        	    //either an InputSource or a node/node list of the types org.w3c.dom.
	        	    //Node, org.w3c.dom.NodeList, or org.w3c.dom.Document.
	        	    //Evaluate the XPath expression with the InputSource of the example XML document to evaluate over.
	        	    String numberOfDownloads = expr.evaluate(document, XPathConstants.STRING).toString();
				 	this.setEmployeeRole(numberOfDownloads);
   					   					
				} catch (Exception e) {
	       			e.printStackTrace();
	       		}      	 
          }         

     }
	
}


~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~