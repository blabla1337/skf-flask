# Question
 
What is the problem here?
 
```
@app.route('/uploader', methods = ['POST'])
def route():
    content_type = request.args["Content-Type"]
    if content_type == "text/html":
        fle = request.files['file']
        fle.save(fle.filename)
        return 'file has been uploaded successfully'
    else:
        return 'you can only upload text files!'

@app.route('/upload')
def upload_file():
   return render_template('upload.html')
```
 
-----SPLIT-----
 
# Answer

It is a Header Injection issue. 'Content-Type' parameter is vulnerable for manipulation. Attacker can change the request 'content-type' to anything to upload files she/he wants. The application only allows text files, however the restriction can be easily bypassed.