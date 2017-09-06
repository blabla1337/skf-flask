# X-XSS-Protection header
-------

## Example:


    """
    In order to set the X-XSS-Protection header, you'll have to add the following code to the head of your application
    """

    @app.after_request
    def anti_XSS(response):
        response.headers["X-XSS-Protection"] = "1; mode=block"
        return response
