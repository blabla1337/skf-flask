# Question
 
What is the problem here?
 
```
index.html:
...
<form method="post" action="/home">
	<input type="text" class="form-control" name="string" placeholder="fill me in plz"/><br/>
    <button class="btn btn-primary" type="submit">Submit Button</button>
</form>
<p style="font-size:2em;"> {{userParam}} </p>
...

...
@app.route("/")
def start():
    return render_template("index.html")

@app.route("/", methods=['POST'])
def home():
    userParam = request.form['string']
    return render_template("index.html",userParam = userParam)

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")
```
 
-----SPLIT-----
 
# Answer

It is an Client Side Template Injection (CSTI) issue. 'userParam' parameter is not being checked for malicious codes. AngularJS parses and renders every expression between curly brackets. So if we pass an arithmentic expression, such as {{7*7}}, the result will be 49 in the response. https://github.com/blabla1337/skf-labs/tree/master/python/CSTI