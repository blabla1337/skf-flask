# Question
 
What is the problem here?
 
```
welcome.html

<!doctype html>
<title>Welcome to internal audit tool</title>
{% if name %}
  <h1>Hello {{ name }}!</h1>
{% else %}
  <h1>Please enter your name!</h1>
{% endif %}

...
@app.route("/admin")
def start():
    if not session.get('usersessionid'):
        return render_template('403.html')
    return render_template("admin.html")

@app.route('/', methods =['GET'])
def greetings():
    username = request.args.get('username')
    html = open('welcome.html').read()
    response = make_response(html.replace('{{ name }}', username))
    return response

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")
```
 
-----SPLIT-----
 
# Answer

It is a Cross Site Scripting (XSS) issue. 'username' parameter is vulnerable for injection attacks and no input sanitization exists. Injected javascript codes will be executed in the response.
