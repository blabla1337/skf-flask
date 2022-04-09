# Question
 
What is the problem here?
 
```
...
@app.route("/")
def start():
    return render_template("index.html")

@app.route("/home", methods=['POST', 'GET'])
def home():
    param = parseString(request.form['parameter'])
    try:
        for event, node in param:
            if event == START_ELEMENT and node.localName == "items":
                param.expandNode(node)
                nodes = node.toxml()
        return render_template("index.html", nodes=nodes)
    except (UnboundLocalError, xml.sax._exceptions.SAXParseException):
        return render_template("index.html")

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")
```
 
-----SPLIT-----
 
# Answer

It is an XML Injection issue. 'parameter' is not being checked properly. A special created XML request will allow attackers to take advantage of this weakness. https://github.com/blabla1337/skf-labs/blob/master/python/XXE
