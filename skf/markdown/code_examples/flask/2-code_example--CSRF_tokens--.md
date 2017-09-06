# CSRF tokens
-------

## Example:


    //The random CSRF token generated need to be send to the server with every form submission. 
    //We are using Flask-WTF, for installing that: 
    //pip install -U Flask-WTF
    //In HTML Forms, for specifying the CSRF we can use the below code

    <form method="post">
      <input type="hidden" name="csrf_token" value="{{ csrf_token() }}"/>
    </form>

	//For ajax requests, we can use the below code

    <script type="text/javascript">
    var csrf_token = "{{ csrf_token() }}";

    $.ajaxSetup({
        beforeSend: function(xhr, settings) {
            if (!/^(GET|HEAD|OPTIONS|TRACE)$/i.test(settings.type) && !this.crossDomain) {
                xhr.setRequestHeader("X-CSRFToken", csrf_token);
            }
        }
    });
    </script>

	//For configuring in the backend, you can use the below code
    import base64
    from OpenSSL import SSL, rand
    from werkzeug.utils import secure_filename
    from flask_wtf.csrf import CSRFProtect, CSRFError

	//Intialize the flask application 
    app = Flask(__name__)

    //To Register CSRF protection globally for the app 
    csrf = CSRFProtect()
    csrf.init_app(app)

    //Configurations 
    //Strictly protection on SSL, Referrer 
    app.config['WTF_CSRF_SSL_STRICT'] = True 

    
    //Always use a WTF_CSRF_SECRET_KEY otherwise by default this will use the Flask app's 
    //SECRET_KEY. So if user didn't WTF_CSRF_SECRET_KEY it will choose SECRET_KEY, 
    //Which may impact the secret key

    //Random string for generating CSRF token
    app.config['WTF_CSRF_SECRET_KEY'] = base64.b64encode(rand.bytes(128)) 

    //Function which is called when CSRF error happens
    @app.errorhandler(CSRFError)
    def handle_csrf_error(e):
        return render_template('csrf_error.html', reason=e.description), 400
	