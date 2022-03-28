# Question
 
What is the problem here?
 
```
@app.route("/")
def start():
    return redirect("/information/eWFtbDogVGhlIGluZm9ybWF0aW9uIHBhZ2UgaXMgc3RpbGwgdW5kZXIgY29uc3RydWN0aW9uLCB1cGRhdGVzIGNvbWluZyBzb29uIQ==", code=302)

@app.route("/information/<input>", methods=['GET'])
def deserialization(input):
    try:
            if not input:
                return render_template("information/index.html")
            yaml_file = base64.b64decode(input)
            content = yaml.load(yaml_file)
    except:
            content = "The application was unable to  to deserialize the object!"
    return render_template("index.html", content = content['yaml'])

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")
```
 
-----SPLIT-----
 
# Answer

It is a Deserialization issue. In the code example the input query string parameter is used to read the input value but as you can see this is under the users control. Instead of just sending the intended text over the request, a potential attacker could abuse this function to also supply his own crafted yaml that the attacker controls. https://github.com/blabla1337/skf-labs/blob/master/python/DES-Yaml