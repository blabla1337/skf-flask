# X-XSS-Protection header
-------

## Example:

    
    """
    In order to set the X-XSS-Protection header, you'll have to add the following code to the head of your application

    For adding X-XSS Protection in everypage we have to add a middleware
    Make a middleware in yourapp/middleware.py
    """

    class MyMiddleware:

    	def __init__(self, get_response):
        	self.get_response = get_response

    	def __call__(self, request):
        	response = self.get_response(request)
        	response['X-XSS-Protection'] = "1; mode=block"
        	return response
   	
   	//For adding middleware in the project, add in yourproject/settings.py
   	MIDDLEWARE = [
    	...,
    	'yourapp.middleware.MyMiddleware',
    	...,
	]	

	//For adding in the individual response page using render_to_response
	response = render_to_response("template.html", {})
	response['X-XSS-Protection'] = '1; mode=block'

	return response

	//For adding in the individual response page using render
	response = render(request, "template.html", {})
	response['X-XSS-Protection'] = '1; mode=block'

	return response