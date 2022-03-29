# Question
 
What is the problem here?
 
```
protected void doGet(HttpServletRequest req, HttpServletResponse resp) throws IOException {
  String xml = "<node userName=\"" + req.getParameter("userName") + "\"></node>";
  String xml += "<node userAddress=\"" + req.getParameter("userAddress") + "\"></node>";
  String xml += "<node UserPhone=\"" + req.getParameter("UserPhone") + "\"></node>";
  DocumentBuilderFactory factory = DocumentBuilderFactory.newInstance();
  DocumentBuilder builder = factory.newDocumentBuilder();
  Document doc = builder.parse(new InputSource(new StringReader(xml)));
}
```
 
-----SPLIT-----
 
# Answer

It is an XML injection issue. 'userName','userAddress' and 'UserPhone' parameters are not being checked while building the xml file. The attacker can manipulate the file content more than she/he is supposed to do.
