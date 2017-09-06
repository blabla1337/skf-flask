# X-Content-Type-Options header
-------

## Example:


    """
    In order to set the "X-Content-Type-Options" header you'll have to add the following code to the head of your application
    """

    @app.after_request
    def anti_ContentType(response):
        response.headers["X-Content-Type-Options"] = "nosniff"
        return response
