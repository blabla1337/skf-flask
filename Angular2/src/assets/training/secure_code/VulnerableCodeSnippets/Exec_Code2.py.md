# Question
 
What is the problem here?
 
```
...
@app.route("/", methods=['GET'])
def start():
    return render_template("index.html")

@app.route("/", methods=['POST'])
def home():
    # input sanitization
    ip_address = request.form['text']
    ip_address = ip_address.replace("`","")
    ip_address = ip_address.replace(";","")
    ip_address = ip_address.replace("&","")
    print("###" + ip_address)
    os.system('ping -c1 ' + ip_address + ' > ./ping_output')
    f = open("ping_output", "r")
    output = f.readlines()
    return render_template("index.html", read = output)

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")
```
 
-----SPLIT-----
 
# Answer

It is a Code Execution issue. 'text' parameter is being checked for only some certain chars. However the attacker can still execute consecutive commands with OS delimeters, such as "|". https://github.com/blabla1337/skf-labs/tree/master/python/CMD4
