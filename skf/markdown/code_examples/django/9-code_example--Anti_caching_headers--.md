
Anti-caching headers
-------

## Example:

	'''
    In order to set the Anti-Caching header you'll have to your application head in order to prevent the browser from caching

    For adding Anti-Caching header in every page we have to add a middleware

    Make a middleware in yourapp/middleware.py
    '''

    class MyMiddleware:

    	def __init__(self, get_response):
        	self.get_response = get_response

    	def __call__(self, request):
        	response = self.get_response(request)

        	response["Cache-Control"] = "no-store, no-cache, must-revalidate" #HTTP/1.1
			response["Cache-Control"] = "post-check=0, pre-check=0, false"
			response["Pragma"] = "no-cache"  #HTTP/1.0
        	
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

	response["Cache-Control"] = "no-store, no-cache, must-revalidate" #HTTP/1.1
	response["Cache-Control"] = "post-check=0, pre-check=0, false"
	response["Pragma"] = "no-cache"  #HTTP/1.0

	return response
	
	'''
	For adding in the individual response page using render
	'''

	response = render(request, "template.html", {})
	
	response["Cache-Control"] = "no-store, no-cache, must-revalidate" #HTTP/1.1
	response["Cache-Control"] = "post-check=0, pre-check=0, false"
	response["Pragma"] = "no-cache"  #HTTP/1.0
	
	return response