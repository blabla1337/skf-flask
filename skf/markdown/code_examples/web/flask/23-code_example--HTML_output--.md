# HTML output
-------

## Example:


    """
    Whenever user input is displayed in the application, whether, as content or a parameter value
    submitted towards the url, all user input should be properly escaped to prevent XSS injections.

    Flask uses the Jinja2 templating engine which does auto escaping for you in the right context, with the
    exception of user supplied input being used in a "href" attribute
    """

    from flask import Flask, request, url_for, render_template, redirect

    app = Flask(__name__, static_url_path='/static', static_folder='static')
    app.config['DEBUG'] = False

    @app.route("/")
    def start():
        return render_template("index.html")

    @app.route("/home", methods=['POST'])
    def home():
        xss = request.form['string']
        return render_template("index.html",xss = xss)
        
    if __name__ == '__main__':
        app.run(debug=True,host='0.0.0.0')


    """
    in order to detect XSS see if the auto escape function is used
    """

    <p style="font-size:2em;"> {% autoescape false %}{{xss}}{% endautoescape %} </p>
    

    """
    A simple example to prevent XSS in Href attribute could be something like:
    """

    @app.route("/home", methods=['POST'])
    def home():
        xss = request.form['string']
        if not line.startswith("https://"):
            #EXIT code here
        return render_template("index.html",xss = xss)