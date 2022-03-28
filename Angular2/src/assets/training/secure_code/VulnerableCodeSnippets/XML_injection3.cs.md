# Question
 
What is the problem here?
 
```
private static string codeFinder(string _param)
{
    XmlReaderSettings xmlReaderSettings = new XmlReaderSettings ();
    XmlParserContext xmlParserContext = new XmlParserContext(null, null, null, XmlSpace.None);
    string elementText = null;
    if (!String.IsNullOrEmpty(_param) && !String.IsNullOrEmpty("xsd:code"))
    {
        using (TextReader textReader = new StringReader(_param))
        {
            XmlReader reader = XmlReader.Create(textReader, xmlReaderSettings, xmlParserContext);
            bool foundElement = reader.ReadToFollowing("xsd:code");
            if (foundElement)
                elementText = reader.ReadElementString();   
            reader.Close();
        }
    }
    return elementText;
}
```
 
-----SPLIT-----
 
# Answer

It is a XML injection issue. 'author','_param' is not being sanitized properly and the code is vulnerable for injection attacks.