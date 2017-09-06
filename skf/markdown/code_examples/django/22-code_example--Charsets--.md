
Charsets
-------

## Example:

    '''
    In order to set the "Charsets" header you'll have to add the following code to the head of your application, the following code could be used in your controller: For Example, text/html
    '''

    #You add directly into the HTML markup
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8">

    '''
    In order to set the "Content-Type" header and charset you'll have to add the following code
    to the head of your application

    For adding Content-Type in everypage we have to add a middleware

    Make a middleware in yourapp/middleware.py
    '''

    class MyMiddleware:

    	def __init__(self, get_response):
        	self.get_response = get_response

    	def __call__(self, request):
        	response = self.get_response(request)
        	
        	# For HTML, the content type is text/html
			response['Content-Type'] = 'text/html; charset=UTF-8'

        	return response
   	
   	# For adding middleware in the project, add in yourproject/settings.py

   	MIDDLEWARE = [
    	...,
    	'yourapp.middleware.MyMiddleware',
    	...,
	]	

	'''
	For adding in the individual response page using render_to_response
	'''

	response = render_to_response("template.html", {})
	
	# For HTML, the content type is text/html
	response['Content-Type'] = 'text/html; charset=UTF-8'
	
	return response

	'''
	For adding in the individual response page using render
	'''

	response = render(request, "template.html", {})
	
	# For HTML, the content type is text/html
	response['Content-Type'] = 'text/html; charset=UTF-8'
	
	return response  