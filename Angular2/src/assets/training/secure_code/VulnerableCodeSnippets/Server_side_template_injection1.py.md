# Question
 
What is the problem here?
 
```
...
@app.route("/")
def home():
    template = """
....
<div class="panel-heading">Welcome Home!</div>
	<div class="panel-body">
		<div class="col-md-6">
			{0}
		</div>
	</div>
</div>
...
""".format(request.url)
    return render_template_string(template)
```
 
-----SPLIT-----
 
# Answer

It is a Server Side Template Injection (SSTI) issue. The parameter is not being checked for malicious codes and if we supply an arithmentic expression, such as {{1+1}}, the result will be 2 in the response. https://github.com/blabla1337/skf-labs/tree/master/python/SSTI
