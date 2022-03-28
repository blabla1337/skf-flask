# Question
 
What is the problem here?
 
```
...
@app.route('/index')
def index():
   return render_template('index.html')
	
@app.route('/fileUpload', methods = ['POST'])
def fileUpload():
   sessionid=request.cookies.get('session_token')
   if sessionValidation(sessionid):
      if request.method == 'POST':
         uploaded_file = request.files['file']
         if uploaded_file.filename != '':
            uploaded_file.save(uploaded_file.filename)
            return HttpResponse("<html><body>%s file has been uploaded.</body></html>" % uploaded_file.filename)
         else:
            return HttpResponse("<html><body>Please provide a valid file name!")
   else:
      return render_template("403.html")

@app.route("/login", methods=['GET', 'POST'])
def login():
      sqli  = Classes()
      values = sqli.getUser(request.form['username'])
      if values:
        if values[0][2] == request.form['password']:
            session['session_token'] = base64.b64encode(str(uuid.uuid4()).encode())
            session_token = str(session['session_token'], 'utf-8')
            return render_template("loggedin.html", session_token = session_token )
      return render_template("403.html")
```
 
-----SPLIT-----
 
# Answer

It is a Filename Injection issue. The code does not perform a proper check for 'filename' parameter and if it is not blank, the service response looks very suspicious for XSS attacks.