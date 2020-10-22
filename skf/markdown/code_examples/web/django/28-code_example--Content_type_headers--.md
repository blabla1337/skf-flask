# Content type headers
-------

## Example:


	"""
    In order to set the "Content-Type" header you'll have to add the following code to the head of your application

    For adding Content-Type in every page we have to add a middleware
    Make a middleware in yourapp/middleware.py
    """

    class MyMiddleware:

    	def __init__(self, get_response):
        	self.get_response = get_response

    	def __call__(self, request):
        	response = self.get_response(request)
        	
        	//For HTML, the content type is text/html
			response['Content-Type'] = 'text/html; charset=UTF-8'
			
			//For Json, the content type is application/json
			response['Content-Type'] = 'application/json'
        	
        	return response
   	
   	//For adding middleware in the project, add in yourproject/settings.py
   	MIDDLEWARE = [
    	...,
    	'yourapp.middleware.MyMiddleware',
    	...,
	]	

	"""
	For adding in the individual response page using render_to_response
	"""

	response = render_to_response("template.html", {})

	//For HTML, the content type is text/html
	response['Content-Type'] = 'text/html; charset=UTF-8'
	//For Json, the content type is application/json
	response['Content-Type'] = 'application/json'
	
	return response

	"""
	For adding in the individual response page using render
	"""

	response = render(request, "template.html", {})
	
	//For HTML, the content type is text/html
	response['Content-Type'] = 'text/html; charset=UTF-8'
	//For Json, the content type is application/json
	response['Content-Type'] = 'application/json'
	
	return response   