# Question
 
What is the problem here?
 
```
/*
<users>
	<user>
		<login>john</login>
		<password>abracadabra</password>
		<home_dir>/home/john</home_dir>
	</user>
	<user>
		<login>cbc</login>
		<password>1mgr8</password>
		<home_dir>/home/cbc</home_dir>
	</user>
</users>
*/
...
XPath xpath = XPathFactory.newInstance().newXPath();
XPathExpression xlogin = xpath.compile("//users/user[login/text()='" + login.getUserName() + "' and password/text() = '" + login.getPassword() + "']/home_dir/text()");
Document d = DocumentBuilderFactory.newInstance().newDocumentBuilder().parse(new File("db.xml"));
String homedir = xlogin.evaluate(d);
...
```
 
-----SPLIT-----
 
# Answer

It is an Xpath Injection issue. Consider the XML document that stores authentication information and a snippet of Java code that uses XPath query to retrieve authentication information and retrieve the home directory based on the provided credentials. Assume that user "john" wishes to leverage XPath Injection and login without a valid password. By providing a username "john" and password "' or ''='". https://cwe.mitre.org/data/definitions/643.html