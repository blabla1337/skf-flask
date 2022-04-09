# Question
 
What is the problem here?
 
```
...
@app.route("/")
def start():
    return render_template("index.html")

@app.route("/verify_email", methods = ['POST'])
def regex():
    email = request.form['email']
    match = re.search(r"^([0-9a-zA-Z]([-.\w]*[0-9a-zA-Z])*@{1}([0-9a-zA-Z][-\w]*[0-9a-zA-Z]\.)+[a-zA-Z]{2,9})$", str(email))
    if (match):
        return render_template("index.html", result = "Matched!")
    else:
        return render_template("index.html", result = "Not matched!")

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")
```
 
-----SPLIT-----
 
# Answer

It is an Denial Of Service issue. The Regular expression Denial of Service (ReDoS) is a Denial of Service attack, that exploits the fact that most Regular Expression implementations may reach extreme situations that cause them to work very slowly (exponentially related to input size). An attacker can then cause a program using a Regular Expression (Regex) to enter these extreme situations and then hang for a very long time. https://github.com/blabla1337/skf-labs/tree/master/python/DoS-regex