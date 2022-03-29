# Question
 
What is the problem here?
 
```
/*

XML File
    <!DOCTYPE contacts SYSTEM "contacts.dtd">
    <contacts>
     <contact>
      <firstname>John</firstname>
      <lastname>&abc;</lastname>
     </contact>
    </contacts>

DTD File
    <!ELEMENT contacts (contact*)>
    <!ELEMENT contact (firstname,lastname)>
    <!ELEMENT firstname (#PCDATA)>
    <!ELEMENT lastname ANY>
    <!ENTITY abc SYSTEM "/etc/passwd">

*/
...
public static void main(String[] args) {
    try {
    DocumentBuilderFactory factory = DocumentBuilderFactory.newInstance();
    DocumentBuilder builder = factory.newDocumentBuilder();
    Document doc = builder.parse(new InputSource("contacts.xml"));
    NodeList nodeList = doc.getElementsByTagName("contact");
    for (int s = 0; s < nodeList.getLength(); s++) {
        Node firstNode = nodeList.item(s);
        if (firstNode.getNodeType() == Node.ELEMENT_NODE) {
            Element firstElement = (Element) firstNode;
            NodeList firstNameElementList = firstElement.getElementsByTagName("firstname");
            Element firstNameElement = (Element) firstNameElementList.item(0);
            NodeList firstName = firstNameElement.getChildNodes();
            System.out.println("First Name: "  + ((Node) firstName.item(0)).getNodeValue());
            NodeList lastNameElementList = firstElement.getElementsByTagName("lastname");
            Element lastNameElement = (Element) lastNameElementList.item(0);
            NodeList lastName = lastNameElement.getChildNodes();
            System.out.println("Last Name: " + ((Node) lastName.item(0)).getNodeValue());
            }
        }
    } catch (Exception e) { e.printStackTrace(); }
}
```
 
-----SPLIT-----
 
# Answer

It is an XML injection issue. If the parser uses a DTD, an attacker might inject data that may adversely affect the XML parser during document processing. These adverse effects could include the parser crashing or accessing local files. For the example, the code may reveal content of '/etc/passwd' file. https://cheatsheetseries.owasp.org/cheatsheets/XML_Security_Cheat_Sheet.html
