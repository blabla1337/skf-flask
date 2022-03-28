# Question
 
What is the problem here?
 
```
...
@app.route("/")
def start():
    return render_template("index.html")

@app.route("/home", methods=['POST'])
def home():
    filename = urllib.parse.unquote(request.form['filename'])
    read='File not found!'
    if '../' not in filename:
        filename = urllib.parse.unquote(filename)
        if os.path.isfile(current_app.root_path + '/'+ filename):
            with current_app.open_resource(filename) as f:
                read = f.read()
    return render_template("index.html",read = read)

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")
```
 
-----SPLIT-----
 
# Answer

It is a  Local File Inclusion(LFI) issue. 'filename' parameter is not sanitized for injections properly. You may notice, the code check for '../' however the attacker can still encode the path, for example: %2e%2e%2f%2e%2e%2fetc%2fpasswd - URL encoding. https://github.com/blabla1337/skf-labs/blob/master/python/LFI-3