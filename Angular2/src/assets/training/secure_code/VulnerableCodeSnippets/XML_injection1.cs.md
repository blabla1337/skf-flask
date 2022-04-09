# Question
 
What is the problem here?
 
```
public static JsonNode dataFiller(URI paramURI){
    try {
        DocumentBuilderFactory factory = DocumentBuilderFactory.newInstance();
        factory.setNamespaceAware(true);
        DocumentBuilder builder = factory.newDocumentBuilder();
        Document doc = builder.parse(paramURI);
        XPathFactory xPathfactory = XPathFactory.newInstance();
        XPath xpath = xPathfactory.newXPath();
        String collectionName = StringUtils.trim(getFirstIfPresent(doc, xpath, "//collectionName"));
        String datasetTitle = StringUtils.trim(getFirstIfPresent(doc, xpath, "//dataset/title"));
        String name = StringUtils.isBlank(collectionName) ? datasetTitle : collectionName;
        String pubDate = StringUtils.trim(getFirstIfPresent(doc, xpath, "//pubDate"));
        String citation = StringUtils.trim(getFirstIfPresent(doc, xpath, "//citation"));
        ObjectNode objectNode = new ObjectMapper().createObjectNode();
        String datasetCitation = Stream.of(name, pubDate,citation)
                .filter(StringUtils::isNotBlank)
                .collect(Collectors.joining(". "));
        objectNode.put("citation", datasetCitation + ".");
        objectNode.put("format", MIME_TYPE_DWCA);
        String string = new ObjectMapper().writeValueAsString(objectNode);
        return new ObjectMapper().readTree(string);
    } catch (XPathExpressionException | ParserConfigurationException | IOException | SAXException e) {
        throw new IOException("failed to handle xpath", e);
    }
}
```
 
-----SPLIT-----
 
# Answer

It is an XML Injection issue. 'paramURI' parameter is vulnerable for malicious injection and no input sanitization is being performed.
