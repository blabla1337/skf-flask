# Question
 
What is the problem here?
 
```
static void Main(string[] args){
    Console.WriteLine("Please enter student username:");
    string userName = Console.ReadLine();
    XmlDocument doc = new XmlDocument();
    doc.Load("students.xml");
    XmlNode root = doc.DocumentElement;
    XmlNamespaceManager nsmgr = new XmlNamespaceManager(doc.NameTable);
    nsmgr.AddNamespace("sc", "urn:school-schema");
    XmlNode node = root.SelectSingleNode("des::sc:school[sc:class/sc:studentName='"+userName+"']", nsmgr);
}
```
 
-----SPLIT-----
 
# Answer

It is an XPath injection issue. 'userName' parameter is not being sanitized and the attacker can inject malicious commands to the query to retrieve more data from 'students.xml'.
