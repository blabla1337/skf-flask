# XML External Entities 
-------

## Example:


  /*
  The overall prevention method for loading external entities is adding the following line of code:
  This line of code function tells the underlying libxml parsing to not try to interpret the values 
  of the entities in the incoming XML and leave the entity references intact.
  */

  /*
  Both DocumentBuilderFactory and SAXParserFactory XML Parsers can be configured using the same techniques to protect them against XXE.The JAXP DocumentBuilderFactory setFeature method allows a developer to control which implementation-specific XML processor features are enabled or disabled. The features can either be set on the factory or the underlying XMLReader setFeature method. Each XML processor implementation has its own features that govern how DTDs and external entities are processed.
  */

  DocumentBuilderFactory dbf = DocumentBuilderFactory.newInstance();
  String FEATURE = null;

  //or

  SAXParserFactory spf = SAXParserFactory.newInstance();
  SAXParser saxParser = spf.newSAXParser();
  XMLReader reader = saxParser.getXMLReader();
    
  //  DocumentBuilderFactory

  import javax.xml.parsers.DocumentBuilderFactory;
  import javax.xml.parsers.ParserConfigurationException; // catching unsupported features

  DocumentBuilderFactory dbf = DocumentBuilderFactory.newInstance();
      String FEATURE = null;
      try {
        // This is the PRIMARY defense. If DTDs (doctypes) are disallowed, almost all XML entity attacks are prevented
        // Xerces 2 only - http://xerces.apache.org/xerces2-j/features.html#disallow-doctype-decl
        FEATURE = "http://apache.org/xml/features/disallow-doctype-decl";
        dbf.setFeature(FEATURE, true);

        // If you can't completely disable DTDs, then at least do the following:
        // Xerces 1 - http://xerces.apache.org/xerces-j/features.html#external-general-entities
        // Xerces 2 - http://xerces.apache.org/xerces2-j/features.html#external-general-entities
        // JDK7+ - http://xml.org/sax/features/external-general-entities    
        FEATURE = "http://xml.org/sax/features/external-general-entities";
        dbf.setFeature(FEATURE, false);

        // Xerces 1 - http://xerces.apache.org/xerces-j/features.html#external-parameter-entities
        // Xerces 2 - http://xerces.apache.org/xerces2-j/features.html#external-parameter-entities
        // JDK7+ - http://xml.org/sax/features/external-parameter-entities    
        FEATURE = "http://xml.org/sax/features/external-parameter-entities";
        dbf.setFeature(FEATURE, false);

        // Disable external DTDs as well
        FEATURE = "http://apache.org/xml/features/nonvalidating/load-external-dtd";
        dbf.setFeature(FEATURE, false);

        // and these as well, per Timothy Morgan's 2014 paper: "XML Schema, DTD, and Entity Attacks" (see reference below)
        dbf.setXIncludeAware(false);
        dbf.setExpandEntityReferences(false);
  
        // And, per Timothy Morgan: "If for some reason support for inline DOCTYPEs are a requirement, then 
        // ensure the entity settings are disabled (as shown above) and beware that SSRF attacks
        // (http://cwe.mitre.org/data/definitions/918.html) and denial 
        // of service attacks (such as billion laughs or decompression bombs via "jar:") are a risk."

        // remaining parser logic
        ...
  
        } catch (ParserConfigurationException e) {
              // This should catch a failed setFeature feature
              logger.info("ParserConfigurationException was thrown. The feature '" +
                          FEATURE +
                          "' is probably not supported by your XML processor.");
              ...
          }
          catch (SAXException e) {
              // On Apache, this should be thrown when disallowing DOCTYPE
              logger.warning("A DOCTYPE was passed into the XML document");
              ...
          }
          catch (IOException e) {
              // XXE that points to a file that doesn't exist
              logger.error("IOException occurred, XXE may still possible: " + e.getMessage());
              ...
          }
      
      
      
      
      
  // SAXParserFactory
      
      
  import javax.xml.parsers.ParserConfigurationException;  // catching unsupported features
  import javax.xml.parsers.SAXParser;
  import javax.xml.parsers.SAXParserFactory;
  
  import org.xml.sax.SAXNotRecognizedException;  // catching unknown features
  import org.xml.sax.SAXNotSupportedException;  // catching known but unsupported features
  import org.xml.sax.XMLReader;
  
  ...
  
      SAXParserFactory spf = SAXParserFactory.newInstance();
      SAXParser saxParser = spf.newSAXParser();
      XMLReader reader = saxParser.getXMLReader();
  
      try {
        // Xerces 1 - http://xerces.apache.org/xerces-j/features.html#external-general-entities
        // Xerces 2 - http://xerces.apache.org/xerces2-j/features.html#external-general-entities
  
        // Using the SAXParserFactory's setFeature
        spf.setFeature("http://xml.org/sax/features/external-general-entities", false);
        // Using the XMLReader's setFeature
        reader.setFeature("http://xml.org/sax/features/external-general-entities", false);
  
  
        // Xerces 2 only - http://xerces.apache.org/xerces-j/features.html#external-general-entities
        spf.setFeature("http://apache.org/xml/features/disallow-doctype-decl", true);
  
        // remaining parser logic
        ...
  
      } catch (ParserConfigurationException e) {
        // Tried an unsupported feature.
  
      } catch (SAXNotRecognizedException e) {
        // Tried an unknown feature.
  
      } catch (SAXNotSupportedException e) {
        // Tried a feature known to the parser but unsupported.
  
      } catch ... {
        
      }
  ...




