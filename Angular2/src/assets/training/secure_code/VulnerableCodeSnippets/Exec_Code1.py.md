# Question
 
What is the problem here?
 
```
...
@app.route("/", methods=['GET'])
def start():
    return render_template("index.html")

@app.route("/", methods=['POST'])
def home():
    text_input = request.form['text']
    os.system('echo ' + text_input + ' >> welcome')
    text = "WELCOME!"
    return render_template("index.html", read = text)

@app.route('/admin', methods=['GET'])
def notAllow():
    return render_template("404.html")
```
 
-----SPLIT-----
 
# Answer

It is a Code Execution issue. 'text' parameter is not being checked for any malicous code and the attacker can execute consecutive commands with OS delimeters, such as ";". https://github.com/blabla1337/skf-labs/blob/master/python/CMD-Blind