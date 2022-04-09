# Question
 
What is the problem here?
 
```
...
app.config.update(dict(
    SECRET_KEY= "woopie",
    SESSION_COOKIE_HTTPONLY = True
))

@app.route("/login", methods=['GET', 'POST'])
def login():
    sqli  = Classes()
    values = sqli.getUser(request.form['username'])
    if values:
        if values[0][2] == request.form['password']:
            session['userId'] = values[0][0]
            session['loggedin'] = True
            time = strftime("%H:%M", gmtime())
            session_identifier = request.form['username'] + time
            session['session_token'] = base64.b64encode(session_identifier.encode())
            session_token = str(session['session_token'], 'utf-8')
            pref = sqli.getColor(values[0][0])
            color = pref[0][0]
            return render_template("loggedin.html", color = color, session_token = session_token )
    return render_template("index.html")

@app.route("/update", methods=['POST', 'GET'])
def update():
    if not session.get('loggedin'):
        return render_template('index.html')
    sqli  = Classes()
    if request.method == "POST":
        session_token = str(session['session_token'], 'utf-8')
        if session_token == request.form['session_token']:
            sqli.updateColor(request.form['color'], session.get('userId'))
        else:
            return render_template("loggedin.html", error = "Session Token was not correct")
    pref = sqli.getColor(session.get('userId'))
    color = pref[0][0]
    return render_template("loggedin.html", color = color)
```
 
-----SPLIT-----
 
# Answer

It is an Cross-Site Request Forgery (CSRF) issue. 'session_token' value is an unique session identifier however it is easily guessable. The intruder can calculate it, and then perform her/his attack. https://github.com/blabla1337/skf-labs/blob/master/python/CSRF-weak
