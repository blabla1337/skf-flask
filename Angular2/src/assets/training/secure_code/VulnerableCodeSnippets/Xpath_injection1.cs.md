# Question
 
What is the problem here?
 
```
protected void Page_Load(object sender, EventArgs e){
    if (Request.QueryString["town"] != null){
        string xmlPath = @"C:\\file.xml";
        strting town = Request.QueryString["townName"];
        XmlDocument xDoc = new XmlDocument();
        xDoc.LoadXml(xmlPath);
        XmlNodeList list = xDoc.SelectNodes("//sales[town='" + town + "']");
        if (list.Count > 0)
            Console.WriteLine("Record found.");
    }
}    
```
 
-----SPLIT-----
 
# Answer

It is an XPath injection issue. 'town' parameter is not being sanitized and the attacker can inject malicious commands to retrieve more data.
