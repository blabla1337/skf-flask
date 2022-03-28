# Question
 
What is the problem here?
 
```
...
@app.route("/")
def start():
    return render_template("index.html")

@app.route("/home", methods=['POST'])
def home():
    filename = request.form['filename']
    filename=filename.replace('../','')
    if os.path.isfile(current_app.root_path + '/'+ filename):
        with current_app.open_resource(filename) as f:
            read = f.read()
    else: 
        read='File not found!'
    return render_template("index.html",read = read)

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")
```
 
-----SPLIT-----
 
# Answer

It is a  Local File Inclusion(LFI) issue. 'filename' parameter is not sanitized for injections properly. You may notice, the code replace '../' with nothing, however the attacker can still fool it with: ..././..././etc/passwd. https://github.com/blabla1337/skf-labs/blob/master/python/LFI-2