# Anti-caching headers
-------

## Example:


	"""
	Add the following headers to your application head in order to prevent the browser from caching
	"""

	@app.after_request
	def anti-Caching(response):
		response.headers["Cache-Control"] = "no-store, no-cache, must-revalidate" #HTTP/1.1
		response.headers["Cache-Control"] = "post-check=0, pre-check=0, false"
		response.headers["Pragma"] = "no-cache"  #HTTP/1.0
		return response
