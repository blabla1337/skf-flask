# Server Side Template Injection prevention
-------

## Example:

    
	"""
	Server Side Template Injection, a frequent critical vulnerability that has high chance of 
	mistaken as Cross Site Scripting and miss it entirely. But inline XSS, it can lead attack in 
	Web server and may even obtain a RCE. Template Injection occurs when user input is embedded in a template in an unsafe manner. 
	"""

	//Vulnerable piece of Code which can lead to SSTI
	@app.errorhandler(404)
	def page_not_found(e):
    	template = '''{%% extends "layout.html" %%}
		{%% block body %%}
    	<div class="center-content error">
        <h1>Oops! That page doesn't exist.</h1>
    	<h3>%s</h3>
    	</div>
		{%% endblock %%}
		''' % (request.url)
    	return render_template_string(template), 404

    """
    The above code is vulnerable to SSTI,
    If we give http://www.example.com/ss/<script>alert(1)</script>
    This will show an alert box, which means its vulnerable to XSS
    If we give http://www.example.com/ss/{{3*3}}
    This will show an output 9, which further tells us that it is vulnerable to code injection or SSTI
    """

    //Sanitization of user input can fix the issue
    @app.errorhandler(404)
	def page_not_found(e):

		//Initialize
		continue = True

		//Escape function would fix the issue
    	url = request.url
    	url = escape(url)
    	
    	//Checking the url
    	p = re.compile(r'(http://www.example.com/(.*))(\?.*)?')

    	if inputValidation(url, "alphanumeric") or len(url>20) or inputValidation(url, "alpha"):
    		continue = False
    	
    	if p.match(url) and continue==True:

    		template = '''{%% extends "layout.html" %%}
			{%% block body %%}
    		<div class="center-content error">
        	<h1>Oops! That page doesn't exist.</h1>
    		<h3>%s</h3>
    		</div>
			{%% endblock %%}
			''' % (url)
    		
    		return render_template_string(template), 404

