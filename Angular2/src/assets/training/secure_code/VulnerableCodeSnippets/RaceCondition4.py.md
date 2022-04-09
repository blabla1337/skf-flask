# Question
 
What is the problem here?
 
```
@app.route("/")
def start():
    return render_template("index.html")

@app.route("/<string:value>", methods=['GET'])
def home(value):
    # Create a Python file object using open() and the with statement
    with open("shared-file.txt", 'w') as f:
        f.write(value)
        f.closed

    file = open("shared-file.txt", "r") 
    response = make_response(send_file("shared-file.txt", attachment_filename="shared-file.txt"))
    response.headers.set("Content-Type", "text/html; charset=utf-8")
    response.headers.set("Content-Disposition", "attachment; filename=shared-file.txt")
    return response
```
 
-----SPLIT-----
 
# Answer

It is a Race Condition issue. In the code, we see that the application gets the query string value, writes it to a file called shared-file.txt, then opens the file and sends it back as a response. Additionally, the code does not lock any system resources and that means the request for file writing and the request file reading might be from different people. https://github.com/blabla1337/skf-labs/blob/master/python/RaceCondition-file-write
