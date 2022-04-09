# Question
 
What is the problem here?
 
```
templates/greetings.html
<!doctype html>
<title>Welcome our portal</title>
{% if name %}
  <h1>Hello {{ name }}!</h1>
{% else %}
  <h1>Hello!</h1>
{% endif %}

...
@app.route('/users', methods =['GET'])
def users():
    userName = request.args.get('userName', '')
    html = open('templates/greetings.html').read()
    response = make_response(html.replace('{{ name }}', userName))
    return response
```
 
-----SPLIT-----
 
# Answer

It is a Cross Site Scripting (XSS) issue. 'userName' parameter is vulnerable for injection attacks and the code does not sanitize the user inputs properly.
