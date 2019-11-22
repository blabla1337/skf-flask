# Charsets
-------

## Example:


    """
    In order to set the "Charsets" header you'll have to add the following code to the head of your application, the following code could be used in your controller: For Example, text/html
    """

    //You add directly into the HTML markup
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8">

    @app.after_request
    def content_Type_Charset(response):
      response.headers["Content-Type"] = "text/html; charset=utf-8"
      return response
